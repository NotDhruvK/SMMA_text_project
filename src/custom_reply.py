import json
from twilio_client_sending import send_message


def process_contacts(file_path):
    # Step 1: Read the dictionary from the file
    with open(file_path, 'r') as file:
        contacts = json.load(file)

    # Step 2 and 3: Loop through the dictionary and call send_message
    for name, contact in contacts.items():
        # Create the f-string message
        message = f"""Hi {name}, Swam here from Cognicraft. We’re looking to partner up with ambitious practices keen on exponentially growing their revenue. Our Expert Program gets you 10-15+ new clients in the next 30-45 days guaranteed. Would that be something you might be interested in?"""
        
        # Call the send_message function
        send_message(contact, message)

# Example usage
file_path = 'contacts.json'  # Replace with your file path
process_contacts(file_path)


'''
The format of the JSON file.
{
    "Alice": "123-456-7890",
    "Bob": "987-654-3210"
}
'''