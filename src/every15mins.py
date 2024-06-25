from googlefiles import get_database, update_sheets_database
from date_counter import today_date
from email_notifier import send_15_min_stats

if __name__ == "__main__":
	dataframe = get_database()
	send_list= []
	date = today_date()

	# check which entries have both yes as done
	for i in range(200000):
		# Break if range is out of bounds
		if (i == len(dataframe)):
			break

		# Get status and get the necessary variables
		if (dataframe.loc[i, "Status"] == "Sent to call"):
			name = dataframe.loc[i, "Name"]
			phone = dataframe.loc[i, "Phone"]
			rmessage = dataframe.loc[i, "Last recieved message"]
			smessage = dataframe.loc[i, "Last sent message"]

			# add them to a list
			my_list = [name, phone, smessage, rmessage]
			send_list.append(my_list)

			# change the status of the leads from "Sent to call" to "Done"
			dataframe.at[i, "Status"] = "Done"
			continue

	print(send_list)
	print(dataframe)

	# Send the list in an email
	# Send email only if list of not empty
	if send_list == []:
		print("The send_list is empty.")
	else:
		send_15_min_stats(date, send_list)

	# Update the Database
	#update_sheets_database(dataframe)


