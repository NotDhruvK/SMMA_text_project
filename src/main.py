from csv_handler import read_csv, write_csv
from twilio_client import send_message
from message_handler import handle_incoming_message
from email_notifier import send_daily_summary
from scheduler import schedule_tasks


def main():
    # Load contacts
    contacts = read_csv('data/contacts.csv')

    # Process contacts and send messages
    for index, contact in contacts.iterrows():
        # Logic to determine message
        message = "Your custom message here"
        send_message(contact['contact_number'], message)

    # Handle responses and update CSVs
    handle_incoming_message()

    # Send daily summary
    send_daily_summary()


if __name__ == "__main__":
    schedule_tasks(main)