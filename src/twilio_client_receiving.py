from flask import request
from twilio.twiml.messaging_response import MessagingResponse
from app import app
from tasks import delayed_response

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