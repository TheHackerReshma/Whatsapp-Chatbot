from flask import Flask, request, jsonify
import random
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

# Sample cybersecurity quiz questions
quiz_data = [
    {"question": "What does VPN stand for?", "options": ["Virtual Private Network", "Very Personal Node", "Verified Protocol Network", "Virtual Protected Net"], "answer": "Virtual Private Network"},
    {"question": "Which of the following is NOT a strong password practice?", "options": ["Using a mix of letters, numbers, and symbols", "Using personal information", "Using long passphrases", "Regularly updating passwords"], "answer": "Using personal information"},
    {"question": "What is phishing?", "options": ["A hacking technique", "A form of cyberattack that tricks users into revealing personal information", "A secure encryption method", "A network protocol"], "answer": "A form of cyberattack that tricks users into revealing personal information"},
]

red_team_tips = [
    "Use Kali Linux for penetration testing.",
    "Always get proper authorization before ethical hacking.",
    "Utilize tools like Metasploit, Nmap, and Burp Suite.",
    "Stay updated with the latest exploits and vulnerabilities."
]

blue_team_tips = [
    "Regularly update and patch software to prevent vulnerabilities.",
    "Monitor logs for any unusual activity.",
    "Implement strong access controls and least privilege principles.",
    "Use SIEM tools to detect and respond to threats proactively."
]

@app.route("/whatsapp", methods=["POST"])
def whatsapp():
    incoming_msg = request.values.get("Body", "").lower()
    resp = MessagingResponse()
    msg = resp.message()
    
    if "quiz" in incoming_msg:
        question = random.choice(quiz_data)
        msg.body(f"{question['question']}\nOptions: {', '.join(question['options'])}")
    elif "awareness" in incoming_msg:
        tips = [
            "Use strong and unique passwords for all accounts.",
            "Enable two-factor authentication (2FA) whenever possible.",
            "Be cautious of phishing emails and suspicious links.",
            "Keep your software and antivirus updated regularly.",
            "Never share personal or sensitive information online unnecessarily."
        ]
        msg.body(random.choice(tips))
    elif "red team" in incoming_msg:
        msg.body(random.choice(red_team_tips))
    elif "blue team" in incoming_msg:
        msg.body(random.choice(blue_team_tips))
    else:
        msg.body("I can provide cybersecurity quizzes and tips. Type 'quiz' for a question, 'awareness' for security tips, 'red team' for offensive security tips, or 'blue team' for defensive security tips.")
    
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
