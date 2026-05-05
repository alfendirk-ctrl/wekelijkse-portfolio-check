import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime

def send_briefing():
    gmail_user = os.environ["GMAIL_USER"]
    gmail_password = ''.join(os.environ["GMAIL_APP_PASSWORD"].split())

    html_path = os.path.join(os.path.dirname(__file__), "email_final.html")
    if not os.path.exists(html_path):
        raise FileNotFoundError("email_final.html not found — did the routine run correctly?")

    with open(html_path, "r", encoding="utf-8") as f:
        html_content = f.read()

    today = datetime.now().strftime("%-d %B %Y")
    subject = f"Aandelen Briefing — {today}"

    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"]    = gmail_user
    msg["To"]      = gmail_user

    msg.attach(MIMEText(html_content, "html"))

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(gmail_user, gmail_password)
        server.sendmail(gmail_user, gmail_user, msg.as_string())

    print(f"✓ Briefing verstuurd naar {gmail_user}")

if __name__ == "__main__":
    send_briefing()
