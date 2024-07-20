from config import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_PHONE_NUMBER
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
from flask import Flask, request, redirect
from reply import big_daddy_reply
from time import sleep

app = Flask(__name__)

@app.route("/")
def index():
	return "<h1> Get out of here!!!</h1>"

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
	print(request.form)

	number = request.form['From']
	message_body = request.form['Body']

	message = big_daddy_reply(number, message_body)

	if (message == "null"):
		print(f"Negative response for {number}")
		return 0 

	time.sleep(35)

	resp = MessagingResponse()
	resp.message(message)

	print(f"Replied to {number} with \n {message}")

	return str(resp)

if __name__ == "__main__":
	app.run(debug=True)