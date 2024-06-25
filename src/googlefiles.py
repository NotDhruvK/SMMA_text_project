import gspread
from google.oauth2.service_account import Credentials
import pygsheets
import pandas as pd


def return_client():
	'''
		Authenticates the client based on 'Credential.json'
		returns: A client object
	'''
	scopes = [
		"https://www.googleapis.com/auth/spreadsheets"
	]

	creds = Credentials.from_service_account_file("credentials.json", scopes = scopes)
	client = gspread.authorize(creds)
	return client


def get_database():
    '''
    Gets the CSV format of a Google Sheet
    returns : A pandas dataframe
    '''
    sheet_id = "1x7n58Z01pAjaNtOvYg3qOsWOLDrfDg9358Efv6Kwaok"
    df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv")
    dataframe = df.dropna(axis=0, how='all')
    
    # Convert the "Phone" series to strings with the desired format
    if 'Phone' in dataframe.columns:
        dataframe['Phone'] = dataframe['Phone'].apply(lambda x: str(int(x)) if pd.notna(x) else '')

    return dataframe


# The big daddy function to update the complete database
def update_sheets_database(df):
	'''
		Updates the google sheet with the set sheet id with the Pandas dataframe that is passed in
		returns : NONE
	'''
	sheet_id = "1x7n58Z01pAjaNtOvYg3qOsWOLDrfDg9358Efv6Kwaok"
	gc = pygsheets.authorize(service_file='credentials.json')

	#open the google spreadsheet 
	sh = gc.open_by_key(sheet_id)

	#select the first sheet 
	wks = sh[0]

	#update the first sheet with df, starting at cell B2. 
	wks.set_dataframe(df, 'A1')
	print("Updated the main database")


#Make a function to write to sheet
def update_info_sheet(new_contacts, hourly_rate):
	'''
		Updates a set sheet(INFO) in a google sheet workbook
		returns : NONE
	'''
	client = return_client()
	sheet_id = "1x7n58Z01pAjaNtOvYg3qOsWOLDrfDg9358Efv6Kwaok"
	workbook = client.open_by_key(sheet_id)

	# Select Sheet 2
	info_sheet = workbook.worksheet("INFO")

	# Update the values
	info_sheet.update_cell(2, 1, f"{new_contacts}")
	info_sheet.update_cell(2, 3, f"{hourly_rate}")
	print("Updated the INFO sheet")


# Returns the set value in a cell C2 of the google sheet
def get_hourly_rate():
	client = return_client()
	sheet_id = "1x7n58Z01pAjaNtOvYg3qOsWOLDrfDg9358Efv6Kwaok"
	workbook = client.open_by_key(sheet_id)

	# Select Sheet 2
	info_sheet = workbook.worksheet("INFO")

	# Get the rate
	value = info_sheet.acell("C2").value
	print(f"Getting the hourly message rate: {value}")
	return value


def get_today_new_contacts():
	client = return_client()
	sheet_id = "1x7n58Z01pAjaNtOvYg3qOsWOLDrfDg9358Efv6Kwaok"
	workbook = client.open_by_key(sheet_id)

	# Select Sheet 2
	info_sheet = workbook.worksheet("INFO")

	# Get the rate
	value = info_sheet.acell("A2").value
	print(f"Getting today's new contacts: {value}")
	return value


def get_sms_segments():
	client = return_client()
	sheet_id = "1x7n58Z01pAjaNtOvYg3qOsWOLDrfDg9358Efv6Kwaok"
	workbook = client.open_by_key(sheet_id)

	# Select Sheet 2
	info_sheet = workbook.worksheet("INFO")

	# Get the rate
	value = info_sheet.acell("E2").value
	print("Getting SMS segments")
	return value


def set_sms_segments(value):
	client = return_client()
	sheet_id = "1x7n58Z01pAjaNtOvYg3qOsWOLDrfDg9358Efv6Kwaok"
	workbook = client.open_by_key(sheet_id)

	# Select Sheet 2
	info_sheet = workbook.worksheet("INFO")

	# Setting the value
	info_sheet.update_cell(2, 5, f"{value}")
	print(f"SMS segments updated as: {value}")


# Write a function to change one cell of the dataframe
def change_one_cell(contact, body):
	'''
		This function will first get a single row of the database, 
		Change the values and then push to the database
		It will also update the Status, Contacted on, Last recieved message and first and second positive values

		returns : None
	'''
	pass 


# if __name__ == "__main__":
