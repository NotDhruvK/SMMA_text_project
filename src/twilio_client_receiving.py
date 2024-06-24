from config import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_PHONE_NUMBER
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
from flask import Flask, request, redirect

app = Flask(__name__)

@app.route("/")
def index():
	return "<h1> Get out of here!!!</h1>"

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
	print(request.form)

	number = request.form['From']
	message_body = request.form['Body']

	# save to the database using "Contact" key
		#  

	resp = MessagingResponse()
	resp.message("Hello {}, you said {}".format(number, message_body))

	return str(resp)

if __name__ == "__main__":
	app.run(debug=True)