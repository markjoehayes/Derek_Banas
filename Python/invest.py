#!/usr/bin/python3

# Have the user enter their investment amount and expected interest
# Each year their investment will increase by their investment + invesrment * rate
# Print out earnings after ten years

def calc_earnings(investment, rate, years):
	for i in range(years):
		investment += (investment * (rate/100))
	return investment


def main():
	investment = int(input("Please Enter your investment amount: "))
	rate = float(input("Please enter your interest rate: "))
	years = int(input("How many years? "))
	investment = calc_earnings(investment, rate, years)

	print(f"Earnings aftre ten years = {investment:.2f}")
	
main()
