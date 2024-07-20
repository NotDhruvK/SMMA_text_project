import pandas as pd
from googlefiles import get_database, update_sheets_database
from date_counter import today_date
from message_handler import sentiment_analyser

def drop_plus_one(phone_number):
    '''
    Drops the "+1" prefix from a phone number string
    and returns the remaining numbers as a string.
    Args:
    phone_number (str): The phone number string in the format "+19729617656"
    Returns:
    str: The phone number without the "+1" prefix
    '''
    if phone_number.startswith("+1"):
        return phone_number[2:]
    return phone_number

def get_message(phone, dataframe):
	'''
		This function will take the dataframe and the contact number and
		return the message based on the value

		returns : String as message
	'''
	message = ""
	for i in range(200000):
		if (i == len(dataframe)):
			break

		if (dataframe.loc[i, "Phone"] == phone):
			# Both Yes acquired
			if ((dataframe.loc[i, "First Yes"] == "Done") 
			and (dataframe.loc[i, "Second Yes"] == "Done")):

				message = "Would you mind if I give you a quick call in the next hour?"
				break

			# One yes and Activation
			elif ((dataframe.loc[i, "First Yes"] == "Done")
				and (dataframe.loc[i, "In Stage"] == "Activation")):

				message = """Hi {Name), Swam here from Cognicraft. We’re looking to partner up with ambitious practices keen on exponentially growing their revenue. Our Expert Program gets you 10-15+ new clients in the next 30-45 days guaranteed. Would that be something you might be interested in?"""
				break
			
			# One Yes and Reactivation 1
			elif ((dataframe.loc[i, "First Yes"] == "Done")
				and (dataframe.loc[i, "In Stage"] == "Reactivation 1")):

				message = "Hey just checking. Did you get my last message?"
				break

			# One Yes and Reactivation 2
			elif ((dataframe.loc[i, "First Yes"] == "Done")
				and (dataframe.loc[i, "In Stage"] == "Reactivation 2")):

				message = """Hey… I feel like I'm drawing blanks here but would you be opposed to a quick chat regarding growing your business?"""
				break

	return message
	pass
	

def big_daddy_reply(contact, recieved_message):
	'''
		This is the function that will call all the other minor 
		functions and run the processing like changing the database,
		getting from the database, updating the entries

		returns : String which will be replied.

	'''
	recieved_message = recieved_message.lower()
	dataframe = get_database()
	print(dataframe)
	date = today_date()
	sentiment = sentiment_analyser(recieved_message)
	phone = drop_plus_one(contact)
	print(phone)

	# message recieved
	# is it positive or negative?
	for i in range(200000):
		if (i == len(dataframe)):
			break

	#update database
		# positive reply
		if (sentiment == 1):
			if (dataframe.loc[i, "Phone"] == phone):
				# If the first yes is already acquired
				if (dataframe.loc[i, "First Yes"] == "Done"):
					dataframe.at[i, "Second Yes"] = "Done"
					dataframe.at[i, "Last recieved message"] = recieved_message

					if ((dataframe.loc[i, "First Yes"] == "Done") and
						(dataframe.loc[i, "Second Yes"] == "Done")):

						dataframe.at[i, "Status"] = "Sent to call"
					break

				# If first yes is not acquired
				else:
					dataframe.at[i, "First Yes"] = "Done"
					dataframe.at[i, "Last recieved message"] = recieved_message
					break

		# negative reply
		elif (sentiment == 0):
			if (dataframe.loc[i, "Phone"] == phone):
				if (pd.isna(dataframe.loc[i, "First Yes"])):
					dataframe.at[i, "Status"] = "Deleted"
					message = "null"
					update_sheets_database(dataframe)
					return message
					break

				if (dataframe.loc[i, "First Yes"] == "Done"):
					dataframe.at[i, "Status"] = "Removed"
					message = "null"
					update_sheets_database(dataframe)
					return message
					break
			pass

	message = get_message(phone, dataframe)
	# print(dataframe)

	# Print the message which will be sent
	print("Getting message based on dataframe")
	print("Message : "  + message)

	# Update the database
	update_sheets_database(dataframe)

	return message

if __name__ == "__main__":
	big_daddy_reply("+19729617656", "yes")
	