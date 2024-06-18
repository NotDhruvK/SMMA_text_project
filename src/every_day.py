#imports
import pandas as pd
from date_counter import today_date, RA1date, RA2date, waiting_date
from googlefiles import trail_read, update_sheets_database

# Calculate number of messages per day = RA1 + RA2 + NEW = 750
#	Basically get the number of new contacts to use. Save to INFO sheet
def daily_new_messages(RA1date, RA2date):
	dataframe = trail_read()
	dataframe = dataframe.dropna(axis=0, how='all')

	
			
    	
# Calculate the number of messages per hour -> Save that to INFO sheet


# Check if any leads qualify for past messages
def check_past(dataframe, RA1date, RA2date, waiting_date):
	old_messages = 0
	for i in range(len(dataframe)):
		if ((dataframe.loc[i, "In Campaign"] == "Reactivation 1" and dataframe.loc[i, "Contacted On"] == RA1date) 
		or (dataframe.loc[i, "In Campaign"] == "Reactivation 2" and dataframe.loc[i, "Contacted On"] == RA2date) 
		or (dataframe.loc[i, "Status"] == "Waiting" and dataframe.loc[i, "Contacted On"] == waiting_date)):
			
			# print(dataframe.loc[i])
			old_messages = old_messages + 1

	return old_messages		


# Send email about previous day stats

if __name__ == '__main__':
	dataframe = trail_read().dropna(axis=0, how='all')

	today = today_date()
	RA1date = RA1date()
	RA2date = RA2date()
	waiting_date = waiting_date()

	# print(today, RA1date, RA2date, waiting_date)
	past_messages = check_past(dataframe, RA1date, RA2date, waiting_date)

	daily_new_messages(RA1date, RA2date)