# This file will contain all the message recieving and sending related functions
import math
from googlefiles import set_sms_segments, get_database


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
										"thats right"
									 ],
						"negative" : [
										"no",
										"not interested"
					 				 ]
	}

	for key, values in sentiments.items():
		if reply in values:
			if key == 'negative':
				return 0
			elif key == 'positive':
				return 1
	return None


if __name__ == "__main__":
	dataframe = get_database()
	print(dataframe)
	
	
