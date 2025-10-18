import pandas as pd
import smtplib
from datetime import datetime, timedelta
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# --- CONFIG ---
CSV_FILE = "leads.csv"           # leads file: name, email, last_contact_date, status
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_USER = "your_email@gmail.com"
EMAIL_PASS = "your_app_password"
FOLLOWUP_DAYS = 7                # days since last contact to trigger follow-up

# --- LOAD LEADS ---
df = pd.read_csv(CSV_FILE)
today = datetime.now()

# --- FILTER LEADS THAT NEED FOLLOW-UP ---
df['last_contact_date'] = pd.to_datetime(df['last_contact_date'])
df['days_since_contact'] = (today - df['last_contact_date']).dt.days
followup_leads = df[df['days_since_contact'] >= FOLLOWUP_DAYS]

print(f"Found {len(followup_leads)} leads needing follow-up.")

# --- SEND EMAILS ---
def send_followup_email(to_email, name):
    subject = f"Just checking in, {name}"
    body = f"""
    Hi {name},

    I wanted to follow up to see if you had a chance to review our last discussion.
    We’d love to help you achieve your goals — happy to answer any questions or share more details.

    Best,
    [Your Name]
    """
    msg = MIMEMultipart()
    msg['From'] = EMAIL_USER
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(EMAIL_USER, EMAIL_PASS)
        server.send_message(msg)

# --- LOOP THROUGH LEADS ---
for _, row in followup_leads.iterrows():
    try:
        send_followup_email(row['email'], row['name'])
        print(f"✅ Follow-up sent to {row['name']} ({row['email']})")
        df.loc[df['email'] == row['email'], 'last_contact_date'] = today
    except Exception as e:
        print(f"❌ Error sending to {row['email']}: {e}")

# --- SAVE UPDATED LEADS FILE ---
df.to_csv(CSV_FILE, index=False)
print("✅ All done — updated lead file saved.")
