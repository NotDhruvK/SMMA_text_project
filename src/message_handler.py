import pandas as pd
from csv_handler import read_csv, write_csv

'''
The total csv files would be as:
    contacts.csv - all the contacts contacted so far
    new.csv - the new contacts are to be added here everyday
    interested.csv  - These are the people in the pipeline who are interested and have replied
    tocall.csv - These are the people who are added to the call list
    reactivation1.csv - These are the people who replied once but didn't reply again
    reactivation2.csv - These are the people who haven't replied at all
    tosend.csv - These are the numbers which will be send vis email every 15 minutes
    removed.csv - These are the people who are removed from the pipeline for the time being
    deleted.csv - These are the people who are irrelevant to what is going on.

Hence the index numbers will be:
    tosend : 1
    interested: 2
    tocall : 3
    reactivation1 : 4
    reactivation2 : 5
    removed : 6
    deleted: 7

The lists which need to store incoming messages are:
    tosend.csv
    tocall.csv


'''

def handle_incoming_message():
    # Example implementation for handling incoming messages
    # This function should categorize contacts based on their responses
    # For now, this is just a placeholder function
    print("Handling incoming messages...")

    # Dummy logic to read and update CSV files
    contacts = read_csv('data/contacts.csv')
    interested = read_csv('data/interested.csv')
    after7day = read_csv('data/after7day.csv')
    not_interested = read_csv('data/not_interested.csv')

    # Simulate categorizing contacts (replace this with actual logic)
    for index, contact in contacts.iterrows():
        if index % 3 == 0:
            interested = interested.append(contact)
        elif index % 3 == 1:
            after7day = after7day.append(contact)
        else:
            not_interested = not_interested.append(contact)

    # Write updated CSV files
    write_csv(interested, 'data/interested.csv')
    write_csv(after7day, 'data/after7day.csv')
    write_csv(not_interested, 'data/not_interested.csv')

    print("Incoming messages handled.")
