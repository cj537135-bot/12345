# SAHARA — Render-ready package

## IMPORTANT: GitHub folder structure
Upload the CONTENTS of this folder to the ROOT of your GitHub repository. Do not upload the outer folder itself.

The GitHub repository must directly contain:

app.py
requirements.txt
Dockerfile
render.yaml
i18n.py
templates/
static/

And these files must exist:

templates/index.html
templates/base.html

## Render
1. Push all files/folders above to the repository root.
2. In Render choose New -> Blueprint and select the repository, OR create a Docker Web Service and use the Dockerfile.
3. Set ADMIN_PASSWORD in Environment to a strong password.
4. Deploy.
5. Open the generated onrender.com URL.
6. Test /healthz first; it should return {"status":"ok"}.

## If you see TemplateNotFound: index.html
That means templates/index.html was not uploaded to the GitHub repository root. Re-upload the complete templates/ folder. The Dockerfile now intentionally fails the build if index.html or base.html is missing, so this mistake is caught before the service is marked live.

## Database note
This package uses SQLite for a simple free demo deployment. On Render's free service the local filesystem is ephemeral, so database data should not be treated as permanent production storage. For permanent data, migrate the database layer to a managed persistent database.
