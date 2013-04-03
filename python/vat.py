#! /usr/bin/python

tax_d = {	"Belgium" : 0.21,
		"Bulgaria" : 0.20,
		"Czech Republic" : 0.20,
		"Denmark" : 0.25	
	}

def calculate(area, price):
	return price * (1 + tax_d[area])

if __name__ == "__main__":
	total = calculate("Belgium", 100)
	print total
	
