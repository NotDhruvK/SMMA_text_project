from twilio.rest import Client
from config import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_PHONE_NUMBER

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)


def send_message(to, body):
    message = client.messages.create(
        body=body,
        from_=TWILIO_PHONE_NUMBER,
        to=to
    )
    return message.sid
