#imports
import pandas as pd
from date_counter import today_date, yesterday_date, yester, RA1date, RA2date, waiting_date
from googlefiles import trail_read, update_info_sheet, update_sheets_database
from email_notifier import send_yesterday_stats


# Check if any leads qualify for past messages
def check_past(dataframe, RA1date, RA2date, waiting_date):
	'''
		This function checks the number which have been contacted in the past
		which are eligible to be contacted today

		returns : integer
	'''
	old_messages = 0
	for i in range(len(dataframe)):
		if ((dataframe.loc[i, "In Stage"] == "Reactivation 1" and dataframe.loc[i, "Contacted On"] == RA1date) 
		or (dataframe.loc[i, "In Stage"] == "Reactivation 2" and dataframe.loc[i, "Contacted On"] == RA2date) 
		or (dataframe.loc[i, "Status"] == "Waiting" and dataframe.loc[i, "Contacted On"] == waiting_date)):
			
			# print(dataframe.loc[i])
			old_messages += 1

	return old_messages


def set_status_today(dataframe, RA1Date, RA2Date, waiting_date, new_today):
	'''
		This function sets the status of the old messages which can be contacted today
		as 'TODAY'.
		It also set the status of leads to be contacted as 'TODAY' 

		returns: NONE
	'''
	for i in range(len(dataframe)):
		if ((dataframe.loc[i, "In Stage"] == "Reactivation 1" and dataframe.loc[i, "Contacted On"] == RA1date) 
		or (dataframe.loc[i, "In Stage"] == "Reactivation 2" and dataframe.loc[i, "Contacted On"] == RA2date) 
		or (dataframe.loc[i, "Status"] == "Waiting" and dataframe.loc[i, "Contacted On"] == waiting_date)):

			dataframe.loc[i, "Status"] = "TODAY"

	for i in range(0, new_today):
		if (i == len(dataframe)):
			break
		
		if(dataframe.loc[i, "Status"] == "To Contact"):
			# print("inside .loc")
			dataframe.at[i, "Status"] = "TODAY"
		
	update_sheets_database(dataframe)



# Send email about previous day stats
def get_yesterday_stats(dataframe, yesterday_date):
	'''
		This funtion gets the status of the dabase right now 
		returns : integers
	'''
	to_contact = 0
	contacted_yesterday = 0
	waiting_contacts = 0

	for i in range(len(dataframe)):
		if (dataframe.loc[i, "Status"] == "To Contact"):
			to_contact += 1

		if (dataframe.loc[i, "Contacted On"] == yesterday_date):
			contacted_yesterday += 1

		if (dataframe.loc[i, "Status"] == "Waiting"):
			waiting_contacts += 1

	return to_contact, contacted_yesterday, waiting_contacts


if __name__ == '__main__':
	# get data from sheets
	dataframe = get_database()
	print("Got data from sheets")

	# set all the important dates
	today = today_date()
	yesterday = yesterday_date()
	RA1date = RA1date()
	RA2date = RA2date()
	waiting_date = waiting_date()

	# Check past messages 
	past_messages = check_past(dataframe, RA1date, RA2date, waiting_date)
	new_today = 750 - past_messages
	print(f"Checked past eligible messages: {past_messages}")

	# Send email about yesterdays stats
	x, y, z = get_yesterday_stats(dataframe, yesterday)
	w = new_today
	yester = yester()
	send_yesterday_stats(yester, x, y, z, w)

	# Save INFO
	update_info_sheet(new_today, 150)
	print("Saved to INFO sheet")

	# Sets today status
	set_status_today(dataframe, RA1date, RA2date, waiting_date, new_today)
	print("Updated today's contacts")
	print("Completed everyday.py")
