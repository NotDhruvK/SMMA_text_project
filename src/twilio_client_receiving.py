from config import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_PHONE_NUMBER
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
from flask import Flask, request, redirect
from reply import big_daddy_reply
from twilio_client_sending import send_message
from celery_worker import make_celery
import time

app = Flask(__name__)
app.config.update(
    broker_url='redis://localhost:6379/0',
    result_backend='redis://localhost:6379/0'
)
celery = make_celery(app)

@celery.task
def delayed_response(number, message_body):
	print(f"Task received for number: {number} with message: {message_body}")
	time.sleep(35)
	message = big_daddy_reply(number, message_body)

	if (message == "null"):
		print(f"Negative response for {number}")
		return 0 

	send_message(number, message)
	print(f"Replied to {number} with \n {message}")

@app.route("/")
def index():
	return "<h1> Get out of here!!!</h1>"

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
	number = request.form['From']
	message_body = request.form['Body']

	delayed_response.delay(number, message_body)

	resp = MessagingResponse()
	return str(resp)

if __name__ == "__main__":
	app.run(debug=True)