# This file will contain the functions and the functionality to be run every hour
import pandas as pd
from date_counter import today_date
from twilio_client_sending import send_message
from message_handler import SMS_segment_counter
from googlefiles import get_sms_segments, set_sms_segments, get_database, get_hourly_rate, update_sheets_database


if __name__ == "__main__":
	# get the dataframe
	dataframe = get_database().dropna(axis=0, how='all')

	# retrieve contacts with the "Status" tag "TODAY" and store them in a list
	hourly_rate = get_hourly_rate()
	count = get_sms_segments()
	date = today_date()
	#print(dataframe)

	for i in range(0, int(hourly_rate)):
		# Breaking if i = len(dataframe)
		if (i == len(dataframe)):
			print("Error data out of bounds")
			break

		message_segments = get_sms_segments()
		if (message_segments > 1800):
			print("Finished today's SMS limit")

			if ((dataframe.loc[i, "Status"] == "TODAY")):
				dataframe.at[i, "Status"] = "To Contact"

			break


		if ((dataframe.loc[i, "Status"] == "To Contact") 
			and pd.isna(dataframe.loc[i, "Last sent message"])):

			# Sending message to a new contact
			name = dataframe.loc[i, "Name"]
			contact = dataframe.loc[i, "Phone"]
			message = f"Hey {name}, this is Dhruv. I was wondering if you are still offering therapy?"
			# send_message(contact, message)

			# Updating the database
			count = count + SMS_segment_counter(message)
			datadrame.at[i, "Contacted On"] == date
			dataframe.at[i, "Status"] == "Waiting"
			dataframe.at[i, "In Stage"] == "Activation"
			dataframe.at[i, "Last sent message"] == message
			continue

		if ((dataframe.loc[i, "Status"] == "To Contact")
			and (dataframe.loc[i, "In Stage"] == "Reactivation 1")):

			# Sending message to contact in Reactivation 1
			name = dataframe.loc[i, "Name"]
			contact = dataframe.loc[i, "Phone"]
			message = f"Hey just checking. Did you get my last message?"

			# Updating the database
			count = count + SMS_segment_counter(message)
			datadrame.at[i, "Contacted On"] == date
			dataframe.at[i, "Status"] == "Waiting"
			dataframe.at[i, "In Stage"] == "Reactivation 1"
			dataframe.at[i, "Last sent message"] == message
			continue



		if ((dataframe.loc[i, "Status"] == "To Contact")
			and (dataframe.loc[i, "In Stage"] == "Reactivation 2")):

			# Sennding message to contact in reactivation 2
			name = dataframe.loc[i, "Name"]
			contact = dataframe.loc[i, "Phone"]
			message = f"Hey… I feel like I'm drawing blanks here but would you be opposed to a quick chat regarding growing your business?"

			# Updating the database
			count = count + SMS_segment_counter(message)
			datadrame.at[i, "Contacted On"] == date
			dataframe.at[i, "Status"] == "Waiting"
			dataframe.at[i, "In Stage"] == "Reactivation 2"
			dataframe.at[i, "Last sent message"] == message
			continue

	set_sms_segments(count)
	print(f"Updated SMS segments to : {count}")

	update_sheets_database(dataframe)
	print(f"Updated sheets database")

	#get_hourly_message()
	# for loop
		# check message segments for the day
			# if message_segments > 1800
				# change all remaining "TODAY" tags to "To contact"
			# else
				# get message to send
				# send message
				# update database with last contact and message and positive
				# update segments
