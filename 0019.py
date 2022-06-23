from datetime import datetime

def main():
	date = datetime(1901, 1, 1)

	one_day = datetime(1, 1, 2) - datetime(1, 1, 1)
	first_month_sundays = 0
	while date < datetime(2000, 12, 31):
		if date.day == 1 and date.weekday() == 6:
			first_month_sundays += 1

		date += one_day

	print(first_month_sundays)

if __name__ == '__main__':
	main()

