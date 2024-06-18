# This module contains the accessible functions to convert datetime objects into 
# string format

from datetime import datetime, timedelta

def today_date():
	today = datetime.today()
	date = today.strftime('%Y-%m-%d')
	return date


def RA1date():
	today = datetime.today()
	RA1date = today - timedelta(days=7)
	date = RA1date.strftime('%Y-%m-%d')
	return date


def RA2date():
	today = datetime.today()
	RA2date = today - timedelta(days=14)
	date = RA2date.strftime('%Y-%m-%d')
	return date


def waiting_date():
	today = datetime.today()
	waiting_date = today - timedelta(days=2)
	date = waiting_date.strftime('%Y-%m-%d')
	return date