from config import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_PHONE_NUMBER
from twilio_client_sending import send_message
from reply import big_daddy_reply
import time
from celery_worker import celery


@celery.task
def delayed_response(number, message_body):
    print(f"Task received for number: {number} with message: {message_body}")
    
    time.sleep(25)
    message = big_daddy_reply(number, message_body)

    if message == "null":
        print(f"Negative response for {number}")
        return 0 
    send_message(number, message)

    print(f"Replied to {number} with \n {message}")
