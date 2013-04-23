#!/usr/bin/python
import datetime
from datetime import timedelta

def test():
	date1 = timedelta(days = 60)
	d = datetime.date(2014, 4, 8)
	print d - date1

#param: YYYY-MM-DD
#return []

expiration_dates = []
def add_dates(e_d, ds):
	for d in ds:
		day = e_d - timedelta(days = d)
		expiration_dates.append(day.strftime("%Y-%m-%d"))

def get_date(expired_date, sub_len):
	e_d = datetime.datetime.strptime(expired_date, "%Y-%m-%d")
	add_dates(e_d, [1, 3, 7])
	if sub_len >= 91 :
		add_dates(e_d, [15, 30])
	if sub_len >= 180 :
		add_dates(e_d, [60])
	return expiration_dates


if __name__ == "__main__":
	get_date("2013-04-19", 31)
	print expiration_dates

	
	



