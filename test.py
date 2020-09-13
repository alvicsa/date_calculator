import unittest
from datetime import datetime, timedelta
from packages.utility import Date, day_difference


class TestMain(unittest.TestCase):
    """Tests for 'day_difference' function."""

    def test_datediff1(self):
        test_date_first = "02/06/1983"
        test_date_second = "22/06/1983"

        # Unpack user input into day, month and year separated by "/"
        first_d, first_m, first_y = test_date_first.split(sep='/')
        second_d, second_m, second_y = test_date_second.split(sep='/')

        # Create Date objects from the Date Class and convert inputs into integers
        date_f = Date(int(first_d), int(first_m), int(first_y))
        date_s = Date(int(second_d), int(second_m), int(second_y))

        result = day_difference(date_f, date_s)
        self.assertEqual(result, 19)

    def test_datediff2(self):
        test_date_first = "04/07/1984"
        test_date_second = "25/12/1984"

        # Unpack user input into day, month and year separated by "/"
        first_d, first_m, first_y = test_date_first.split(sep='/')
        second_d, second_m, second_y = test_date_second.split(sep='/')

        # Create Date objects from the Date Class and convert inputs into integers
        date_f = Date(int(first_d), int(first_m), int(first_y))
        date_s = Date(int(second_d), int(second_m), int(second_y))

        result = day_difference(date_f, date_s)
        self.assertEqual(result, 173)

    def test_datediff3(self):
        test_date_first = "03/01/1989"
        test_date_second = "03/08/1983"

        # Unpack user input into day, month and year separated by "/"
        first_d, first_m, first_y = test_date_first.split(sep='/')
        second_d, second_m, second_y = test_date_second.split(sep='/')

        # Create Date objects from the Date Class and convert inputs into integers
        date_f = Date(int(first_d), int(first_m), int(first_y))
        date_s = Date(int(second_d), int(second_m), int(second_y))

        result = day_difference(date_f, date_s)
        self.assertEqual(result, 1979)

    def test_datediff4(self):
        test_date_first = "03/01/1901"
        test_date_second = "03/08/2999"

        # Unpack user input into day, month and year separated by "/"
        first_d, first_m, first_y = test_date_first.split(sep='/')
        second_d, second_m, second_y = test_date_second.split(sep='/')

        # Create Date objects from the Date Class and convert inputs into integers
        date_f = Date(int(first_d), int(first_m), int(first_y))
        date_s = Date(int(second_d), int(second_m), int(second_y))

        date_format = "%d/%m/%Y"
        a = datetime.strptime(test_date_first, date_format)
        b = datetime.strptime(test_date_second, date_format)
        delta = b - a

        result = day_difference(date_f, date_s)
        self.assertEqual(result, abs(delta.days)-1)


if __name__ == '__main__':
    unittest.main()
