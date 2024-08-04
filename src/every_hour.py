# This file will contain the functions and the functionality to be run every hour
import pandas as pd
from date_counter import today_date
from twilio_client_sending import send_message
from message_handler import SMS_segment_counter
from twilio_client_sending import is_valid_us_phone_number
from googlefiles import get_sms_segments, set_sms_segments, get_database, get_hourly_rate, update_sheets_database


if __name__ == "__main__":
	# get the dataframe
	dataframe = get_database()

	# retrieve contacts with the "Status" tag "TODAY" and store them in a list
	hourly_rate = get_hourly_rate()
	count = get_sms_segments()
	count = int(count)
	date = today_date()
	message_segments = get_sms_segments()
	message_count = 0
	#print(dataframe)

	for i in range(len(dataframe)):
		# Breaking if i = len(dataframe)
		if (i == len(dataframe)):
			print("Error data out of bounds")
			break

		if (message_count == hourly_rate):
			print(f"Sent the decided number of hourly messages.")
			break

		if (int(message_segments) > 1800):
			print("Finished today's SMS limit")

			if ((dataframe.loc[i, "Status"] == "TODAY")):
				dataframe.at[i, "Status"] = "To Contact"

			break


		if ((dataframe.loc[i, "Status"] == "TODAY") 
			and pd.isna(dataframe.loc[i, "Last sent message"])):

			# Sending message to a new contact
			name = dataframe.loc[i, "Name"]
			contact = dataframe.loc[i, "Phone"]
			message = f"Hey {name}! I was wondering if you are still offering therapy?"

			#sending message
			if (is_valid_us_phone_number(contact)):
				send_message(contact, message)
				message_count += 1
			else:
				print("Invalid Phone")
				continue

			# Updating the database
			count = count + SMS_segment_counter(message)
			dataframe.at[i, "Contacted On"] = date
			dataframe.at[i, "Status"] = "Waiting"
			dataframe.at[i, "In Stage"] = "Activation"
			dataframe.at[i, "Last sent message"] = message
			continue

		if ((dataframe.loc[i, "Status"] == "TODAY")
			and (dataframe.loc[i, "In Stage"] == "Activation")
			and pd.notna(dataframe.loc[i, "Last sent message"])):

			# Sending message to contact in Activation but waiting
			name = dataframe.loc[i, "Name"]
			contact = dataframe.loc[i, "Phone"]
			message = f"Hey just checking. Did you get my last message?"
			#sending message
			if (is_valid_us_phone_number(contact)):
				send_message(contact, message)
				message_count += 1
			else:
				print("Invalid Phone")
				continue

			# Updating the database
			count = count + SMS_segment_counter(message)
			dataframe.at[i, "Contacted On"] = date
			dataframe.at[i, "Status"] = "Waiting"
			dataframe.at[i, "In Stage"] = "Activation"
			dataframe.at[i, "Last sent message"] = message
			continue
	

		if ((dataframe.loc[i, "Status"] == "TODAY")
			and (dataframe.loc[i, "In Stage"] == "Reactivation 1")):

			# Sending message to contact in Reactivation 1
			name = dataframe.loc[i, "Name"]
			contact = dataframe.loc[i, "Phone"]
			message = f"Hey you there?"
			#sending message
			if (is_valid_us_phone_number(contact)):
				send_message(contact, message)
				message_count += 1
			else:
				print("Invalid Phone")
				continue

			# Updating the database
			count = count + SMS_segment_counter(message)
			dataframe.at[i, "Contacted On"] = date
			dataframe.at[i, "Status"] = "Waiting"
			dataframe.at[i, "In Stage"] = "Reactivation 1"
			dataframe.at[i, "Last sent message"] = message
			continue



		if ((dataframe.loc[i, "Status"] == "TODAY")
			and (dataframe.loc[i, "In Stage"] == "Reactivation 2")):

			# Sending message to contact in reactivation 2
			name = dataframe.loc[i, "Name"]
			contact = dataframe.loc[i, "Phone"]
			message = f"Hey… I feel like I'm drawing blanks here but would you like to have a quick chat regarding growing your business?"
			#sending message
			if (is_valid_us_phone_number(contact)):
				send_message(contact, message)
				message_count += 1
			else:
				print("Invalid Phone")
				continue

			# Updating the database
			count = count + SMS_segment_counter(message)
			dataframe.at[i, "Contacted On"] = date
			dataframe.at[i, "Status"] = "Waiting"
			dataframe.at[i, "In Stage"] = "Reactivation 2"
			dataframe.at[i, "Last sent message"] = message
			continue

	set_sms_segments(count)
	print(f"Updated SMS segments to : {count}")

	update_sheets_database(dataframe)
	print("Completed every_hour.py")