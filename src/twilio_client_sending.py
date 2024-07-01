from config import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_PHONE_NUMBER, TWILIO_MSERVICE_SID
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
from flask import Flask, request, redirect
from message_handler import add_country_code

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)


def send_message(number, body):
    number = add_country_code(number)
    message = client.messages.create(
        messaging_service_sid = TWILIO_MSERVICE_SID,
        body = body,
        from_= TWILIO_PHONE_NUMBER,
        to = number
    )
    # print(message.body)
    return message.sid

