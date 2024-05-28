import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from os.path import basename
from email import encoders
from config import EMAIL_HOST, EMAIL_PORT, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD


def send_daily_summary():
    # Example implementation for sending a daily email summary
    # This is just a placeholder function
    print("Sending daily summary...")

    TO_EMAILS = ["dhruvadam@gmail.com","swayambeloskar@gmail.com"]
    ATTACHMENT_FILE = "E:\\Business\\Agency\\textproject\\data\\tosend.csv"

    subject = "Daily Summary"
    body = "Here is the summary of today's contacts."

    msg = MIMEMultipart()
    msg['From'] = EMAIL_HOST_USER
    msg['To'] = ", ".join(TO_EMAILS)
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    # Add attachment
    with open(ATTACHMENT_FILE, 'rb') as f:
        attachment = MIMEApplication(f.read(), Name=basename(ATTACHMENT_FILE))
        encoders.encode_base64(attachment)
        attachment['Content-Disposition'] = f'attachment; filename="{basename(ATTACHMENT_FILE)}"'
        msg.attach(attachment)


    try:
        server = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)
        server.starttls()
        server.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
        text = msg.as_string()
        server.sendmail(EMAIL_HOST_USER, TO_EMAILS, text)
        server.quit()

        print("Email sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")


if __name__ == "__main__":
    send_daily_summary()