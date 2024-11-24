import unittest
from datetime import date

from dvrd_pydate.enums import ModifyKey
from dvrd_pydate.pydate import PYDate


class TestPYDate(unittest.TestCase):
    def setUp(self):
        self.test_date = PYDate(2023, 1, 15)

    def test_constructors(self):
        self.assertEqual(PYDate.from_value("2023-01-15"), date(2023, 1, 15))
        self.assertEqual(PYDate.from_value(), date.today())

    def test_add_operations(self):
        test_date = PYDate(2023, 1, 15)

        # Test adding years
        date_copy = PYDate.from_value(test_date).add(value=1, key=ModifyKey.YEAR)
        self.assertEqual(date(2024, 1, 15), date_copy)

        # Test adding months
        date_copy = PYDate.from_value(test_date).add(value=2, key=ModifyKey.MONTHS)
        self.assertEqual(date_copy, date(2023, 3, 15))

        # Test adding weeks
        date_copy = PYDate.from_value(test_date).add(value=1, key=ModifyKey.WEEKS)
        self.assertEqual(date_copy, date(2023, 1, 22))

        # Test adding days
        date_copy = PYDate.from_value(test_date).add(value=5, key=ModifyKey.DAYS)
        self.assertEqual(date_copy, date(2023, 1, 20))

        self.assertRaises(KeyError, date_copy.add, value=5, key=ModifyKey.HOURS)

    def test_add_overflow_operations(self):
        test_date = PYDate.from_value('2023-12-31')

        # Test adding years
        date_copy = test_date.clone().add(value=1, key=ModifyKey.YEAR)
        self.assertEqual(date_copy, date(2024, 12, 31))

        date_copy = test_date.clone().add_year()
        self.assertEqual(date_copy, date(2024, 12, 31))

        # Test adding months
        date_copy = test_date.clone().add(value=1, key=ModifyKey.MONTH)
        self.assertEqual(date_copy, date(2024, 1, 31))

        date_copy = test_date.clone().add_month()
        self.assertEqual(date_copy, date(2024, 1, 31))

        # Test adding month to less max days
        date_copy = PYDate.from_value('2023-03-31').add(value=1, key=ModifyKey.MONTH)
        self.assertEqual(date_copy, date(2023, 4, 30))

        date_copy = PYDate.from_value('2023-03-31').add_month()
        self.assertEqual(date_copy, date(2023, 4, 30))

        # Test adding weeks
        date_copy = test_date.clone().add(value=1, key=ModifyKey.WEEK)
        self.assertEqual(date_copy, date(2024, 1, 7))

        date_copy = test_date.clone().add_week()
        self.assertEqual(date_copy, date(2024, 1, 7))

        # Test adding days
        date_copy = test_date.clone().add(value=1, key=ModifyKey.DAY)
        self.assertEqual(date_copy, date(2024, 1, 1))

        date_copy = test_date.clone().add_day()
        self.assertEqual(date_copy, date(2024, 1, 1))

    def test_subtract_operations(self):
        # Test subtracting years
        test_date = PYDate(2023, 1, 15)

        date_copy = PYDate.from_value(test_date).subtract(value=1, key=ModifyKey.YEAR)
        self.assertEqual(date_copy, date(2022, 1, 15))

        date_copy = PYDate.from_value(test_date).subtract_year()
        self.assertEqual(date_copy, date(2022, 1, 15))

        # Test subtracting months
        date_copy = PYDate.from_value(test_date).subtract(value=2, key=ModifyKey.MONTHS)
        self.assertEqual(date(2022, 11, 15), date_copy)

        date_copy = PYDate.from_value(test_date).subtract_month()
        self.assertEqual(date_copy, date(2022, 12, 15))

        # Test subtracting 37 in months
        date_copy = PYDate.from_value(test_date).subtract(value=37, key=ModifyKey.MONTHS)
        self.assertEqual(date_copy, date(2019, 12, 15))

        # Test subtracting weeks
        date_copy = PYDate.from_value(test_date).subtract(value=1, key=ModifyKey.WEEK)
        self.assertEqual(date_copy, date(2023, 1, 8))

        date_copy = PYDate.from_value(test_date).subtract_week()
        self.assertEqual(date_copy, date(2023, 1, 8))

        # Test subtracting days
        date_copy = PYDate.from_value(test_date).subtract(value=1, key=ModifyKey.DAY)
        self.assertEqual(date(2023, 1, 14), date_copy)

        date_copy = PYDate.from_value(test_date).subtract_day()
        self.assertEqual(date(2023, 1, 14), date_copy)

        self.assertRaises(KeyError, date_copy.subtract, value=5, key=ModifyKey.HOURS)

    def test_subtract_overflow_operations(self):
        test_date = PYDate.from_value('2023-01-31')

        # Test subtracting years
        date_copy = test_date.clone().subtract(value=1, key=ModifyKey.YEAR)
        self.assertEqual(date(2022, 1, 31), date_copy)

        # Test subtracting months
        date_copy = test_date.clone().subtract(value=1, key=ModifyKey.MONTH)
        self.assertEqual(date(2022, 12, 31), date_copy)

        # Test subtracting months to less max days
        date_copy = PYDate.from_value('2023-07-31').subtract(value=1, key=ModifyKey.MONTH)
        self.assertEqual(date(2023, 6, 30), date_copy)

    def test_clone(self):
        cloned = self.test_date.clone()
        self.assertEqual(cloned, self.test_date)
        self.assertIsNot(cloned, self.test_date)


if __name__ == '__main__':
    unittest.main()
