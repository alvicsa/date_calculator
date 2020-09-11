'''This program calculates the number of full days elapsed in between two events'''

# Stage 1: Creating Classes and Functions
# Create a Date Class


class Date:
    def __init__(self, d, m, y):
        self.d = d
        self.m = m
        self.y = y


# Fuction for counting number of Leap Years
def count_leap_years(d):

    years = d.y

    # Checking if current year needs to be included
    if (d.m <= 2):
        years -= 1

    # Calculate total number of Leap Years
    return int(years / 4 - years / 100 + years / 400)


# Function for calculating number of days between two dates
def day_difference(dt1, dt2):

    # List number of days in each month for non-leap years
    month_days = 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31

    # Count number of days between 01/01/1901 and specified first_date

    # initialize count using years and day
    n1 = dt1.y * 365 + dt1.d

    # Add days for months in given date
    for i in range(0, dt1.m - 1):
        n1 += month_days[i]

    # Since every leap year is of 366 days,
    # Add a day for every leap year
    n1 += count_leap_years(dt1)

    # Count number of days between 01/01/1901 and specified second_date

    n2 = dt2.y * 365 + dt2.d
    for i in range(0, dt2.m - 1):
        n2 += month_days[i]
    n2 += count_leap_years(dt2)

    # return difference between two counts
    return abs(n2 - n1) - 1


# Stage 2: User interaction
if __name__ == '__main__':

    while True:
        # Prompt the user for data filename and return the processed dataframe
        first_date = input(
            'Please enter First Date using the DD/MM/YYYY format: ')
        second_date = input(
            'Please enter Second Date using the DD/MM/YYYY format: ')

        # Unpack user input into day, month and year separated by "/"
        first_d, first_m, first_y = first_date.split(sep='/')
        second_d, second_m, second_y = second_date.split(sep='/')

        # Create Date objects from the Date Class and convert inputs into integers
        date_f = Date(int(first_d), int(first_m), int(first_y))
        date_s = Date(int(second_d), int(second_m), int(second_y))

        if 2999 > date_f.y < 1901 or 2999 > date_s.y < 1901:
            print("Dates must be between 01/01/1901 and 31/12/2999. Try again!")
        else:
            # Print resulting date difference
            print(f'{first_date} - {second_date} =',
                  day_difference(date_f, date_s), "days")
            break
