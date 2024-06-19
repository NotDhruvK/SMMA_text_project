import gspread
from google.oauth2.service_account import Credentials
import pygsheets
import pandas


def return_client():
	scopes = [
		"https://www.googleapis.com/auth/spreadsheets"
	]

	creds = Credentials.from_service_account_file("credentials.json", scopes = scopes)
	client = gspread.authorize(creds)
	return client


# Returns a pandas database object
def trail_read():
	sheet_id = "1x7n58Z01pAjaNtOvYg3qOsWOLDrfDg9358Efv6Kwaok"
	df = pandas.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv")
	return df


# The big daddy function to update the complete database
def update_sheets_database(df):
	sheet_id = "1x7n58Z01pAjaNtOvYg3qOsWOLDrfDg9358Efv6Kwaok"
	gc = pygsheets.authorize(service_file='credentials.json')

	#open the google spreadsheet 
	sh = gc.open_by_key(sheet_id)

	#select the first sheet 
	wks = sh[0]

	#update the first sheet with df, starting at cell B2. 
	wks.set_dataframe(df, 'A1')


#Make a function to write to sheet
def update_info_sheet(new_contacts, hourly_rate):
	client = return_client()
	sheet_id = "1x7n58Z01pAjaNtOvYg3qOsWOLDrfDg9358Efv6Kwaok"
	workbook = client.open_by_key(sheet_id)

	# Select Sheet 2
	info_sheet = workbook.worksheet("INFO")

	# Update the values
	info_sheet.update_cell(2, 1, f"{new_contacts}")
	info_sheet.update_cell(2, 3, f"{hourly_rate}")


# Returns the set value in a cell C2 of the google sheet
def get_hourly_rate():
	client = return_client()
	sheet_id = "1x7n58Z01pAjaNtOvYg3qOsWOLDrfDg9358Efv6Kwaok"
	workbook = client.open_by_key(sheet_id)

	# Select Sheet 2
	info_sheet = workbook.worksheet("INFO")

	# Get the rate
	value = info_sheet.acell("C2").value
	return value


def get_today_new_contacts():
	client = return_client()
	sheet_id = "1x7n58Z01pAjaNtOvYg3qOsWOLDrfDg9358Efv6Kwaok"
	workbook = client.open_by_key(sheet_id)

	# Select Sheet 2
	info_sheet = workbook.worksheet("INFO")

	# Get the rate
	value = info_sheet.acell("A2").value
	return value

# if __name__ == "__main__":