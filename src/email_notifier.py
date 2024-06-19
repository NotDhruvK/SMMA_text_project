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

    subject = "Daily Summary"
    body = "Here is the summary of today's contacts."

    msg = MIMEMultipart()
    msg['From'] = EMAIL_HOST_USER
    msg['To'] = ", ".join(TO_EMAILS)
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

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


def send_yesterday_stats(yesterday_date, x, y, z, w):
    print("Sending yesterday's summary...")

    TO_EMAILS = ["dhruvadam@gmail.com"]

    subject = f"{yesterday_date} System Summary"
    body = f'''
            Here is yesterday's summary \n\n
            Leads remaining in the system: {x} \n
            Number of contacts contacted yesterday: {y} \n
            Number of new contacts to be contacted today: {w} \n
            Number of contacts we are awaiting a response from: {z} \n\n
            Regards, \n
            Machine
            '''

    msg = MIMEMultipart()
    msg['From'] = EMAIL_HOST_USER
    msg['To'] = ", ".join(TO_EMAILS)
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

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
    pass

'''
if __name__ == "__main__":
    send_daily_summary()
'''