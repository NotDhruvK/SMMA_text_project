import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import EMAIL_HOST, EMAIL_PORT, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD


def send_daily_summary():
    # Example implementation for sending a daily email summary
    # This is just a placeholder function
    print("Sending daily summary...")

    subject = "Daily Summary"
    body = "Here is the summary of today's contacts."

    msg = MIMEMultipart()
    msg['From'] = EMAIL_HOST_USER
    msg['To'] = 'your_email@example.com'  # Change to the recipient's email address
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)
        server.starttls()
        server.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
        text = msg.as_string()
        server.sendmail(EMAIL_HOST_USER, 'your_email@example.com', text)
        server.quit()

        print("Email sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")
