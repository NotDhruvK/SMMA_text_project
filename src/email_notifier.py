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


def send_yesterday_stats(yesterday_date, x, y, z, w, a):
    print("Sending yesterday's summary...")

    TO_EMAILS = ["dhruvadam@gmail.com"]

    subject = f"{yesterday_date} System Summary"
    body = f'''
            Here is yesterday's summary \n\n
            Leads remaining in the system: {x} \n
            Number of contacts contacted yesterday: {y} \n
            Number of new contacts to be contacted today: {w} \n
            Number of contacts we are awaiting a response from: {z} \n
            Number of segments used yesterday: {a} \n\n
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


def send_15_min_stats(today_date, my_list):
    print("Sending 15 min emails")

    TO_EMAILS = ["dhruvadam@gmail.com"]
    subject = f"{today_date} contacts that have 2 yes's"

    # Ensure all items in the list are strings
    my_list = [str(item) for item in my_list]

    # Create the email content
    body = "Here are the contacts that replied:\n\n" + "\n".join(my_list) + "\nRegards, \nMachine"

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

'''
if __name__ == "__main__":
    send_daily_summary()
'''