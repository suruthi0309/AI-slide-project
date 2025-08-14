from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Base images (cycled through)
image_pool = [
    "/static/images/images2.png",
    "/static/images/images3.png",
    "/static/images/images1.png"
]

# Define base slide data
base_slide_data = [
    {
        "type": "default",
        "module": "Module 3: Statistics and EDA",
        "title": "Challenges in",
        "highlight": "Digital Payments",
        "extra_label": None
    },
    {
        "module": "Module 4",
        "extra_label": "Social Media Marketing (SMM) + Email & WhatsApp Marketing",
        "title": "Introduction to Digital Payments",
        "points": [
            "Digital payments refer to transactions made through digital or electronic modes without the use of physical cash.",
            "They make use of the technology and medium of internet/intranet"
        ],
        "type": "intro"
    },
    {
        "module": "Module 4",
        "extra_label": "Social Media Marketing (SMM) + Email & WhatsApp Marketing )",
        "title": "Growth of",
        "highlight": "Digital Payments",
        "points": [
            "The digital payments ecosystem has seen explosive growth driven by mobile devices, fintech innovation, and user convenience.",
            "Emergence of NEFT, RTGS, UPI have created a wow feeling amongst the users"
        ],
        "type": "growth"
    },
    {
        "module": "Module 4",
        "extra_label": "Social Media Marketing (SMM) + Email & WhatsApp Marketing )",
        "title": "Overview of",
        "highlight": "Cybersecurity in Digital Payments",
        "points": [
            "Cybersecurity refers to Protecting digital payment systems from fraud, hacking, and unauthorized access.",
            "Ensuring safety and security of the transaction and giving confidence to the user that the amount remitted reaches the intended person/beneficiary without being materially altered"
        ],
        "type": "cyber"
    },
    {
        "type": "threats",
        "module": "Module 4",
        "extra_label": "Social Media Marketing (SMM) + Email & WhatsApp Marketing :)",
        "title": "Types of Cyber Threats",
        "threats": [
            "Common threats include",
            "Phishing",
            "Ransomware",
            "Malware",
            "Vishing",
            "Man-in-the-middle attacks."
        ]
    },
     {
    "type": "phishing_details",
    "module": "Module 4",
    "extra_label": "Social Media Marketing (SMM) + Email & WhatsApp Marketing",
    "title": "Phishing Attacks",
    "point1": "Fraudsters trick users into providing sensitive information like passwords and OTPs. The email are sent to persons appearing to have originated from accredited office/bank. The tone of emails will be threatening/ warning. They have been sent from fake ids/websites",
    "point2": "Phishing is a type of cyberattack where malicious actors deceive individuals into revealing sensitive information or taking actions that compromise their security. This is typically achieved by disguising the attacker as a trusted entity..."
},{
  "type": "phishing_working",
  "module": "Module 4",
  "extra_label": "Social Media Marketing (SMM) + Email & WhatsApp Marketing",
  "title": "How Phishing Works",
  "items": [
    {"label": "Deceptive Communication", "description": "Phishing attacks often involve emails, text messages..."},
    {"label": "Social Engineering", "description": "Attackers use psychological manipulation..."},
    {"label": "Malicious Links/Attachments", "description": "Phishing attempts include fake links..."},
    {"label": "Data Theft", "description": "Once a victim provides information or downloads malware..."},
    {"label": "Email Phishing", "description": "The most common type, where attackers send fraudulent emails..."},
    {"label": "Smishing", "description": "Phishing attacks conducted via SMS text messages."}
  ]
},
{
  "type": "malware_ransomware",
   "module": "Module 4",
  "extra_label": "Social Media Marketing (SMM) + Email & WhatsApp Marketing",
  "title": "Malware and Ransomware",
  "image": "images/ransomware.png",
  "items": [
    {
      "icon": "icons/shield.png",
      "text": "Malicious software can infiltrate systems, steal data, or lock users out until a ransom is paid."
    },
    {
      "icon": "icons/microchip.png",
      "text": "Malware is a broad term for malicious software designed to harm or exploit computer systems, while ransomware is a specific type of malware that locks and encrypts a victim's data, demanding a ransom payment to restore access"
    }
  ]
},
{
    "type": "man_in_the_middle",
    "module": "Module 4",
    "extra_label": "Social Media Marketing (SMM) + Email & WhatsApp Marketing )",
    "title": "Man-in-the-Middle Attacks",
    "items": [
        {"text": "Hackers intercept communication between two parties to steal information."},
        {"text": "Ethical and Unethical hackers are two categories"},
        {"text": "Ethical hacker’s goal to find out the loop holes in the system and take corrective steps for strengthening the system."},
        {"text": "Unethical hacker hacks the system for personal gain or to sabotage the system/network"}
    ]
},
{
  "type": "data_breaches",
  "module": "Module 4",
  "extra_label": "Social Media Marketing (SMM) + Email & WhatsApp Marketing )",
  "title": "Data Breaches",
  "items": [
    { "text": "Large-scale hacks targeting user data can compromise millions of digital payment accounts." },
    { "text": "The data is gained can be used for unethical purposes such as selling of data for gainful purposes." },
    { "text": "Example City Bank card data was breached and millions of card holders data was compromised in 2007–08" }
  ]
},
{
  "type": "fraud_prevention",
  "module": "Module 4",
  "extra_label": "Social Media Marketing (SMM) + Email & WhatsApp Marketing )",
  "title": "Fraud Detection and Prevention",
  "items": [
    {
      "text": "Machine learning and AI are used to detect unusual patterns and prevent fraudulent activities.",
      "icon": "icons/icon3.png"
    },
    {
      "text": "All systems will have Intrusion Detection System (IDS) and Intrusion Prevention System (IPS). IDS is post-mortem and IPS is a preventive measure.",
      "icon": "icons/icon4.png"
    }
  ]
}







]

# To alternate images
access_counter = 0

@app.route('/')
def slides():
    global access_counter

    slides = []
    for i, slide in enumerate(base_slide_data):
        new_slide = slide.copy()
        new_slide['image_url'] = image_pool[(access_counter + i) % len(image_pool)]
        slides.append(new_slide)

    access_counter += 1
    return render_template("slide.html", slides=slides, logo_url="/static/images/career247-logo.png")


@app.route('/update-slide', methods=['POST'])
def update_slide():
    data = request.get_json()
    index = int(data['slideIndex'])
    field = data['field']
    new_value = data['newValue']

    if index >= len(base_slide_data):
        return jsonify(success=False, message="Slide index out of range")

    slide = base_slide_data[index]

    # Update fields based on field name
    if field == 'module':
        slide['module'] = new_value
    elif field == 'title':
        slide['title'] = new_value
    elif field == 'highlight' and 'highlight' in slide:
        slide['highlight'] = new_value
    elif field == 'extra_label' and 'extra_label' in slide:
        slide['extra_label'] = new_value
    elif field.startswith('point-'):
        point_index = int(field.split('-')[1])
        if 'points' in slide and point_index < len(slide['points']):
            slide['points'][point_index] = new_value
    elif field == 'point1' and 'point1' in slide:
        slide['point1'] = new_value
    elif field == 'point2' and 'point2' in slide:
        slide['point2'] = new_value
    elif field.startswith('threat-'):
        threat_index = int(field.split('-')[1])
        if 'threats' in slide and threat_index < len(slide['threats']):
            slide['threats'][threat_index] = new_value

    return jsonify(success=True)


if __name__ == '__main__':
    app.run(debug=True)
