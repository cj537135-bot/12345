"""Sahara - support platform connecting sex workers with doctors, advocates,
teachers, NGOs, CSR companies, skill institutes, livelihood providers and
restaurants with surplus food.

Run:  pip install -r requirements.txt
      set SECRET_KEY and ADMIN_PASSWORD (see below), then:  python app.py
"""
import os, secrets, sqlite3, hmac, hashlib
from datetime import datetime
from functools import wraps
from flask import (Flask, g, render_template, request, redirect, url_for,
                   session, flash, abort, jsonify)
from i18n import LANGS, RTL, translate
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY") or "local-development-only-change-this"
app.config.update(
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE="Lax",
    SESSION_COOKIE_SECURE=bool(os.environ.get("RENDER")),
)
DB = os.environ.get("DB_PATH", "sahara.db")
_db_parent = os.path.dirname(os.path.abspath(DB))
if _db_parent:
    os.makedirs(_db_parent, exist_ok=True)

# ---------- configuration ----------
PROVIDER_ROLES = {
    "doctor": "Doctor / Clinic",
    "advocate": "Advocate / Legal aid",
    "teacher": "Teacher / Educator",
    "skill_institute": "Skill institute (e.g. BE10X)",
    "work_provider": "Work provider (Griha Udyog / home-based work)",
    "ngo": "NGO",
    "csr": "CSR company / Donor",
    "restaurant": "Restaurant / Food donor",
}
CATEGORIES = {
    "medical": "Medical help", "legal": "Legal help", "education": "Education",
    "skill": "Skill training", "livelihood": "Work / income", "food": "Food",
    "support": "Counselling / shelter / other support",
}
# which request categories each provider role can see and respond to
ROLE_CATEGORIES = {
    "doctor": ["medical"], "advocate": ["legal"], "teacher": ["education"],
    "skill_institute": ["skill"], "work_provider": ["livelihood"],
    "ngo": list(CATEGORIES), "csr": list(CATEGORIES), "restaurant": ["food"],
}

ICONS = {"medical": "🩺", "legal": "⚖️", "education": "📚", "skill": "🛠️", "livelihood": "💼",
         "food": "🍲", "support": "🤝"}
STATES = ["Andhra Pradesh","Arunachal Pradesh","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh",
 "Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha",
 "Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal",
 "Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli and Daman and Diu","Delhi","Jammu and Kashmir",
 "Ladakh","Lakshadweep","Puducherry"]
JOB_ROLES = {"work_provider", "ngo", "csr", "skill_institute", "restaurant"}

def photo_url(name):
    """Use your own (e.g. AI-generated) photo if static/img/<name>.jpg|png|webp exists."""
    for ext in ("jpg", "jpeg", "png", "webp"):
        if os.path.exists(os.path.join(app.static_folder, "img", f"{name}.{ext}")):
            return url_for("static", filename=f"img/{name}.{ext}")
    return None

def clean_state(v):
    return v if v in STATES else ""

def tr(key):
    return translate(session.get("lang", "en"), key)

def video_url(offer_id):
    """Unguessable Jitsi Meet room per offer (free, no account needed)."""
    h = hmac.new(app.config["SECRET_KEY"].encode(), f"offer-{offer_id}".encode(), hashlib.sha256).hexdigest()[:20]
    return "https://meet.jit.si/sahara-" + h

# ---------- database ----------
def db():
    if "db" not in g:
        g.db = sqlite3.connect(DB, timeout=30)
        g.db.row_factory = sqlite3.Row
        g.db.execute("PRAGMA busy_timeout=30000")
    return g.db

@app.teardown_appcontext
def close_db(_):
    d = g.pop("db", None)
    if d: d.close()

SCHEMA = """
CREATE TABLE IF NOT EXISTS users(
  id INTEGER PRIMARY KEY, role TEXT NOT NULL, username TEXT UNIQUE NOT NULL,
  password_hash TEXT NOT NULL, display_name TEXT NOT NULL, email TEXT, phone TEXT,
  city TEXT, org TEXT, verified INTEGER DEFAULT 0, created TEXT DEFAULT CURRENT_TIMESTAMP);
CREATE TABLE IF NOT EXISTS requests(
  id INTEGER PRIMARY KEY, user_id INTEGER NOT NULL, category TEXT NOT NULL,
  title TEXT NOT NULL, details TEXT, city TEXT, urgency TEXT DEFAULT 'normal',
  contact_note TEXT, contact_phone TEXT, status TEXT DEFAULT 'open', created TEXT DEFAULT CURRENT_TIMESTAMP,
  closed_at TEXT);
CREATE TABLE IF NOT EXISTS stories(
  id INTEGER PRIMARY KEY, user_id INTEGER NOT NULL, request_id INTEGER, category TEXT NOT NULL,
  title TEXT NOT NULL, body TEXT NOT NULL, what_helped TEXT, outcome TEXT, duration_minutes INTEGER,
  status TEXT DEFAULT 'published', created TEXT DEFAULT CURRENT_TIMESTAMP);
CREATE TABLE IF NOT EXISTS offers(
  id INTEGER PRIMARY KEY, request_id INTEGER NOT NULL, provider_id INTEGER NOT NULL,
  message TEXT, status TEXT DEFAULT 'pending', created TEXT DEFAULT CURRENT_TIMESTAMP, updated_at TEXT DEFAULT CURRENT_TIMESTAMP);
CREATE TABLE IF NOT EXISTS messages(
  id INTEGER PRIMARY KEY, offer_id INTEGER NOT NULL, sender_id INTEGER NOT NULL, body TEXT NOT NULL,
  created TEXT DEFAULT CURRENT_TIMESTAMP);
CREATE TABLE IF NOT EXISTS jobs(
  id INTEGER PRIMARY KEY, poster_id INTEGER NOT NULL, title TEXT NOT NULL, description TEXT, city TEXT,
  job_type TEXT, pay TEXT, phone TEXT, status TEXT DEFAULT 'open', created TEXT DEFAULT CURRENT_TIMESTAMP);
CREATE TABLE IF NOT EXISTS applications(
  id INTEGER PRIMARY KEY, job_id INTEGER NOT NULL, user_id INTEGER NOT NULL, message TEXT, contact TEXT,
  created TEXT DEFAULT CURRENT_TIMESTAMP, UNIQUE(job_id, user_id));
CREATE TABLE IF NOT EXISTS food(
  id INTEGER PRIMARY KEY, restaurant_id INTEGER NOT NULL, description TEXT NOT NULL,
  quantity TEXT, city TEXT, pickup_address TEXT, pickup_by TEXT,
  status TEXT DEFAULT 'available', claimed_by INTEGER, created TEXT DEFAULT CURRENT_TIMESTAMP);
"""

def init_db():
    with sqlite3.connect(DB) as c:
        c.executescript(SCHEMA)
        for stmt in ("ALTER TABLE requests ADD COLUMN contact_phone TEXT",   # upgrade older databases
                     "ALTER TABLE requests ADD COLUMN closed_at TEXT",
                     "ALTER TABLE requests ADD COLUMN updated_at TEXT",
                     "ALTER TABLE requests ADD COLUMN beneficiary_done INTEGER DEFAULT 0",
                     "ALTER TABLE requests ADD COLUMN provider_done INTEGER DEFAULT 0",
                     "ALTER TABLE requests ADD COLUMN completed_at TEXT",
                     "ALTER TABLE offers ADD COLUMN updated_at TEXT",
                     "ALTER TABLE users ADD COLUMN state TEXT", "ALTER TABLE requests ADD COLUMN state TEXT",
                     "ALTER TABLE jobs ADD COLUMN state TEXT", "ALTER TABLE food ADD COLUMN state TEXT"):
            try:
                c.execute(stmt)
            except sqlite3.OperationalError:
                pass
        c.execute("UPDATE requests SET updated_at=COALESCE(updated_at, created)")
        c.execute("UPDATE offers SET updated_at=COALESCE(updated_at, created)")
        if not c.execute("SELECT 1 FROM users WHERE role='admin'").fetchone():
            pw = os.environ.get("ADMIN_PASSWORD", "admin123")
            c.execute("INSERT INTO users(role,username,password_hash,display_name,verified)"
                      " VALUES('admin','admin',?, 'Administrator',1)", (generate_password_hash(pw),))

# ---------- auth / csrf helpers ----------
def current_user():
    uid = session.get("uid")
    return db().execute("SELECT * FROM users WHERE id=?", (uid,)).fetchone() if uid else None

def login_required(*roles):
    def deco(f):
        @wraps(f)
        def w(*a, **k):
            u = current_user()
            if not u:
                return redirect(url_for("login"))
            if roles and not (u["role"] in roles or ("provider" in roles and u["role"] in PROVIDER_ROLES)):
                abort(403)
            return f(*a, **k)
        return w
    return deco

@app.before_request
def csrf_protect():
    if request.method == "POST":
        sent = request.form.get("csrf", "") or request.headers.get("X-CSRF", "")
        real = session.get("csrf", "")
        if not real or not secrets.compare_digest(real, sent):
            abort(400, "Invalid form token. Please go back and try again.")

@app.context_processor
def inject():
    session.setdefault("csrf", secrets.token_hex(16))
    lang = session.get("lang", "en")
    return dict(user=current_user(), csrf=session["csrf"], CATEGORIES=CATEGORIES, PROVIDER_ROLES=PROVIDER_ROLES,
                t=lambda k: translate(lang, k), lang=lang, LANGS=LANGS, rtl=lang in RTL, ICONS=ICONS,
                stats=get_stats(), video_url=video_url, photo=photo_url, STATES=STATES)

# ---------- public pages ----------
@app.get("/healthz")
def healthz():
    return {"status": "ok"}, 200

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        f = request.form
        role = f.get("role")
        if role != "beneficiary" and role not in PROVIDER_ROLES:
            abort(400)
        username = f.get("username", "").strip().lower()
        if len(username) < 3 or len(f.get("password", "")) < 8:
            flash("Username must be 3+ characters and password 8+ characters.", "error")
            return render_template("register.html")
        if db().execute("SELECT 1 FROM users WHERE username=?", (username,)).fetchone():
            flash("That username is taken.", "error")
            return render_template("register.html")
        beneficiary = role == "beneficiary"
        # Beneficiaries: only an alias is required. No real name/email/phone needed.
        db().execute(
            "INSERT INTO users(role,username,password_hash,display_name,email,phone,city,org,verified,state)"
            " VALUES(?,?,?,?,?,?,?,?,?,?)",
            (role, username, generate_password_hash(f["password"]),
             f.get("display_name", username).strip() or username,
             f.get("email", "").strip(), f.get("phone", "").strip(),
             f.get("city", "").strip(), f.get("org", "").strip(), 1 if beneficiary else 0, clean_state(f.get("state"))))
        db().commit()
        flash("Registered. " + ("You can log in now." if beneficiary else
              "Our team will verify your organisation before you can respond to requests."), "ok")
        return redirect(url_for("login"))
    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        u = db().execute("SELECT * FROM users WHERE username=?",
                         (request.form.get("username", "").strip().lower(),)).fetchone()
        if u and check_password_hash(u["password_hash"], request.form.get("password", "")):
            session.clear(); session["uid"] = u["id"]; session["csrf"] = secrets.token_hex(16)
            return redirect(url_for("dashboard"))
        flash("Wrong username or password.", "error")
    return render_template("login.html")

@app.route("/logout", methods=["POST"])
def logout():
    session.clear()
    return redirect(url_for("index"))

@app.route("/exit")
def quick_exit():  # "leave this site quickly" button target
    session.clear()
    return redirect("https://www.google.com")

# ---------- dashboards ----------
@app.route("/dashboard")
@login_required()
def dashboard():
    u = current_user()
    if u["role"] == "admin":
        return redirect(url_for("admin"))
    if u["role"] == "beneficiary":
        return redirect(url_for("get_help_dashboard"))
    return redirect(url_for("give_help_dashboard"))

@app.route("/get-help")
@login_required("beneficiary")
def get_help_dashboard():
    u = current_user()
    reqs = db().execute(
        "SELECT r.*, (SELECT COUNT(*) FROM offers o WHERE o.request_id=r.id AND o.status='pending') AS pending, "
        "(SELECT p.display_name FROM offers o JOIN users p ON p.id=o.provider_id WHERE o.request_id=r.id AND o.status='accepted' LIMIT 1) AS helper_name "
        "FROM requests r WHERE r.user_id=? ORDER BY r.created DESC", (u["id"],)).fetchall()
    ready = db().execute(
        "SELECT o.id AS offer_id,o.status,o.message,o.created,r.id AS request_id,r.title,r.category,r.status AS request_status,"
        "p.display_name AS helper_name,p.org,p.role FROM offers o JOIN requests r ON r.id=o.request_id JOIN users p ON p.id=o.provider_id "
        "WHERE r.user_id=? AND o.status IN ('pending','accepted') ORDER BY o.updated_at DESC, o.created DESC", (u["id"],)).fetchall()
    return render_template("dashboard_beneficiary.html", reqs=reqs, ready=ready)

@app.route("/give-help")
@login_required("provider")
def give_help_dashboard():
    u = current_user()
    cats = ROLE_CATEGORIES[u["role"]]
    q = "SELECT r.*, u.display_name AS alias FROM requests r JOIN users u ON u.id=r.user_id " \
        "WHERE r.status='open' AND r.category IN (%s)" % ",".join("?" * len(cats))
    args = list(cats)
    city = request.args.get("city", "").strip()
    state = clean_state(request.args.get("state", ""))
    if city:
        q += " AND lower(r.city) LIKE ?"; args.append("%" + city.lower() + "%")
    if state:
        q += " AND r.state=?"; args.append(state)
    q += " ORDER BY CASE r.urgency WHEN 'urgent' THEN 0 ELSE 1 END, r.created DESC"
    reqs = db().execute(q, args).fetchall()
    mine = db().execute(
        "SELECT o.*, r.title, r.category, r.status AS request_status, r.provider_done, r.beneficiary_done "
        "FROM offers o JOIN requests r ON r.id=o.request_id WHERE o.provider_id=? "
        "ORDER BY o.updated_at DESC, o.created DESC", (u["id"],)).fetchall()
    return render_template("dashboard_provider.html", reqs=reqs, mine=mine, city=city, state=state)

# ---------- help requests ----------
@app.route("/request/new", methods=["GET", "POST"])
@login_required("beneficiary")
def new_request():
    if request.method == "POST":
        f = request.form
        if f.get("category") not in CATEGORIES or not f.get("title", "").strip():
            abort(400)
        db().execute("INSERT INTO requests(user_id,category,title,details,city,urgency,contact_note,contact_phone,state)"
                     " VALUES(?,?,?,?,?,?,?,?,?)",
                     (current_user()["id"], f["category"], f["title"].strip(), f.get("details", "").strip(),
                      f.get("city", "").strip(), "urgent" if f.get("urgency") == "urgent" else "normal",
                      f.get("contact_note", "").strip(), f.get("contact_phone", "").strip(), clean_state(f.get("state"))))
        db().commit()
        flash("Your request was posted. Verified helpers will respond here.", "ok")
        return redirect(url_for("dashboard"))
    return render_template("new_request.html")

@app.route("/request/<int:rid>")
@login_required()
def view_request(rid):
    u = current_user()
    r = db().execute("SELECT r.*, u.display_name AS alias FROM requests r JOIN users u ON u.id=r.user_id"
                     " WHERE r.id=?", (rid,)).fetchone() or abort(404)
    owner = u["id"] == r["user_id"]
    offers = db().execute(
        "SELECT o.*, p.display_name, p.org, p.role, p.email, p.phone FROM offers o"
        " JOIN users p ON p.id=o.provider_id WHERE o.request_id=?", (rid,)).fetchall()
    my_offer = next((o for o in offers if o["provider_id"] == u["id"]), None)
    if not owner and u["role"] != "admin":
        if u["role"] not in PROVIDER_ROLES or r["category"] not in ROLE_CATEGORIES[u["role"]]:
            abort(403)
        offers = [o for o in offers if o["provider_id"] == u["id"]]
    return render_template("request_detail.html", r=r, offers=offers, owner=owner, my_offer=my_offer)

@app.route("/request/<int:rid>/offer", methods=["POST"])
@login_required("provider")
def make_offer(rid):
    u = current_user()
    r = db().execute("SELECT * FROM requests WHERE id=?", (rid,)).fetchone() or abort(404)
    if not u["verified"]:
        flash("Your account is awaiting verification.", "error")
    elif r["category"] not in ROLE_CATEGORIES[u["role"]] or r["status"] != "open":
        abort(403)
    elif db().execute("SELECT 1 FROM offers WHERE request_id=? AND provider_id=?", (rid, u["id"])).fetchone():
        flash("You already offered help on this request.", "error")
    else:
        db().execute("INSERT INTO offers(request_id,provider_id,message,updated_at) VALUES(?,?,?,CURRENT_TIMESTAMP)",
                     (rid, u["id"], request.form.get("message", "").strip()))
        db().execute("UPDATE requests SET updated_at=CURRENT_TIMESTAMP WHERE id=?", (rid,))
        db().commit(); flash("Your offer to help has been sent. The person will see that you are ready to help.", "ok")
    return redirect(url_for("view_request", rid=rid))

@app.route("/offer/<int:oid>/<action>", methods=["POST"])
@login_required("beneficiary")
def respond_offer(oid, action):
    o = db().execute("SELECT o.*, r.user_id FROM offers o JOIN requests r ON r.id=o.request_id WHERE o.id=?",
                     (oid,)).fetchone() or abort(404)
    if o["user_id"] != current_user()["id"] or action not in ("accept", "decline"):
        abort(403)
    db().execute("UPDATE offers SET status=?, updated_at=CURRENT_TIMESTAMP WHERE id=?", ("accepted" if action == "accept" else "declined", oid))
    if action == "accept":
        db().execute("UPDATE offers SET status='declined', updated_at=CURRENT_TIMESTAMP WHERE request_id=? AND id!=? AND status='pending'", (o["request_id"], oid))
        db().execute("UPDATE requests SET status='in_progress', provider_done=0, beneficiary_done=0, updated_at=CURRENT_TIMESTAMP WHERE id=?", (o["request_id"],))
    else:
        db().execute("UPDATE requests SET updated_at=CURRENT_TIMESTAMP WHERE id=?", (o["request_id"],))
    db().commit()
    return redirect(url_for("view_request", rid=o["request_id"]))

@app.route("/request/<int:rid>/done", methods=["POST"])
@login_required()
def request_done(rid):
    u=current_user(); r=db().execute("SELECT * FROM requests WHERE id=?", (rid,)).fetchone() or abort(404)
    if u["id"]==r["user_id"]:
        db().execute("UPDATE requests SET beneficiary_done=1, updated_at=CURRENT_TIMESTAMP WHERE id=?", (rid,))
    elif u["role"] in PROVIDER_ROLES:
        ok=db().execute("SELECT 1 FROM offers WHERE request_id=? AND provider_id=? AND status='accepted'", (rid,u["id"])).fetchone()
        if not ok: abort(403)
        db().execute("UPDATE requests SET provider_done=1, updated_at=CURRENT_TIMESTAMP WHERE id=?", (rid,))
    else: abort(403)
    r2=db().execute("SELECT * FROM requests WHERE id=?", (rid,)).fetchone()
    if r2["beneficiary_done"] and r2["provider_done"]:
        db().execute("UPDATE requests SET status='closed', closed_at=COALESCE(closed_at,CURRENT_TIMESTAMP), completed_at=COALESCE(completed_at,CURRENT_TIMESTAMP), updated_at=CURRENT_TIMESTAMP WHERE id=?", (rid,))
    elif r2["status"]=="open":
        db().execute("UPDATE requests SET status='in_progress', updated_at=CURRENT_TIMESTAMP WHERE id=?", (rid,))
    db().commit(); return redirect(url_for("dashboard"))

@app.route("/request/<int:rid>/close", methods=["POST"])
@login_required("beneficiary")
def close_request(rid):
    return request_done(rid)

@app.route("/api/dashboard_version")
@login_required()
def dashboard_version():
    u=current_user()
    if u["role"]=="beneficiary":
        row=db().execute("SELECT MAX(v) AS v FROM (SELECT COALESCE(MAX(updated_at),'') v FROM requests WHERE user_id=? UNION ALL SELECT COALESCE(MAX(o.updated_at),'') v FROM offers o JOIN requests r ON r.id=o.request_id WHERE r.user_id=?)", (u["id"],u["id"])).fetchone()
    else:
        cats=ROLE_CATEGORIES.get(u["role"],[])
        ph=','.join('?'*len(cats)) or "NULL"
        args=tuple(cats)+(u["id"],)
        row=db().execute(f"SELECT MAX(v) AS v FROM (SELECT COALESCE(MAX(r.updated_at),'') v FROM requests r WHERE r.category IN ({ph}) UNION ALL SELECT COALESCE(MAX(o.updated_at),'') v FROM offers o WHERE o.provider_id=?)", args).fetchone()
    return jsonify({"version":row["v"] or ""})

# ---------- community stories / experience blog ----------
def _duration_minutes(started, ended):
    if not started or not ended: return None
    try:
        a=datetime.strptime(started[:19], "%Y-%m-%d %H:%M:%S")
        b=datetime.strptime(ended[:19], "%Y-%m-%d %H:%M:%S")
        return max(0, int((b-a).total_seconds()//60))
    except (TypeError,ValueError): return None

def _duration_label(minutes):
    if minutes is None: return ""
    days, rem=divmod(minutes,1440); hours, mins=divmod(rem,60); parts=[]
    if days: parts.append(f"{days} day{'s' if days!=1 else ''}")
    if hours: parts.append(f"{hours} hour{'s' if hours!=1 else ''}")
    if mins or not parts: parts.append(f"{mins} min")
    return " ".join(parts)

@app.route("/stories")
def stories():
    rows=db().execute("SELECT s.*,u.display_name AS alias FROM stories s JOIN users u ON u.id=s.user_id WHERE s.status='published' ORDER BY s.created DESC").fetchall()
    return render_template("stories.html", stories=rows, duration_label=_duration_label)

@app.route("/stories/new", methods=["GET","POST"])
@login_required("beneficiary")
def story_new():
    u=current_user()
    closed=db().execute("SELECT id,title,category,created,closed_at FROM requests WHERE user_id=? AND status='closed' ORDER BY closed_at DESC",(u["id"],)).fetchall()
    if request.method=="POST":
        f=request.form
        title=f.get("title","").strip()[:160]; body=f.get("body","").strip()[:8000]; category=f.get("category","support")
        if not title or not body or category not in CATEGORIES: abort(400)
        raw=f.get("request_id","").strip(); rid=int(raw) if raw.isdigit() else None; duration=None
        if rid:
            r=db().execute("SELECT * FROM requests WHERE id=? AND user_id=? AND status='closed'",(rid,u["id"])).fetchone() or abort(403)
            category=r["category"]; duration=_duration_minutes(r["created"],r["closed_at"])
        db().execute("INSERT INTO stories(user_id,request_id,category,title,body,what_helped,outcome,duration_minutes,status) VALUES(?,?,?,?,?,?,?,?,?)",
                     (u["id"],rid,category,title,body,f.get("what_helped","").strip()[:3000],f.get("outcome","").strip()[:3000],duration,"published"))
        db().commit(); flash("Your experience has been shared.","ok")
        return redirect(url_for("stories"))
    return render_template("story_new.html",closed=closed)

# ---------- surplus food ----------
@app.route("/food")
@login_required()
def food():
    state = clean_state(request.args.get("state", ""))
    rows = db().execute(
        "SELECT f.*, u.org, u.display_name FROM food f JOIN users u ON u.id=f.restaurant_id"
        " WHERE (?='' OR f.state=?) ORDER BY (f.status='available') DESC, f.created DESC LIMIT 100", (state, state)).fetchall()
    return render_template("food.html", rows=rows, state=state)

@app.route("/food/new", methods=["GET", "POST"])
@login_required("restaurant")
def food_new():
    u = current_user()
    if request.method == "POST":
        if not u["verified"]:
            flash("Your account is awaiting verification.", "error")
            return redirect(url_for("food"))
        f = request.form
        db().execute("INSERT INTO food(restaurant_id,description,quantity,city,pickup_address,pickup_by,state)"
                     " VALUES(?,?,?,?,?,?,?)",
                     (u["id"], f["description"].strip(), f.get("quantity", ""), f.get("city", u["city"]),
                      f.get("pickup_address", ""), f.get("pickup_by", ""), clean_state(f.get("state"))))
        db().commit(); flash("Food listing posted. Thank you!", "ok")
        return redirect(url_for("food"))
    return render_template("food_new.html")

@app.route("/food/<int:fid>/claim", methods=["POST"])
@login_required("beneficiary", "ngo")
def food_claim(fid):
    db().execute("UPDATE food SET status='claimed', claimed_by=? WHERE id=? AND status='available'",
                 (current_user()["id"], fid))
    db().commit(); flash("Claimed. Please collect before the pickup time.", "ok")
    return redirect(url_for("food"))

@app.route("/food/<int:fid>/done", methods=["POST"])
@login_required("restaurant")
def food_done(fid):
    db().execute("UPDATE food SET status='collected' WHERE id=? AND restaurant_id=?", (fid, current_user()["id"]))
    db().commit()
    return redirect(url_for("food"))

# ---------- live statistics (aggregate only, no personal data) ----------
def get_stats(state=""):
    d = db()
    sc, sa = (" AND state=?", (state,)) if state else ("", ())
    one = lambda q, a=(): d.execute(q + sc, tuple(a) + sa).fetchone()[0]
    st = {"open": one("SELECT COUNT(*) FROM requests WHERE status='open'"),
          "progress": one("SELECT COUNT(*) FROM requests WHERE status='in_progress'"),
          "closed": one("SELECT COUNT(*) FROM requests WHERE status='closed'"),
          "jobs": one("SELECT COUNT(*) FROM jobs WHERE status='open'"),
          "food": one("SELECT COUNT(*) FROM food WHERE status='available'"),
          "helpers": one("SELECT COUNT(*) FROM users WHERE verified=1 AND role NOT IN ('beneficiary','admin')"),
          "cat": {}}
    total = st["open"] + st["progress"] + st["closed"]
    st["rate"] = round(100 * st["closed"] / total) if total else 0
    for c in CATEGORIES:
        st["cat"][c] = {k: one("SELECT COUNT(*) FROM requests WHERE category=? AND status=?", (c, v))
                        for k, v in (("open", "open"), ("progress", "in_progress"), ("closed", "closed"))}
    return st

def state_table():
    rows = db().execute("SELECT state, SUM(status='open') o, SUM(status='in_progress') p, SUM(status='closed') c"
                        " FROM requests WHERE state IS NOT NULL AND state!='' GROUP BY state ORDER BY (o+p+c) DESC").fetchall()
    return [{"state": r["state"], "open": r["o"], "progress": r["p"], "closed": r["c"]} for r in rows]

@app.route("/api/states")
def api_states():
    return jsonify(state_table())

@app.route("/api/stats")
def api_stats():
    return jsonify(get_stats(clean_state(request.args.get("state", ""))))

@app.route("/live")
def live():
    state = clean_state(request.args.get("state", ""))
    return render_template("live.html", stats=get_stats(state), state=state, table=state_table())

@app.route("/lang/<code>")
def set_lang(code):
    if code in LANGS:
        session["lang"] = code
    ref = request.referrer or ""
    return redirect(ref if ref.startswith(request.host_url) else url_for("index"))

# ---------- chat + calls for an offer ----------
def offer_access(oid):
    o = db().execute("SELECT o.*, r.user_id AS owner_id, r.title, r.contact_phone, r.contact_note, r.category,"
                     " p.display_name AS pname, p.org AS porg, p.phone AS pphone, b.display_name AS alias"
                     " FROM offers o JOIN requests r ON r.id=o.request_id JOIN users p ON p.id=o.provider_id"
                     " JOIN users b ON b.id=r.user_id WHERE o.id=?", (oid,)).fetchone() or abort(404)
    u = current_user()
    if u["id"] not in (o["owner_id"], o["provider_id"]):
        abort(403)
    return o, u

@app.route("/offer/<int:oid>")
@login_required()
def chat(oid):
    o, u = offer_access(oid)
    return render_template("chat.html", o=o, is_owner=u["id"] == o["owner_id"], room=video_url(oid))

@app.route("/offer/<int:oid>/msgs")
@login_required()
def chat_msgs(oid):
    o, u = offer_access(oid)
    rows = db().execute("SELECT sender_id, body, created FROM messages WHERE offer_id=? ORDER BY id", (oid,)).fetchall()
    return jsonify([{"mine": r["sender_id"] == u["id"], "body": r["body"], "time": r["created"][11:16]} for r in rows])

@app.route("/offer/<int:oid>/msg", methods=["POST"])
@login_required()
def chat_send(oid):
    o, u = offer_access(oid)
    body = request.form.get("body", "").strip()[:1000]
    if body and o["status"] != "declined":
        db().execute("INSERT INTO messages(offer_id,sender_id,body) VALUES(?,?,?)", (oid, u["id"], body))
        db().commit()
    return ("", 204)

# ---------- jobs ----------
@app.route("/jobs")
def jobs():
    city = request.args.get("city", "").strip().lower()
    state = clean_state(request.args.get("state", ""))
    rows = db().execute(
        "SELECT j.*, u.org, u.display_name, u.role FROM jobs j JOIN users u ON u.id=j.poster_id"
        " WHERE j.status='open' AND lower(coalesce(j.city,'')) LIKE ? AND (?='' OR j.state=?)"
        " ORDER BY j.created DESC", ("%" + city + "%", state, state)).fetchall()
    return render_template("jobs.html", rows=rows, city=city, state=state)

@app.route("/jobs/new", methods=["GET", "POST"])
@login_required(*JOB_ROLES)
def job_new():
    u = current_user()
    if request.method == "POST":
        if not u["verified"]:
            flash("Your account is awaiting verification.", "error")
            return redirect(url_for("jobs"))
        f = request.form
        if not f.get("title", "").strip():
            abort(400)
        db().execute("INSERT INTO jobs(poster_id,title,description,city,job_type,pay,phone,state) VALUES(?,?,?,?,?,?,?,?)",
                     (u["id"], f["title"].strip(), f.get("description", "").strip(), f.get("city", u["city"]),
                      f.get("job_type", ""), f.get("pay", ""), f.get("phone", u["phone"]), clean_state(f.get("state"))))
        db().commit(); flash("Job posted.", "ok")
        return redirect(url_for("jobs"))
    return render_template("job_new.html")

@app.route("/jobs/<int:jid>", methods=["GET", "POST"])
def job_view(jid):
    j = db().execute("SELECT j.*, u.org, u.display_name FROM jobs j JOIN users u ON u.id=j.poster_id WHERE j.id=?",
                     (jid,)).fetchone() or abort(404)
    u = current_user()
    if request.method == "POST":
        if not u or u["role"] != "beneficiary":
            abort(403)
        try:
            db().execute("INSERT INTO applications(job_id,user_id,message,contact) VALUES(?,?,?,?)",
                         (jid, u["id"], request.form.get("message", "").strip()[:500], request.form.get("contact", "").strip()[:200]))
            db().commit(); flash("Application sent.", "ok")
        except sqlite3.IntegrityError:
            flash("You already applied.", "error")
        return redirect(url_for("job_view", jid=jid))
    applied = bool(u and db().execute("SELECT 1 FROM applications WHERE job_id=? AND user_id=?", (jid, u["id"])).fetchone())
    apps = []
    if u and u["id"] == j["poster_id"]:
        apps = db().execute("SELECT a.*, b.display_name AS alias FROM applications a JOIN users b ON b.id=a.user_id"
                            " WHERE a.job_id=? ORDER BY a.created DESC", (jid,)).fetchall()
    return render_template("job_view.html", j=j, applied=applied, apps=apps)

@app.route("/jobs/<int:jid>/close", methods=["POST"])
@login_required(*JOB_ROLES)
def job_close(jid):
    db().execute("UPDATE jobs SET status='closed' WHERE id=? AND poster_id=?", (jid, current_user()["id"]))
    db().commit()
    return redirect(url_for("jobs"))

# ---------- admin ----------
@app.route("/admin", methods=["GET", "POST"])
@login_required("admin")
def admin():
    if request.method=="POST":
        action=request.form.get("action")
        if action in ("verify","unverify"):
            db().execute("UPDATE users SET verified=? WHERE id=? AND role!='admin'", (1 if action=="verify" else 0, request.form["uid"]))
        elif action=="remove_request":
            rid=request.form["rid"]; db().execute("DELETE FROM messages WHERE offer_id IN (SELECT id FROM offers WHERE request_id=?)",(rid,)); db().execute("DELETE FROM offers WHERE request_id=?",(rid,)); db().execute("DELETE FROM stories WHERE request_id=?",(rid,)); db().execute("DELETE FROM requests WHERE id=?",(rid,))
        elif action=="remove_story": db().execute("DELETE FROM stories WHERE id=?",(request.form["sid"],))
        elif action=="remove_user":
            uid=int(request.form["uid"])
            if uid!=current_user()["id"]:
                db().execute("DELETE FROM messages WHERE sender_id=? OR offer_id IN (SELECT id FROM offers WHERE provider_id=?)",(uid,uid))
                db().execute("DELETE FROM offers WHERE provider_id=? OR request_id IN (SELECT id FROM requests WHERE user_id=?)",(uid,uid))
                db().execute("DELETE FROM stories WHERE user_id=? OR request_id IN (SELECT id FROM requests WHERE user_id=?)",(uid,uid))
                db().execute("DELETE FROM applications WHERE user_id=? OR job_id IN (SELECT id FROM jobs WHERE poster_id=?)",(uid,uid))
                db().execute("DELETE FROM jobs WHERE poster_id=?",(uid,)); db().execute("DELETE FROM food WHERE restaurant_id=? OR claimed_by=?",(uid,uid)); db().execute("DELETE FROM requests WHERE user_id=?",(uid,)); db().execute("DELETE FROM users WHERE id=? AND role!='admin'",(uid,))
        db().commit()
    users=db().execute("SELECT * FROM users WHERE role!='admin' ORDER BY role,created DESC").fetchall()
    requests=db().execute("SELECT r.id,r.title,r.status,r.created,u.display_name AS alias FROM requests r JOIN users u ON u.id=r.user_id ORDER BY r.created DESC LIMIT 200").fetchall()
    stories=db().execute("SELECT s.id,s.title,s.status,s.created,u.display_name AS alias FROM stories s JOIN users u ON u.id=s.user_id ORDER BY s.created DESC LIMIT 200").fetchall()
    admin_stats={"Beneficiaries":db().execute("SELECT COUNT(*) FROM users WHERE role='beneficiary'").fetchone()[0],"Open requests":db().execute("SELECT COUNT(*) FROM requests WHERE status='open'").fetchone()[0],"Food listings":db().execute("SELECT COUNT(*) FROM food").fetchone()[0],"Stories":db().execute("SELECT COUNT(*) FROM stories").fetchone()[0]}
    return render_template("admin.html",users=users,requests=requests,stories=stories,stats=admin_stats)

init_db()
if __name__ == "__main__":
    port = int(os.environ.get("PORT", "5000"))
    app.run(host="0.0.0.0", port=port, debug=os.environ.get("FLASK_DEBUG") == "1")
