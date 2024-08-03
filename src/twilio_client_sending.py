from config import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_PHONE_NUMBER, TWILIO_MSERVICE_SID
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
from flask import Flask, request, redirect
from message_handler import add_country_code

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

"""
messages: 
    First basic message:
        Hi {Name), Swam here from Cognicraft. We’re looking to partner up with ambitious practices keen on exponentially growing their revenue. Our Expert Program gets you 10-15+ new clients in the next 30-45 days guaranteed. Would that be something you might be interested in?

    Second reply:
        Would you mind if I give you a quick call in the next hour?

    Reactivation 1 reply:
        Hey just checking. Did you get my last message?

"""

def is_valid_us_phone_number(phone_number: str) -> bool:
    """
    Check if the phone number is a valid US phone number without +1 and no spaces or separators.
    
    Args:
    phone_number (str): The phone number to check.
    
    Returns:
    bool: True if the phone number is valid, False otherwise.
    """
    return len(phone_number) == 10 and phone_number.isdigit()


def send_message(number, body):
    if (is_valid_us_phone_number(number)):
        number = add_country_code(number)
        message = client.messages.create(
            messaging_service_sid = TWILIO_MSERVICE_SID,
            body = body,
            from_= TWILIO_PHONE_NUMBER,
            to = number
        )
        # print(message.body)
        return message.sid
    else:
        return 0

if __name__ == "__main__":
    send_message(number, body)
    pass