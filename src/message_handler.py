# This file will contain all the message recieving and sending related functions
import math
from googlefiles import set_sms_segments, get_database


def add_country_code(phone_number):
    """
    Adds '+1' to the beginning of the phone number.

    Args:
    phone_number (str): The phone number to which '+1' will be added.

    Returns:
    str: The phone number with '+1' added to the beginning.
    """
    return '+1' + phone_number


def SMS_segment_counter(message):
	'''
		This function will calculate the sms segments in a string and set it 
		on the database
		returns : NONE
	'''
	message_len = len(message.lower())
	segments = math.ceil(message_len/160)
	return segments

	
def sentiment_analyser(reply):
	'''
		Figures out if a sms is positive or negative
		returns : Integer
	'''
	negative = 0
	positive = 1
	sentiments = {
						"positive" : [
										"yes",
										"yea",
										"yup",
										"thats right",
										"yeah",
										"that's right",
										"great",
										"thanks",
										"correct",
										"works",
										"cool"
									 ],
						"negative" : [
										"no",
										"nah",
										"not interested",
										"stop",
										"unsubscribe",

					 				 ]
	}

	for key, values in sentiments.items():
		for value in values:
			if value in reply:
				if key == 'negative':
					return 0
				elif key == 'positive':
					return 1
	return None


if __name__ == "__main__":
	dataframe = get_database()
	print(dataframe)
	
	
