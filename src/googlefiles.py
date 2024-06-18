import gspread
from google.oauth2.service_account import Credentials
import pygsheets
import pandas

scopes = [
	"https://www.googleapis.com/auth/spreadsheets"
]

creds = Credentials.from_service_account_file("credentials.json", scopes = scopes)
client = gspread.authorize(creds)

sheet_id = "1x7n58Z01pAjaNtOvYg3qOsWOLDrfDg9358Efv6Kwaok"
#sheet = client.open_by_key(sheet_id)

#values_list = sheet.sheet1.row_values(1)
#print(values_list)
def trail_read():
	sheet_id = "1x7n58Z01pAjaNtOvYg3qOsWOLDrfDg9358Efv6Kwaok"
	df = pandas.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv")
	return df


def update_sheets_database(df):
	gc = pygsheets.authorize(service_file='credentials.json')

	#open the google spreadsheet 
	sh = gc.open_by_key(sheet_id)

	#select the first sheet 
	wks = sh[0]

	#update the first sheet with df, starting at cell B2. 
	wks.set_dataframe(df, 'B2')

#Make a function to write to sheet

# Make a function to change sheets and return the new sheet

#if __name__ == "__main__":
#	trail_read()