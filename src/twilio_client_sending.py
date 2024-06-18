from config import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_PHONE_NUMBER
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
from flask import Flask, request, redirect
from sms_counter import SMSCounter

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)


def send_message(to, body):
    message = client.messages.create(
        body = body,
        from_= TWILIO_PHONE_NUMBER,
        to = to
    )
    print(message.body)
    return message.sid

if __name__ == "__main__":
    counter = SMSCounter.count("Hello, This is a robbery")
    print(counter)
