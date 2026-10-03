"""UI translations. Add a language by adding a block below and an entry in LANGS.
Missing keys fall back to English. Have a native speaker review sensitive wording."""
LANGS = {"en": "English", "hi": "हिन्दी", "gu": "ગુજરાતી", "mr": "मराठी", "bn": "বাংলা", "ta": "தமிழ்",
         "te": "తెలుగు", "kn": "ಕನ್ನಡ", "ml": "മലയാളം", "pa": "ਪੰਜਾਬੀ", "or": "ଓଡ଼ିଆ", "ur": "اردو"}
RTL = {"ur"}
KEYS = """nav_food nav_jobs nav_live nav_dash nav_login nav_register nav_logout quick_exit hero_title hero_text
need_help want_help open_problems in_progress solved open_jobs food_avail helpers c_medical c_legal c_education
c_skill c_livelihood c_food c_support ask_help post_request my_requests offer_help send_offer accept decline
mark_solved call video_call messages send chat_calls jobs apply applied post_job list_food claim emergency
f_username f_password f_alias f_city f_title f_details f_phone f_message f_urgency urgent normal s_open
live_title by_category resolved_rate privacy_line no_items""".split()

def _mk(text):
    vals = [v.strip() for v in text.strip().split("\n")]
    assert len(vals) == len(KEYS), (len(vals), len(KEYS))
    return dict(zip(KEYS, vals))

EN = _mk("""Food support
Jobs
Live status
Dashboard
Login
Register
Logout
Quick exit
Safe, private support for sex workers
Ask for medical, legal, education, skill, work or food help. Verified helpers will respond.
I need help
I want to help
Open problems
In progress
Solved
Open jobs
Food available
Verified helpers
Medical help
Legal help
Education
Skill training
Work / income
Food
Counselling / shelter
Ask for help
Post request
My requests
Offer help
Send offer
Accept
Decline
Mark as solved
Call
Video call
Messages
Send
Chat & calls
Job openings
Apply
Applied
Post a job
List surplus food
Claim
Emergency
Username
Password
Name / alias
City
Title
Details
Phone
Message
Urgency
Urgent
Normal
Open
Live status (updates automatically)
By category
Resolved
Your privacy comes first. Contact details are shared only after you accept help.
Nothing here yet.""")

HI = _mk("""भोजन सहायता
नौकरियां
लाइव स्थिति
डैशबोर्ड
लॉगिन
रजिस्टर करें
लॉगआउट
तुरंत बाहर निकलें
यौनकर्मियों के लिए सुरक्षित और निजी सहायता
चिकित्सा, कानूनी, शिक्षा, कौशल, काम या भोजन की मदद मांगें। सत्यापित सहायक आपकी मदद करेंगे।
मुझे मदद चाहिए
मैं मदद करना चाहता/चाहती हूँ
खुली समस्याएँ
प्रगति में
हल हुई
खुली नौकरियां
उपलब्ध भोजन
सत्यापित सहायक
चिकित्सा सहायता
कानूनी सहायता
शिक्षा
कौशल प्रशिक्षण
काम / आमदनी
भोजन
परामर्श / आश्रय
मदद मांगें
अनुरोध भेजें
मेरे अनुरोध
मदद की पेशकश करें
पेशकश भेजें
स्वीकार करें
अस्वीकार करें
हल हुआ चिह्नित करें
फ़ोन करें
वीडियो कॉल
संदेश
भेजें
चैट और कॉल
नौकरी के अवसर
आवेदन करें
आवेदन किया
नौकरी पोस्ट करें
बचा हुआ भोजन दें
प्राप्त करें
आपातकाल
उपयोगकर्ता नाम
पासवर्ड
नाम / उपनाम
शहर
शीर्षक
विवरण
फ़ोन
संदेश
तात्कालिकता
अत्यावश्यक
सामान्य
खुला
लाइव स्थिति (अपने आप अपडेट होती है)
श्रेणी अनुसार
हल
आपकी निजता सबसे पहले। संपर्क विवरण तभी साझा होते हैं जब आप मदद स्वीकार करें।
अभी कुछ नहीं है।""")

GU = _mk("""ભોજન સહાય
નોકરીઓ
લાઇવ સ્થિતિ
ડેશબોર્ડ
લૉગિન
નોંધણી કરો
લૉગઆઉટ
તરત બહાર નીકળો
સેક્સ વર્કર્સ માટે સુરક્ષિત અને ખાનગી સહાય
તબીબી, કાનૂની, શિક્ષણ, કૌશલ્ય, કામ કે ભોજનની મદદ માગો. ચકાસાયેલા સહાયકો તમને જવાબ આપશે.
મને મદદ જોઈએ છે
હું મદદ કરવા માગું છું
ખુલ્લી સમસ્યાઓ
પ્રગતિમાં
ઉકેલાયેલી
ખુલ્લી નોકરીઓ
ઉપલબ્ધ ભોજન
ચકાસાયેલા સહાયકો
તબીબી સહાય
કાનૂની સહાય
શિક્ષણ
કૌશલ્ય તાલીમ
કામ / આવક
ભોજન
કાઉન્સેલિંગ / આશ્રય
મદદ માગો
વિનંતી મોકલો
મારી વિનંતીઓ
મદદ ઓફર કરો
ઓફર મોકલો
સ્વીકારો
નકારો
ઉકેલાયેલ તરીકે ચિહ્નિત કરો
ફોન કરો
વિડિઓ કૉલ
સંદેશાઓ
મોકલો
ચેટ અને કૉલ
નોકરીની તકો
અરજી કરો
અરજી કરી
નોકરી પોસ્ટ કરો
વધેલું ભોજન આપો
મેળવો
કટોકટી
વપરાશકર્તા નામ
પાસવર્ડ
નામ / ઉપનામ
શહેર
શીર્ષક
વિગતો
ફોન
સંદેશ
તાત્કાલિકતા
તાત્કાલિક
સામાન્ય
ખુલ્લું
લાઇવ સ્થિતિ (આપોઆપ અપડેટ થાય છે)
શ્રેણી મુજબ
ઉકેલાયેલ
તમારી ગોપનીયતા સૌથી પહેલા. તમે મદદ સ્વીકારો પછી જ સંપર્ક વિગતો શેર થાય છે.
હજુ કંઈ નથી.""")

MR = _mk("""अन्न मदत
नोकऱ्या
थेट स्थिती
डॅशबोर्ड
लॉगिन
नोंदणी करा
लॉगआउट
त्वरित बाहेर पडा
सेक्स वर्कर्ससाठी सुरक्षित आणि खाजगी मदत
वैद्यकीय, कायदेशीर, शिक्षण, कौशल्य, काम किंवा अन्नाची मदत मागा. पडताळणी केलेले सहाय्यक तुम्हाला प्रतिसाद देतील.
मला मदत हवी आहे
मला मदत करायची आहे
खुल्या समस्या
प्रगतीत
सोडवलेल्या
खुल्या नोकऱ्या
उपलब्ध अन्न
पडताळलेले सहाय्यक
वैद्यकीय मदत
कायदेशीर मदत
शिक्षण
कौशल्य प्रशिक्षण
काम / उत्पन्न
अन्न
समुपदेशन / निवारा
मदत मागा
विनंती पाठवा
माझ्या विनंत्या
मदतीची ऑफर द्या
ऑफर पाठवा
स्वीकारा
नाकारा
सोडवले म्हणून नोंदवा
फोन करा
व्हिडिओ कॉल
संदेश
पाठवा
चॅट आणि कॉल
नोकरीच्या संधी
अर्ज करा
अर्ज केला
नोकरी पोस्ट करा
उरलेले अन्न द्या
मिळवा
आणीबाणी
वापरकर्तानाव
पासवर्ड
नाव / टोपणनाव
शहर
शीर्षक
तपशील
फोन
संदेश
तातडी
तातडीचे
सामान्य
खुले
थेट स्थिती (आपोआप अपडेट होते)
श्रेणीनुसार
सोडवलेले
तुमची गोपनीयता प्रथम. तुम्ही मदत स्वीकारल्यानंतरच संपर्क तपशील शेअर केले जातात.
अजून काही नाही.""")

BN = _mk("""খাদ্য সহায়তা
চাকরি
লাইভ অবস্থা
ড্যাশবোর্ড
লগইন
নিবন্ধন করুন
লগআউট
দ্রুত বেরিয়ে যান
যৌনকর্মীদের জন্য নিরাপদ ও গোপনীয় সহায়তা
চিকিৎসা, আইনি, শিক্ষা, দক্ষতা, কাজ বা খাবারের সাহায্য চান। যাচাইকৃত সহায়করা সাড়া দেবেন।
আমার সাহায্য দরকার
আমি সাহায্য করতে চাই
খোলা সমস্যা
চলমান
সমাধান হয়েছে
খোলা চাকরি
উপলব্ধ খাবার
যাচাইকৃত সহায়ক
চিকিৎসা সহায়তা
আইনি সহায়তা
শিক্ষা
দক্ষতা প্রশিক্ষণ
কাজ / আয়
খাবার
কাউন্সেলিং / আশ্রয়
সাহায্য চান
অনুরোধ পাঠান
আমার অনুরোধ
সাহায্যের প্রস্তাব দিন
প্রস্তাব পাঠান
গ্রহণ করুন
প্রত্যাখ্যান করুন
সমাধান হয়েছে চিহ্নিত করুন
ফোন করুন
ভিডিও কল
বার্তা
পাঠান
চ্যাট ও কল
চাকরির সুযোগ
আবেদন করুন
আবেদন করা হয়েছে
চাকরি পোস্ট করুন
উদ্বৃত্ত খাবার দিন
গ্রহণ
জরুরি
ব্যবহারকারীর নাম
পাসওয়ার্ড
নাম / ছদ্মনাম
শহর
শিরোনাম
বিবরণ
ফোন
বার্তা
জরুরিত্ব
জরুরি
সাধারণ
খোলা
লাইভ অবস্থা (স্বয়ংক্রিয়ভাবে আপডেট হয়)
বিভাগ অনুযায়ী
সমাধান হয়েছে
আপনার গোপনীয়তা সবার আগে। আপনি সাহায্য গ্রহণ করলে তবেই যোগাযোগের তথ্য শেয়ার হয়।
এখনও কিছু নেই।""")

TA = _mk("""உணவு உதவி
வேலைகள்
நேரடி நிலை
டாஷ்போர்டு
உள்நுழை
பதிவு செய்
வெளியேறு
உடனே வெளியேறு
பாலியல் தொழிலாளர்களுக்கான பாதுகாப்பான, தனிப்பட்ட உதவி
மருத்துவம், சட்டம், கல்வி, திறன், வேலை அல்லது உணவு உதவி கேளுங்கள். சரிபார்க்கப்பட்ட உதவியாளர்கள் பதிலளிப்பார்கள்.
எனக்கு உதவி தேவை
நான் உதவ விரும்புகிறேன்
திறந்த பிரச்சனைகள்
நடைபெறுகிறது
தீர்க்கப்பட்டது
திறந்த வேலைகள்
கிடைக்கும் உணவு
சரிபார்க்கப்பட்ட உதவியாளர்கள்
மருத்துவ உதவி
சட்ட உதவி
கல்வி
திறன் பயிற்சி
வேலை / வருமானம்
உணவு
ஆலோசனை / தங்குமிடம்
உதவி கேளுங்கள்
கோரிக்கையை அனுப்பு
என் கோரிக்கைகள்
உதவி வழங்கு
வழங்கலை அனுப்பு
ஏற்றுக்கொள்
நிராகரி
தீர்க்கப்பட்டதாகக் குறி
அழை
வீடியோ அழைப்பு
செய்திகள்
அனுப்பு
அரட்டை & அழைப்புகள்
வேலை வாய்ப்புகள்
விண்ணப்பி
விண்ணப்பித்தாயிற்று
வேலையை இடுகையிடு
மீதமுள்ள உணவை வழங்கு
பெறு
அவசரம்
பயனர் பெயர்
கடவுச்சொல்
பெயர் / புனைப்பெயர்
நகரம்
தலைப்பு
விவரங்கள்
தொலைபேசி
செய்தி
அவசரநிலை
மிக அவசரம்
சாதாரணம்
திறந்தது
நேரடி நிலை (தானாகப் புதுப்பிக்கப்படும்)
வகை வாரியாக
தீர்க்கப்பட்டது
உங்கள் தனியுரிமை முதலில். நீங்கள் உதவியை ஏற்ற பின்னரே தொடர்பு விவரங்கள் பகிரப்படும்.
இன்னும் எதுவும் இல்லை.""")

TE = _mk("""ఆహార సహాయం
ఉద్యోగాలు
ప్రత్యక్ష స్థితి
డాష్‌బోర్డ్
లాగిన్
నమోదు చేయండి
లాగ్ అవుట్
త్వరగా నిష్క్రమించు
సెక్స్ వర్కర్ల కోసం సురక్షిత, గోప్యమైన సహాయం
వైద్య, న్యాయ, విద్య, నైపుణ్యం, పని లేదా ఆహార సహాయం అడగండి. ధృవీకరించబడిన సహాయకులు స్పందిస్తారు.
నాకు సహాయం కావాలి
నేను సహాయం చేయాలనుకుంటున్నాను
తెరిచిన సమస్యలు
కొనసాగుతున్నవి
పరిష్కరించబడినవి
తెరిచిన ఉద్యోగాలు
అందుబాటులో ఉన్న ఆహారం
ధృవీకరించబడిన సహాయకులు
వైద్య సహాయం
న్యాయ సహాయం
విద్య
నైపుణ్య శిక్షణ
పని / ఆదాయం
ఆహారం
కౌన్సెలింగ్ / ఆశ్రయం
సహాయం అడగండి
అభ్యర్థన పంపండి
నా అభ్యర్థనలు
సహాయం అందించండి
ఆఫర్ పంపండి
అంగీకరించు
తిరస్కరించు
పరిష్కరించబడినదిగా గుర్తించు
కాల్ చేయండి
వీడియో కాల్
సందేశాలు
పంపు
చాట్ & కాల్స్
ఉద్యోగ అవకాశాలు
దరఖాస్తు చేయండి
దరఖాస్తు చేశారు
ఉద్యోగం పోస్ట్ చేయండి
మిగిలిన ఆహారం ఇవ్వండి
పొందండి
అత్యవసరం
వినియోగదారు పేరు
పాస్‌వర్డ్
పేరు / మారుపేరు
నగరం
శీర్షిక
వివరాలు
ఫోన్
సందేశం
అత్యవసరత
అత్యవసరం
సాధారణం
తెరిచి ఉంది
ప్రత్యక్ష స్థితి (ఆటోమేటిక్‌గా అప్‌డేట్ అవుతుంది)
వర్గం వారీగా
పరిష్కరించబడింది
మీ గోప్యతే ముందు. మీరు సహాయాన్ని అంగీకరించిన తర్వాతే సంప్రదింపు వివరాలు పంచబడతాయి.
ఇంకా ఏమీ లేదు.""")

KN = _mk("""ಆಹಾರ ಸಹಾಯ
ಉದ್ಯೋಗಗಳು
ನೇರ ಸ್ಥಿತಿ
ಡ್ಯಾಶ್‌ಬೋರ್ಡ್
ಲಾಗಿನ್
ನೋಂದಣಿ ಮಾಡಿ
ಲಾಗ್ ಔಟ್
ತಕ್ಷಣ ನಿರ್ಗಮಿಸಿ
ಲೈಂಗಿಕ ಕಾರ್ಯಕರ್ತರಿಗೆ ಸುರಕ್ಷಿತ, ಖಾಸಗಿ ಸಹಾಯ
ವೈದ್ಯಕೀಯ, ಕಾನೂನು, ಶಿಕ್ಷಣ, ಕೌಶಲ್ಯ, ಕೆಲಸ ಅಥವಾ ಆಹಾರದ ಸಹಾಯ ಕೇಳಿ. ಪರಿಶೀಲಿಸಿದ ಸಹಾಯಕರು ಪ್ರತಿಕ್ರಿಯಿಸುತ್ತಾರೆ.
ನನಗೆ ಸಹಾಯ ಬೇಕು
ನಾನು ಸಹಾಯ ಮಾಡಲು ಬಯಸುತ್ತೇನೆ
ತೆರೆದ ಸಮಸ್ಯೆಗಳು
ಪ್ರಗತಿಯಲ್ಲಿ
ಪರಿಹರಿಸಲಾಗಿದೆ
ತೆರೆದ ಉದ್ಯೋಗಗಳು
ಲಭ್ಯವಿರುವ ಆಹಾರ
ಪರಿಶೀಲಿಸಿದ ಸಹಾಯಕರು
ವೈದ್ಯಕೀಯ ಸಹಾಯ
ಕಾನೂನು ಸಹಾಯ
ಶಿಕ್ಷಣ
ಕೌಶಲ್ಯ ತರಬೇತಿ
ಕೆಲಸ / ಆದಾಯ
ಆಹಾರ
ಸಮಾಲೋಚನೆ / ಆಶ್ರಯ
ಸಹಾಯ ಕೇಳಿ
ವಿನಂತಿ ಕಳುಹಿಸಿ
ನನ್ನ ವಿನಂತಿಗಳು
ಸಹಾಯ ನೀಡಿ
ಕೊಡುಗೆ ಕಳುಹಿಸಿ
ಒಪ್ಪಿಕೊಳ್ಳಿ
ತಿರಸ್ಕರಿಸಿ
ಪರಿಹರಿಸಲಾಗಿದೆ ಎಂದು ಗುರುತಿಸಿ
ಕರೆ ಮಾಡಿ
ವೀಡಿಯೊ ಕರೆ
ಸಂದೇಶಗಳು
ಕಳುಹಿಸಿ
ಚಾಟ್ ಮತ್ತು ಕರೆಗಳು
ಉದ್ಯೋಗ ಅವಕಾಶಗಳು
ಅರ್ಜಿ ಸಲ್ಲಿಸಿ
ಅರ್ಜಿ ಸಲ್ಲಿಸಲಾಗಿದೆ
ಉದ್ಯೋಗ ಪೋಸ್ಟ್ ಮಾಡಿ
ಉಳಿದ ಆಹಾರ ನೀಡಿ
ಪಡೆಯಿರಿ
ತುರ್ತು
ಬಳಕೆದಾರ ಹೆಸರು
ಪಾಸ್‌ವರ್ಡ್
ಹೆಸರು / ಅಡ್ಡಹೆಸರು
ನಗರ
ಶೀರ್ಷಿಕೆ
ವಿವರಗಳು
ಫೋನ್
ಸಂದೇಶ
ತುರ್ತು ಮಟ್ಟ
ತುರ್ತು
ಸಾಮಾನ್ಯ
ತೆರೆದಿದೆ
ನೇರ ಸ್ಥಿತಿ (ತಾನಾಗಿ ನವೀಕರಿಸುತ್ತದೆ)
ವರ್ಗದ ಪ್ರಕಾರ
ಪರಿಹರಿಸಲಾಗಿದೆ
ನಿಮ್ಮ ಗೌಪ್ಯತೆ ಮೊದಲು. ನೀವು ಸಹಾಯ ಒಪ್ಪಿಕೊಂಡ ನಂತರವೇ ಸಂಪರ್ಕ ವಿವರಗಳನ್ನು ಹಂಚಲಾಗುತ್ತದೆ.
ಇನ್ನೂ ಏನೂ ಇಲ್ಲ.""")

ML = _mk("""ഭക്ഷണ സഹായം
ജോലികൾ
തത്സമയ നില
ഡാഷ്ബോർഡ്
ലോഗിൻ
രജിസ്റ്റർ ചെയ്യുക
ലോഗ്ഔട്ട്
പെട്ടെന്ന് പുറത്തുകടക്കുക
ലൈംഗിക തൊഴിലാളികൾക്ക് സുരക്ഷിതവും സ്വകാര്യവുമായ സഹായം
വൈദ്യ, നിയമ, വിദ്യാഭ്യാസ, നൈപുണ്യ, തൊഴിൽ അല്ലെങ്കിൽ ഭക്ഷണ സഹായം ചോദിക്കൂ. പരിശോധിച്ച സഹായികൾ പ്രതികരിക്കും.
എനിക്ക് സഹായം വേണം
എനിക്ക് സഹായിക്കണം
തുറന്ന പ്രശ്നങ്ങൾ
പുരോഗമിക്കുന്നു
പരിഹരിച്ചു
തുറന്ന ജോലികൾ
ലഭ്യമായ ഭക്ഷണം
പരിശോധിച്ച സഹായികൾ
വൈദ്യ സഹായം
നിയമ സഹായം
വിദ്യാഭ്യാസം
നൈപുണ്യ പരിശീലനം
ജോലി / വരുമാനം
ഭക്ഷണം
കൗൺസിലിംഗ് / അഭയം
സഹായം ചോദിക്കൂ
അഭ്യർത്ഥന അയയ്ക്കുക
എന്റെ അഭ്യർത്ഥനകൾ
സഹായം വാഗ്ദാനം ചെയ്യുക
വാഗ്ദാനം അയയ്ക്കുക
സ്വീകരിക്കുക
നിരസിക്കുക
പരിഹരിച്ചതായി അടയാളപ്പെടുത്തുക
വിളിക്കുക
വീഡിയോ കോൾ
സന്ദേശങ്ങൾ
അയയ്ക്കുക
ചാറ്റും കോളുകളും
തൊഴിൽ അവസരങ്ങൾ
അപേക്ഷിക്കുക
അപേക്ഷിച്ചു
ജോലി പോസ്റ്റ് ചെയ്യുക
ബാക്കിവന്ന ഭക്ഷണം നൽകുക
സ്വീകരിക്കുക
അടിയന്തരം
ഉപയോക്തൃനാമം
പാസ്‌വേഡ്
പേര് / അപരനാമം
നഗരം
തലക്കെട്ട്
വിശദാംശങ്ങൾ
ഫോൺ
സന്ദേശം
അടിയന്തര നില
അടിയന്തരം
സാധാരണം
തുറന്നത്
തത്സമയ നില (സ്വയം അപ്ഡേറ്റ് ചെയ്യും)
വിഭാഗം അനുസരിച്ച്
പരിഹരിച്ചു
നിങ്ങളുടെ സ്വകാര്യതയാണ് ആദ്യം. നിങ്ങൾ സഹായം സ്വീകരിച്ചതിനു ശേഷം മാത്രമേ ബന്ധപ്പെടാനുള്ള വിവരങ്ങൾ പങ്കിടൂ.
ഇതുവരെ ഒന്നുമില്ല.""")

PA = _mk("""ਭੋਜਨ ਸਹਾਇਤਾ
ਨੌਕਰੀਆਂ
ਲਾਈਵ ਸਥਿਤੀ
ਡੈਸ਼ਬੋਰਡ
ਲਾਗਇਨ
ਰਜਿਸਟਰ ਕਰੋ
ਲਾਗਆਊਟ
ਤੁਰੰਤ ਬਾਹਰ ਨਿਕਲੋ
ਸੈਕਸ ਵਰਕਰਾਂ ਲਈ ਸੁਰੱਖਿਅਤ ਅਤੇ ਨਿੱਜੀ ਸਹਾਇਤਾ
ਡਾਕਟਰੀ, ਕਾਨੂੰਨੀ, ਸਿੱਖਿਆ, ਹੁਨਰ, ਕੰਮ ਜਾਂ ਭੋਜਨ ਦੀ ਮਦਦ ਮੰਗੋ। ਤਸਦੀਕਸ਼ੁਦਾ ਸਹਾਇਕ ਜਵਾਬ ਦੇਣਗੇ।
ਮੈਨੂੰ ਮਦਦ ਚਾਹੀਦੀ ਹੈ
ਮੈਂ ਮਦਦ ਕਰਨਾ ਚਾਹੁੰਦਾ/ਚਾਹੁੰਦੀ ਹਾਂ
ਖੁੱਲ੍ਹੀਆਂ ਸਮੱਸਿਆਵਾਂ
ਜਾਰੀ ਹੈ
ਹੱਲ ਹੋਈਆਂ
ਖੁੱਲ੍ਹੀਆਂ ਨੌਕਰੀਆਂ
ਉਪਲਬਧ ਭੋਜਨ
ਤਸਦੀਕਸ਼ੁਦਾ ਸਹਾਇਕ
ਡਾਕਟਰੀ ਸਹਾਇਤਾ
ਕਾਨੂੰਨੀ ਸਹਾਇਤਾ
ਸਿੱਖਿਆ
ਹੁਨਰ ਸਿਖਲਾਈ
ਕੰਮ / ਆਮਦਨ
ਭੋਜਨ
ਸਲਾਹ / ਪਨਾਹ
ਮਦਦ ਮੰਗੋ
ਬੇਨਤੀ ਭੇਜੋ
ਮੇਰੀਆਂ ਬੇਨਤੀਆਂ
ਮਦਦ ਦੀ ਪੇਸ਼ਕਸ਼ ਕਰੋ
ਪੇਸ਼ਕਸ਼ ਭੇਜੋ
ਮਨਜ਼ੂਰ ਕਰੋ
ਨਾਮਨਜ਼ੂਰ ਕਰੋ
ਹੱਲ ਹੋਇਆ ਚਿੰਨ੍ਹਿਤ ਕਰੋ
ਫ਼ੋਨ ਕਰੋ
ਵੀਡੀਓ ਕਾਲ
ਸੁਨੇਹੇ
ਭੇਜੋ
ਚੈਟ ਅਤੇ ਕਾਲ
ਨੌਕਰੀ ਦੇ ਮੌਕੇ
ਅਰਜ਼ੀ ਦਿਓ
ਅਰਜ਼ੀ ਦਿੱਤੀ
ਨੌਕਰੀ ਪੋਸਟ ਕਰੋ
ਬਚਿਆ ਹੋਇਆ ਭੋਜਨ ਦਿਓ
ਪ੍ਰਾਪਤ ਕਰੋ
ਐਮਰਜੈਂਸੀ
ਉਪਭੋਗਤਾ ਨਾਮ
ਪਾਸਵਰਡ
ਨਾਮ / ਉਪਨਾਮ
ਸ਼ਹਿਰ
ਸਿਰਲੇਖ
ਵੇਰਵੇ
ਫ਼ੋਨ
ਸੁਨੇਹਾ
ਜ਼ਰੂਰੀ ਪੱਧਰ
ਜ਼ਰੂਰੀ
ਆਮ
ਖੁੱਲ੍ਹਾ
ਲਾਈਵ ਸਥਿਤੀ (ਆਪਣੇ ਆਪ ਅੱਪਡੇਟ ਹੁੰਦੀ ਹੈ)
ਸ਼੍ਰੇਣੀ ਅਨੁਸਾਰ
ਹੱਲ ਹੋਈਆਂ
ਤੁਹਾਡੀ ਨਿੱਜਤਾ ਸਭ ਤੋਂ ਪਹਿਲਾਂ। ਤੁਹਾਡੇ ਮਦਦ ਮਨਜ਼ੂਰ ਕਰਨ ਤੋਂ ਬਾਅਦ ਹੀ ਸੰਪਰਕ ਵੇਰਵੇ ਸਾਂਝੇ ਹੁੰਦੇ ਹਨ।
ਹਾਲੇ ਕੁਝ ਨਹੀਂ।""")

OR = _mk("""ଖାଦ୍ୟ ସହାୟତା
ଚାକିରି
ଲାଇଭ୍ ସ୍ଥିତି
ଡ୍ୟାସବୋର୍ଡ
ଲଗଇନ୍
ପଞ୍ଜିକରଣ କରନ୍ତୁ
ଲଗଆଉଟ୍
ତୁରନ୍ତ ବାହାରନ୍ତୁ
ଯୌନକର୍ମୀଙ୍କ ପାଇଁ ସୁରକ୍ଷିତ ଓ ଗୋପନୀୟ ସହାୟତା
ଡାକ୍ତରୀ, ଆଇନଗତ, ଶିକ୍ଷା, ଦକ୍ଷତା, କାମ କିମ୍ବା ଖାଦ୍ୟ ସାହାଯ୍ୟ ମାଗନ୍ତୁ। ଯାଞ୍ଚ ହୋଇଥିବା ସହାୟକମାନେ ଉତ୍ତର ଦେବେ।
ମୋତେ ସାହାଯ୍ୟ ଦରକାର
ମୁଁ ସାହାଯ୍ୟ କରିବାକୁ ଚାହେଁ
ଖୋଲା ସମସ୍ୟା
ଚାଲିଛି
ସମାଧାନ ହୋଇଛି
ଖୋଲା ଚାକିରି
ଉପଲବ୍ଧ ଖାଦ୍ୟ
ଯାଞ୍ଚ ହୋଇଥିବା ସହାୟକ
ଡାକ୍ତରୀ ସହାୟତା
ଆଇନଗତ ସହାୟତା
ଶିକ୍ଷା
ଦକ୍ଷତା ତାଲିମ
କାମ / ଆୟ
ଖାଦ୍ୟ
ପରାମର୍ଶ / ଆଶ୍ରୟ
ସାହାଯ୍ୟ ମାଗନ୍ତୁ
ଅନୁରୋଧ ପଠାନ୍ତୁ
ମୋ ଅନୁରୋଧ
ସାହାଯ୍ୟ ପ୍ରସ୍ତାବ ଦିଅନ୍ତୁ
ପ୍ରସ୍ତାବ ପଠାନ୍ତୁ
ଗ୍ରହଣ କରନ୍ତୁ
ପ୍ରତ୍ୟାଖ୍ୟାନ କରନ୍ତୁ
ସମାଧାନ ହୋଇଛି ଚିହ୍ନିତ କରନ୍ତୁ
ଫୋନ୍ କରନ୍ତୁ
ଭିଡିଓ କଲ୍
ବାର୍ତ୍ତା
ପଠାନ୍ତୁ
ଚାଟ୍ ଓ କଲ୍
ଚାକିରି ସୁଯୋଗ
ଆବେଦନ କରନ୍ତୁ
ଆବେଦନ କରାଯାଇଛି
ଚାକିରି ପୋଷ୍ଟ କରନ୍ତୁ
ବଳକା ଖାଦ୍ୟ ଦିଅନ୍ତୁ
ନିଅନ୍ତୁ
ଜରୁରୀକାଳୀନ
ଉପଯୋଗକର୍ତ୍ତା ନାମ
ପାସୱାର୍ଡ
ନାମ / ଉପନାମ
ସହର
ଶିରୋନାମା
ବିବରଣୀ
ଫୋନ୍
ବାର୍ତ୍ତା
ଜରୁରୀ ସ୍ତର
ଜରୁରୀ
ସାଧାରଣ
ଖୋଲା
ଲାଇଭ୍ ସ୍ଥିତି (ସ୍ୱୟଂଚାଳିତ ଅପଡେଟ୍)
ବର୍ଗ ଅନୁସାରେ
ସମାଧାନ ହୋଇଛି
ଆପଣଙ୍କ ଗୋପନୀୟତା ପ୍ରଥମେ। ଆପଣ ସାହାଯ୍ୟ ଗ୍ରହଣ କଲେ ହିଁ ଯୋଗାଯୋଗ ବିବରଣୀ ସେୟାର ହୁଏ।
ଏପର୍ଯ୍ୟନ୍ତ କିଛି ନାହିଁ।""")

UR = _mk("""کھانے کی مدد
ملازمتیں
لائیو صورتحال
ڈیش بورڈ
لاگ اِن
رجسٹر کریں
لاگ آؤٹ
فوراً باہر نکلیں
جنسی کارکنوں کے لیے محفوظ اور نجی مدد
طبی، قانونی، تعلیم، ہنر، کام یا کھانے کی مدد مانگیں۔ تصدیق شدہ مددگار جواب دیں گے۔
مجھے مدد چاہیے
میں مدد کرنا چاہتا/چاہتی ہوں
کھلے مسائل
جاری
حل شدہ
کھلی ملازمتیں
دستیاب کھانا
تصدیق شدہ مددگار
طبی مدد
قانونی مدد
تعلیم
ہنر کی تربیت
کام / آمدنی
کھانا
مشاورت / پناہ
مدد مانگیں
درخواست بھیجیں
میری درخواستیں
مدد کی پیشکش کریں
پیشکش بھیجیں
قبول کریں
مسترد کریں
حل شدہ کے طور پر نشان زد کریں
کال کریں
ویڈیو کال
پیغامات
بھیجیں
چیٹ اور کالز
ملازمت کے مواقع
درخواست دیں
درخواست دی گئی
ملازمت پوسٹ کریں
بچا ہوا کھانا دیں
حاصل کریں
ہنگامی
صارف نام
پاس ورڈ
نام / عرفی نام
شہر
عنوان
تفصیلات
فون
پیغام
فوری ضرورت
فوری
عام
کھلا
لائیو صورتحال (خود بخود اپڈیٹ ہوتی ہے)
زمرے کے لحاظ سے
حل شدہ
آپ کی رازداری سب سے پہلے۔ رابطے کی تفصیلات صرف اس وقت شیئر ہوتی ہیں جب آپ مدد قبول کریں۔
ابھی کچھ نہیں۔""")

STR = {"en": EN, "hi": HI, "gu": GU, "mr": MR, "bn": BN, "ta": TA, "te": TE, "kn": KN, "ml": ML, "pa": PA, "or": OR, "ur": UR}

EXTRA_KEYS = "f_state all_india state_wise how_title step1 step2 step3 who_helps".split()
def _ex(text):
    v = [x.strip() for x in text.strip().split("\n")]
    assert len(v) == len(EXTRA_KEYS)
    return dict(zip(EXTRA_KEYS, v))
EXTRA = {
"en": _ex("""State
All India
State-wise status
How it works
Post your need privately
Verified helpers respond
Accept, chat, call & get help
Who is helping"""),
"hi": _ex("""राज्य
पूरा भारत
राज्यवार स्थिति
यह कैसे काम करता है
अपनी ज़रूरत निजी तौर पर बताएँ
सत्यापित सहायक जवाब देते हैं
स्वीकार करें, चैट करें, कॉल करें और मदद पाएँ
कौन मदद कर रहा है"""),
"gu": _ex("""રાજ્ય
સમગ્ર ભારત
રાજ્ય મુજબ સ્થિતિ
આ કેવી રીતે કામ કરે છે
તમારી જરૂરિયાત ખાનગી રીતે જણાવો
ચકાસાયેલા સહાયકો જવાબ આપે છે
સ્વીકારો, ચેટ કરો, કૉલ કરો અને મદદ મેળવો
કોણ મદદ કરી રહ્યું છે"""),
"mr": _ex("""राज्य
संपूर्ण भारत
राज्यनिहाय स्थिती
हे कसे काम करते
तुमची गरज खाजगीत सांगा
पडताळलेले सहाय्यक प्रतिसाद देतात
स्वीकारा, चॅट करा, कॉल करा आणि मदत मिळवा
कोण मदत करत आहे"""),
"bn": _ex("""রাজ্য
সারা ভারত
রাজ্য অনুযায়ী অবস্থা
এটি কীভাবে কাজ করে
গোপনে আপনার প্রয়োজন জানান
যাচাইকৃত সহায়করা সাড়া দেন
গ্রহণ করুন, চ্যাট করুন, কল করুন ও সাহায্য পান
কারা সাহায্য করছেন"""),
"ta": _ex("""மாநிலம்
இந்தியா முழுவதும்
மாநில வாரி நிலை
இது எப்படி செயல்படுகிறது
உங்கள் தேவையை தனிப்பட்ட முறையில் பதிவிடுங்கள்
சரிபார்க்கப்பட்ட உதவியாளர்கள் பதிலளிக்கிறார்கள்
ஏற்றுக்கொள், அரட்டையடி, அழை, உதவி பெறு
யார் உதவுகிறார்கள்"""),
"te": _ex("""రాష్ట్రం
భారతదేశమంతా
రాష్ట్రాల వారీగా స్థితి
ఇది ఎలా పనిచేస్తుంది
మీ అవసరాన్ని గోప్యంగా తెలపండి
ధృవీకరించబడిన సహాయకులు స్పందిస్తారు
అంగీకరించండి, చాట్ చేయండి, కాల్ చేయండి, సహాయం పొందండి
ఎవరు సహాయం చేస్తున్నారు"""),
"kn": _ex("""ರಾಜ್ಯ
ಇಡೀ ಭಾರತ
ರಾಜ್ಯವಾರು ಸ್ಥಿತಿ
ಇದು ಹೇಗೆ ಕೆಲಸ ಮಾಡುತ್ತದೆ
ನಿಮ್ಮ ಅಗತ್ಯವನ್ನು ಖಾಸಗಿಯಾಗಿ ತಿಳಿಸಿ
ಪರಿಶೀಲಿಸಿದ ಸಹಾಯಕರು ಪ್ರತಿಕ್ರಿಯಿಸುತ್ತಾರೆ
ಒಪ್ಪಿಕೊಳ್ಳಿ, ಚಾಟ್ ಮಾಡಿ, ಕರೆ ಮಾಡಿ, ಸಹಾಯ ಪಡೆಯಿರಿ
ಯಾರು ಸಹಾಯ ಮಾಡುತ್ತಿದ್ದಾರೆ"""),
"ml": _ex("""സംസ്ഥാനം
ഇന്ത്യ മുഴുവൻ
സംസ്ഥാനം തിരിച്ചുള്ള നില
ഇത് എങ്ങനെ പ്രവർത്തിക്കുന്നു
നിങ്ങളുടെ ആവശ്യം സ്വകാര്യമായി അറിയിക്കുക
പരിശോധിച്ച സഹായികൾ പ്രതികരിക്കുന്നു
സ്വീകരിക്കുക, ചാറ്റ് ചെയ്യുക, വിളിക്കുക, സഹായം നേടുക
ആരാണ് സഹായിക്കുന്നത്"""),
"pa": _ex("""ਰਾਜ
ਸਾਰਾ ਭਾਰਤ
ਰਾਜ ਅਨੁਸਾਰ ਸਥਿਤੀ
ਇਹ ਕਿਵੇਂ ਕੰਮ ਕਰਦਾ ਹੈ
ਆਪਣੀ ਲੋੜ ਨਿੱਜੀ ਤੌਰ 'ਤੇ ਦੱਸੋ
ਤਸਦੀਕਸ਼ੁਦਾ ਸਹਾਇਕ ਜਵਾਬ ਦਿੰਦੇ ਹਨ
ਮਨਜ਼ੂਰ ਕਰੋ, ਚੈਟ ਕਰੋ, ਕਾਲ ਕਰੋ ਤੇ ਮਦਦ ਲਓ
ਕੌਣ ਮਦਦ ਕਰ ਰਿਹਾ ਹੈ"""),
"or": _ex("""ରାଜ୍ୟ
ସମଗ୍ର ଭାରତ
ରାଜ୍ୟ ଅନୁସାରେ ସ୍ଥିତି
ଏହା କିପରି କାମ କରେ
ଆପଣଙ୍କ ଆବଶ୍ୟକତା ଗୋପନରେ ଜଣାନ୍ତୁ
ଯାଞ୍ଚ ହୋଇଥିବା ସହାୟକମାନେ ଉତ୍ତର ଦିଅନ୍ତି
ଗ୍ରହଣ କରନ୍ତୁ, ଚାଟ୍ କରନ୍ତୁ, କଲ୍ କରନ୍ତୁ ଓ ସାହାଯ୍ୟ ପାଆନ୍ତୁ
କିଏ ସାହାଯ୍ୟ କରୁଛି"""),
"ur": _ex("""ریاست
پورا بھارت
ریاست کے لحاظ سے صورتحال
یہ کیسے کام کرتا ہے
اپنی ضرورت نجی طور پر بتائیں
تصدیق شدہ مددگار جواب دیتے ہیں
قبول کریں، چیٹ کریں، کال کریں اور مدد پائیں
کون مدد کر رہا ہے"""),
}
for _l in STR:
    STR[_l].update(EXTRA[_l])
# Added dashboard separation labels; native translations can be added per language later.
_EXTRA_V5 = {
    'get_help_nav2':'Get Help',
    'give_help_nav2':'Give Help',
    'give_help_desc2':'See people who currently need support in your verified category. Choose exactly whom you want to help.',
}
EN.update(_EXTRA_V5)
for _l in STR:
    for _k,_v in _EXTRA_V5.items():
        STR[_l].setdefault(_k,_v)



HOME_KEYS = """brand_tag nav_home2 nav_stories2 nav_help2 nav_offer2 nav_jobs2 nav_food2 nav_impact2 nav_about2 login_register2 safety2 footer_line2 hero_kicker2 hero_title_a2 hero_title_b2 hero_text2 safe_free2 be_change2 safe2 private2 verified2 no_judgment2 hero_quote2 hero_quote_by2 hero_brush2 impact_title2 impact_sub2 metric_women2 metric_medical2 metric_legal2 metric_education2 metric_skill2 metric_work2 metric_food2 problem_kicker2 problem_title2 problem_sub2 get_help_now2 problem1_title2 problem1_text2 problem2_title2 problem2_text2 problem3_title2 problem3_text2 problem4_title2 problem4_text2 stories_kicker2 stories_title2 stories_sub2 view_stories2 story1_title2 story1_by2 story2_title2 story2_by2 story3_title2 story3_by2 story4_title2 story4_by2 story5_title2 story5_by2 story6_title2 story6_by2 what_kicker2 what_title2 what_sub2 learn_more2 service_medical_2 service_legal_2 service_education_2 service_skill_2 service_livelihood_2 service_food_2 service_support_2 how_kicker2 how_title2 how_sub2 step1_title2 step1_text2 step2_title2 step2_text2 step3_title2 step3_text2 step4_title2 step4_text2 step5_title2 step5_text2 who_kicker2 who_title2 who_sub2 who_doctors2 who_lawyers2 who_teachers2 who_skills2 who_ngos2 who_csr2 who_employers2 who_restaurants2 cta_title2 cta_text2 become_helper2 privacy_title2 privacy_text2 privacy_alias2 privacy_verified2 privacy_after2 privacy_exit2 chatbot_title2 chatbot_sub2 chatbot_intro2 chatbot_help2 chatbot_privacy2 chatbot_jobs2 chatbot_placeholder2 chatbot_help_reply2 chatbot_privacy_reply2 chatbot_jobs_reply2 community_stories2 community_stories_sub2 share_story2 share_story_kicker2 share_story_title2 share_story_sub2 story_title_label2 story_title_placeholder2 story_category2 story_request2 story_no_request2 duration_auto2 story_body2 story_body_placeholder2 what_helped2 what_helped_placeholder2 outcome2 outcome_placeholder2 story_privacy2 publish_story2 time_taken2 no_stories2 be_first_story2""".split()

def _home_en():
    vals=[
    "Support · Dignity · New Beginnings","Home","Stories","Get Help","Offer Support","Jobs","Food","Our Impact","About","Login / Register","Safety","Built around dignity, privacy and practical support.",
    "SUPPORT. DIGNITY. OPPORTUNITY.","A Brighter Tomorrow","Is Always Possible.","Sahara connects women from vulnerable communities with trusted doctors, legal aid, education, skills, jobs, food and more — because everyone deserves dignity, safety and a second chance.","It's safe, private and free","Be the change","Safe","Private","Verified support","No judgment","I chose myself again, and Sahara made it possible.","A woman, 29","Different journeys. Same strength.","Our Impact So Far","Real people. Real support. Growing every day.","Women reached","Medical consultations","Legal assistance provided","Enrolled in education","Skill training opportunities","Jobs & livelihood support","Meals redistributed",
    "THE CHALLENGE","Too many women are still left without a safe path to support.","Medical care, legal guidance, learning, work and food support can be difficult to reach — especially when privacy and trust matter.","Get help now","Support is fragmented","The right service may be hard to find at the right moment.","Trust can be missing","People may hesitate to ask for help when they fear judgment or exposure.","Opportunities are limited","Skills, education and livelihood pathways are not always easy to access.","A safe second chance matters","Practical support can help someone move toward a safer, more independent future.",
    "STORIES OF STRENGTH","Different journeys. Same courage. Real change is possible.","Stories are illustrative journeys showing what practical support can mean.","View all stories","Sahara helped me get the medical care I needed when I had no one to turn to.","Illustrative journey · Healthcare","With legal support, I was able to understand my options and start a new life.","Illustrative journey · Legal aid","I learned new skills through Sahara and now I can earn independently.","Illustrative journey · Skills","I got a job opportunity and now I can support myself with dignity.","Illustrative journey · Livelihood","Sahara helped me complete my education and rebuild my confidence.","Illustrative journey · Education","Through the food support network, I never have to sleep hungry.","Illustrative journey · Food support",
    "WHAT WE DO","Connecting women with the right people at the right time.","Practical support across the areas where life can become difficult — without judgment.","Learn more","Access trusted doctors and clinics.","Get legal advice and support.","Continue your education journey.","Learn new skills for financial independence.","Find job opportunities and income support.","Surplus food from partners reaches those in need.","Counselling, shelter and other support when you need it.",
    "HOW SAHARA WORKS","Simple steps. Real impact.","A safe, guided process from asking for help to connecting privately.","Register safely","Create a safe, private account using an alias if you prefer.","Tell us what you need","Medical, legal, education, skills, work, food or other support.","Get matched","Relevant verified providers see your request.","Choose your helper","Accept an offer from a trusted provider.","Connect privately","Chat, call or video call and receive support.",
    "WHO MAKES IT POSSIBLE?","A growing community of changemakers.","Doctors, lawyers, teachers, skill institutes, NGOs, CSR organisations, employers and restaurants can contribute.","Doctors & Clinics","Lawyers & Advocates","Teachers & Educators","Skill Institutes","NGOs","CSR Organisations","Employers & Work Providers","Restaurants & Food Donors","You don't have to solve someone's life.","Sometimes, you just have to help with one part of it.","Become a Helper","Your story belongs to you.","Privacy is part of the foundation of SAHARA. Contact details are shared only after you accept help.","Alias-friendly registration","Verified providers","Contact sharing after acceptance","Quick exit",
    "SAHARA Assistant","Here to guide you","Hi. I can help you understand how SAHARA works and where to start.","I need help","Privacy","Jobs","Type your question...","If you need support, choose Get Help and tell us what you need. You can register using an alias.","SAHARA is designed around privacy. Contact details are shared only after you accept an offer.","Open Jobs shows available opportunities. You can browse them and apply when logged in.","Community stories","Real experiences shared by people who received support through Sahara.","Share your experience","COMMUNITY STORIES","Your experience can help someone else take the first step.","Tell what happened, what helped and how long it took to solve the issue.","Story title","e.g. How Sahara helped me find legal support","Support area","Link to a solved help request","No linked request","Resolution time will be calculated automatically from the request dates.","Your experience","Tell your story in your own words...","What helped?","Which person, service or support made the biggest difference?","What changed?","Tell readers what became different after receiving support.","Your story is published using your Sahara name/alias. Do not include phone numbers, addresses or other private information.","Publish my story","Time taken to resolve","No stories have been shared yet.","Be the first to share an experience that could help someone else."]
    assert len(vals)==len(HOME_KEYS),(len(vals),len(HOME_KEYS))
    return dict(zip(HOME_KEYS,vals))
HOME_EN=_home_en()
HOME={k:dict(HOME_EN) for k in STR}
# High-visibility UI translations for the 11 Indian languages. Less prominent prose falls back to the existing language pack.

story_ui={
'en':{},
'hi':{'community_stories2':'समुदाय की कहानियाँ','community_stories_sub2':'सहायता पाने वाले लोगों के वास्तविक अनुभव।','share_story2':'अपना अनुभव साझा करें','share_story_kicker2':'समुदाय की आवाज़','share_story_title2':'आपकी कहानी किसी और की शुरुआत बन सकती है।','share_story_sub2':'बताएँ क्या हुआ, किस मदद से फर्क पड़ा और समस्या को हल होने में कितना समय लगा।','story_title_label2':'कहानी का शीर्षक','story_title_placeholder2':'अपनी कहानी का शीर्षक लिखें','story_category2':'मदद का क्षेत्र','story_request2':'हल हुए अनुरोध से जोड़ें','story_no_request2':'कोई अनुरोध नहीं','duration_auto2':'समाधान का समय अपने आप निकलेगा','story_body2':'आपका अनुभव','story_body_placeholder2':'अपनी कहानी अपने शब्दों में लिखें...','what_helped2':'क्या मददगार रहा?','what_helped_placeholder2':'किस व्यक्ति, सेवा या सहायता से सबसे ज्यादा फर्क पड़ा?','outcome2':'क्या बदला?','outcome_placeholder2':'मदद मिलने के बाद क्या बेहतर हुआ?','story_privacy2':'आपकी कहानी आपके सहारा नाम/उपनाम से प्रकाशित होगी। फोन नंबर, पता या निजी जानकारी साझा न करें।','publish_story2':'मेरी कहानी प्रकाशित करें','time_taken2':'समस्या हल होने में समय','no_stories2':'अभी कोई कहानी साझा नहीं की गई है।','be_first_story2':'पहली कहानी साझा करें और किसी और को पहला कदम उठाने में मदद करें।'},
'gu':{'community_stories2':'સમુદાયની વાર્તાઓ','community_stories_sub2':'સહાય મેળવનાર લોકોના વાસ્તવિક અનુભવો.','share_story2':'તમારો અનુભવ શેર કરો','share_story_kicker2':'સમુદાયનો અવાજ','share_story_title2':'તમારી વાર્તા કોઈની નવી શરૂઆત બની શકે છે.','share_story_sub2':'શું થયું, કઈ મદદથી ફરક પડ્યો અને સમસ્યા ઉકેલવામાં કેટલો સમય લાગ્યો તે જણાવો.','story_title_label2':'વાર્તાનું શીર્ષક','story_title_placeholder2':'તમારી વાર્તાનું શીર્ષક લખો','story_category2':'મદદનો વિસ્તાર','story_request2':'ઉકેલાયેલા વિનંતી સાથે જોડો','story_no_request2':'કોઈ વિનંતી નથી','duration_auto2':'ઉકેલનો સમય આપમેળે ગણાશે','story_body2':'તમારો અનુભવ','story_body_placeholder2':'તમારી વાર્તા તમારા શબ્દોમાં લખો...','what_helped2':'શું મદદરૂપ થયું?','what_helped_placeholder2':'કયા વ્યક્તિ, સેવા અથવા સહાયથી સૌથી મોટો ફરક પડ્યો?','outcome2':'શું બદલાયું?','outcome_placeholder2':'મદદ મળ્યા પછી શું બદલાયું?','story_privacy2':'તમારી વાર્તા તમારા સહારા નામ/ઉપનામથી પ્રકાશિત થશે. ફોન નંબર, સરનામું અથવા ખાનગી માહિતી શેર ન કરો.','publish_story2':'મારી વાર્તા પ્રકાશિત કરો','time_taken2':'સમસ્યા ઉકેલવામાં લાગેલો સમય','no_stories2':'હજુ કોઈ વાર્તા શેર કરવામાં આવી નથી.','be_first_story2':'પહેલી વાર્તા શેર કરો અને કોઈને પહેલું પગલું ભરવામાં મદદ કરો.'},
'mr':{'community_stories2':'समुदायाच्या कथा','community_stories_sub2':'सहाय्य मिळालेल्या लोकांचे प्रत्यक्ष अनुभव.','share_story2':'तुमचा अनुभव शेअर करा','share_story_kicker2':'समुदायाचा आवाज','share_story_title2':'तुमची कथा कोणाच्या नव्या सुरुवातीचे कारण बनू शकते.','share_story_sub2':'काय झाले, कोणत्या मदतीने फरक पडला आणि समस्या सोडवायला किती वेळ लागला ते सांगा.','story_title_label2':'कथेचे शीर्षक','story_title_placeholder2':'तुमच्या कथेचे शीर्षक लिहा','story_category2':'मदतीचे क्षेत्र','story_request2':'सोडवलेल्या विनंतीशी जोडा','story_no_request2':'कोणतीही विनंती नाही','duration_auto2':'निराकरणाचा वेळ आपोआप मोजला जाईल','story_body2':'तुमचा अनुभव','story_body_placeholder2':'तुमची कथा तुमच्या शब्दांत लिहा...','what_helped2':'काय मदत झाली?','what_helped_placeholder2':'कोणत्या व्यक्ती, सेवेमुळे किंवा मदतीमुळे सर्वाधिक फरक पडला?','outcome2':'काय बदलले?','outcome_placeholder2':'मदत मिळाल्यानंतर काय बदलले?','story_privacy2':'तुमची कथा तुमच्या सहारा नाव/उपनावाने प्रकाशित होईल. फोन नंबर, पत्ता किंवा खासगी माहिती देऊ नका.','publish_story2':'माझी कथा प्रकाशित करा','time_taken2':'समस्या सोडवायला लागलेला वेळ','no_stories2':'अजून कोणतीही कथा शेअर केलेली नाही.','be_first_story2':'पहिली कथा शेअर करा आणि कोणाला तरी पहिले पाऊल उचलण्यास मदत करा.'},
'bn':{'community_stories2':'সম্প্রদায়ের গল্প','community_stories_sub2':'সহায়তা পাওয়া মানুষের বাস্তব অভিজ্ঞতা।','share_story2':'আপনার অভিজ্ঞতা শেয়ার করুন','share_story_kicker2':'সম্প্রদায়ের কণ্ঠ','share_story_title2':'আপনার গল্প অন্য কারও নতুন শুরুর কারণ হতে পারে।','share_story_sub2':'কী ঘটেছিল, কোন সহায়তায় পরিবর্তন এসেছে এবং সমস্যা সমাধানে কত সময় লেগেছে তা জানান।','story_title_label2':'গল্পের শিরোনাম','story_title_placeholder2':'আপনার গল্পের শিরোনাম লিখুন','story_category2':'সহায়তার ক্ষেত্র','story_request2':'সমাধান হওয়া অনুরোধের সঙ্গে যুক্ত করুন','story_no_request2':'কোনও অনুরোধ নয়','duration_auto2':'সমাধানের সময় স্বয়ংক্রিয়ভাবে গণনা হবে','story_body2':'আপনার অভিজ্ঞতা','story_body_placeholder2':'নিজের ভাষায় আপনার গল্প লিখুন...','what_helped2':'কী সাহায্য করেছে?','what_helped_placeholder2':'কোন ব্যক্তি, সেবা বা সহায়তা সবচেয়ে বেশি পার্থক্য তৈরি করেছে?','outcome2':'কী বদলেছে?','outcome_placeholder2':'সহায়তা পাওয়ার পর কী পরিবর্তন হয়েছে?','story_privacy2':'আপনার গল্প আপনার সাহারা নাম/ছদ্মনামে প্রকাশিত হবে। ফোন নম্বর, ঠিকানা বা ব্যক্তিগত তথ্য দেবেন না।','publish_story2':'আমার গল্প প্রকাশ করুন','time_taken2':'সমস্যা সমাধানে সময়','no_stories2':'এখনও কোনও গল্প শেয়ার করা হয়নি।','be_first_story2':'প্রথম গল্পটি শেয়ার করুন এবং অন্য কাউকে প্রথম পদক্ষেপ নিতে সাহায্য করুন।'}
}
for _l,_p in story_ui.items(): HOME[_l].update(_p)

patches={
'hi':{'brand_tag':'सुरक्षित जीवन · उज्ज्वल कल','nav_home2':'होम','nav_stories2':'कहानियाँ','nav_help2':'मदद लें','nav_offer2':'मदद करें','nav_jobs2':'नौकरियाँ','nav_food2':'भोजन','nav_impact2':'हमारा प्रभाव','nav_about2':'हमारे बारे में','login_register2':'लॉगिन / रजिस्टर','hero_kicker2':'सहायता। गरिमा। अवसर।','hero_title_a2':'एक उज्जवल कल','hero_title_b2':'हमेशा संभव है।','hero_text2':'सहारा महिलाओं को भरोसेमंद डॉक्टरों, कानूनी सहायता, शिक्षा, कौशल, रोजगार, भोजन और अन्य मदद से जोड़ता है।','need_help2':'मुझे मदद चाहिए','want_help2':'मैं मदद करना चाहता/चाहती हूँ','impact_title2':'अब तक का प्रभाव','problem_title2':'बहुत सी महिलाएँ आज भी सुरक्षित सहायता से दूर हैं।','stories_title2':'हर यात्रा की अपनी कहानी है।','what_title2':'सही समय पर सही व्यक्ति से जोड़ना।','how_title2':'सहारा कैसे काम करता है','who_title2':'इसे संभव कौन बनाता है?','become_helper2':'सहायक बनें','chatbot_title2':'सहारा सहायक','chatbot_intro2':'नमस्ते। मैं आपको सहारा में मदद का सही रास्ता समझाने में मदद कर सकता हूँ।'},
'gu':{'brand_tag':'સુરક્ષિત જીવન · ઉજ્જવળ આવતીકાલ','nav_home2':'હોમ','nav_stories2':'કથાઓ','nav_help2':'મદદ મેળવો','nav_offer2':'મદદ કરો','nav_jobs2':'નોકરીઓ','nav_food2':'ભોજન','nav_impact2':'અમારી અસર','nav_about2':'અમારા વિશે','login_register2':'લૉગિન / નોંધણી','hero_kicker2':'સહાય. ગૌરવ. તક.','hero_title_a2':'વધુ ઉજ્જવળ આવતીકાલ','hero_title_b2':'હંમેશા શક્ય છે.','hero_text2':'સહારા મહિલાઓને વિશ્વસનીય ડૉક્ટર, કાનૂની મદદ, શિક્ષણ, કૌશલ્ય, નોકરી, ભોજન અને અન્ય સહાય સાથે જોડે છે.','need_help2':'મને મદદ જોઈએ','want_help2':'હું મદદ કરવા માગું છું','impact_title2':'અત્યાર સુધીની અસર','problem_title2':'ઘણી મહિલાઓ આજે પણ સુરક્ષિત સહાયથી દૂર છે.','stories_title2':'દરેક મુસાફરીની પોતાની કહાની છે.','what_title2':'સાચા સમયે યોગ્ય વ્યક્તિ સાથે જોડાણ.','how_title2':'સહારા કેવી રીતે કામ કરે છે','who_title2':'આ શક્ય કોણ બનાવે છે?','become_helper2':'સહાયક બનો','chatbot_title2':'સહારા સહાયક','chatbot_intro2':'નમસ્તે. હું તમને સહારામાં મદદ મેળવવાનો યોગ્ય રસ્તો સમજાવી શકું છું.'},
'mr':{'brand_tag':'सुरक्षित जीवन · उज्ज्वल उद्या','nav_home2':'मुख्यपृष्ठ','nav_stories2':'कथा','nav_help2':'मदत घ्या','nav_offer2':'मदत करा','nav_jobs2':'नोकऱ्या','nav_food2':'अन्न','nav_impact2':'आमचा परिणाम','nav_about2':'आमच्याबद्दल','login_register2':'लॉगिन / नोंदणी','hero_kicker2':'साथ. सन्मान. संधी.','hero_title_a2':'उज्ज्वल उद्या','hero_title_b2':'नेहमी शक्य आहे.','need_help2':'मला मदत हवी','want_help2':'मला मदत करायची आहे','impact_title2':'आतापर्यंतचा परिणाम','problem_title2':'अनेक महिला आजही सुरक्षित मदतीपासून दूर आहेत.','stories_title2':'प्रत्येक प्रवासाची स्वतःची कथा असते.','what_title2':'योग्य वेळी योग्य व्यक्तीशी जोडणी.','how_title2':'सहारा कसे काम करते','who_title2':'हे शक्य कोण बनवते?','become_helper2':'सहाय्यक बना','chatbot_title2':'सहारा सहाय्यक','chatbot_intro2':'नमस्कार. सहारामध्ये मदत कुठून सुरू करायची हे समजून घेण्यात मी मदत करू शकतो.'},
}
for lang,p in patches.items(): HOME[lang].update(p)

def translate(lang,key):
    if key in HOME.get(lang,{}): return HOME.get(lang,HOME_EN).get(key,HOME_EN.get(key,key))
    return STR.get(lang, EN).get(key) or EN.get(key,key)
