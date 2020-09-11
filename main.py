from packages.utility import Date, day_difference


# User interaction
if __name__ == '__main__':

    print("Enter 'q' at any time to quit.")
    while True:
        try:
            # Prompt the user for data filename and return the processed dataframe
            first_date = input('Please enter First Date using the DD/MM/YYYY format: ')
            if first_date == 'q':
                break
            second_date = input('Please enter Second Date using the DD/MM/YYYY format: ')
            if second_date == 'q':
                break

            # Unpack user input into day, month and year separated by "/"
            first_d, first_m, first_y = first_date.split(sep='/')
            second_d, second_m, second_y = second_date.split(sep='/')

            # Create Date objects from the Date Class and convert inputs into integers
            date_f = Date(int(first_d), int(first_m), int(first_y))
            date_s = Date(int(second_d), int(second_m), int(second_y))

            if not (1901 <= date_f.y <= 2999) or not (1901 <= date_s.y <= 2999):
                print("Dates must be between 01/01/1901 and 31/12/2999. Try again!")
                continue
        except:
            print("Make sure the dates are entered in the following format: DD/MM/YYYY")
        else:
            # Print resulting date difference
            if first_date == second_date:
                print("You entered the same First and Second dates.")
            else:
                print(f'\t{first_date} - {second_date} =', day_difference(date_f, date_s), "days")
            break
