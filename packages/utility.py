# Create a Date Class
class Date:
    '''
    Date class is used to assign day, month and year as attributes to the Date object
    '''

    def __init__(self, d, m, y):
        self.d = d
        self.m = m
        self.y = y


# Fuction for counting number of Leap Years
def count_leap_years(d):
    '''
    Counts the number of Leap Years for each Date Object
    '''
    years = d.y

    # Checking if current year needs to be included
    if (d.m <= 2):
        years -= 1

    # Calculate total number of Leap Years
    return int(years / 4 - years / 100 + years / 400)


# Function for calculating number of days between two dates
def day_difference(dt1, dt2):
    '''
    Calculates a number of full days elapsed between two Date Objects
    '''
    try:
        

        # List number of days in each month for non-leap years
        month_days = 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31

        # Check that valid days are being entered
        if (0 < dt1.d <= month_days[dt1.m -1]) and (0 < dt2.d <= month_days[dt2.m - 1]):

            # Count number of days between 01/01/1901 and specified first_date
            # initialize count using years and days
            n1 = dt1.y * 365 + dt1.d

            # Add days for months in given date
            for i in range(0, dt1.m):
                n1 += month_days[i]

            # Since every leap year is of 366 days,
            # Add a day for every leap year
            n1 += count_leap_years(dt1)

            # Count number of days between 01/01/1901 and specified second_date

            n2 = dt2.y * 365 + dt2.d
            for i in range(0, dt2.m):
                n2 += month_days[i]
            n2 += count_leap_years(dt2)
        
        else:
            raise ValueError

    except:
        return "Dates not valid"
    # return difference between two counts
    else:
        return abs(n2 - n1) - 1
