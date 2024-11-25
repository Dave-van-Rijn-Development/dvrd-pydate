import unittest
from datetime import datetime, timedelta, date

from dvrd_pydate.enums import DatePart, TimePart
from dvrd_pydate.pydatetime import PyDateTime


class TestPyDateTime(unittest.TestCase):
    def setUp(self):
        self.test_date = datetime(2023, 1, 1, 12, 30, 45, 123456)
        self.py_datetime = PyDateTime.from_value(self.test_date)

    def test_initialization(self):
        self.assertEqual(PyDateTime.from_value(self.test_date), self.test_date)
        self.assertEqual(PyDateTime.from_value('2023-01-01 00:00:00.000'), datetime(2023, 1, 1, 0, 0, 0, 0))
        now = datetime.now()
        self.assertTrue((PyDateTime.from_value() - now).total_seconds() < 1)

    def test_add_methods(self):
        # Test adding hours
        result = self.py_datetime.clone().add(value=2, key=TimePart.HOURS)
        expected = self.test_date + timedelta(hours=2)
        self.assertEqual(expected, result)

        result = self.py_datetime.clone().add_hour()
        expected = self.test_date + timedelta(hours=1)
        self.assertEqual(expected, result)

        # Test adding minutes
        result = self.py_datetime.clone().add(value=30, key=TimePart.MINUTES)
        expected = self.test_date + timedelta(minutes=30)
        self.assertEqual(expected, result)

        result = self.py_datetime.clone().add_minute()
        expected = self.test_date + timedelta(minutes=1)
        self.assertEqual(expected, result)

        # Test adding seconds
        result = self.py_datetime.clone().add(value=30, key=TimePart.SECOND)
        expected = self.test_date + timedelta(seconds=30)
        self.assertEqual(expected, result)

        result = self.py_datetime.clone().add_second()
        expected = self.test_date + timedelta(seconds=1)
        self.assertEqual(expected, result)

        # Test adding microseconds
        result = self.py_datetime.clone().add(value=30, key=TimePart.MICROSECOND)
        expected = self.test_date + timedelta(microseconds=30)
        self.assertEqual(expected, result)

        result = self.py_datetime.clone().add_microsecond()
        expected = self.test_date + timedelta(microseconds=1)
        self.assertEqual(expected, result)

        self.assertRaises(KeyError, self.py_datetime.add, value=30, key='not_a_part')

    def test_subtract_methods(self):
        # Test subtracting date part
        result = self.py_datetime.clone().subtract(value=1, key=DatePart.DAY)
        expected = self.test_date - timedelta(days=1)
        self.assertEqual(result, expected)

        # Test subtracting hours
        result = self.py_datetime.clone().subtract(value=2, key=TimePart.HOURS)
        expected = self.test_date - timedelta(hours=2)
        self.assertEqual(result, expected)

        result = self.py_datetime.clone().subtract_hour()
        expected = self.test_date - timedelta(hours=1)
        self.assertEqual(result, expected)

        # Test subtracting minutes
        result = self.py_datetime.clone().subtract(value=30, key=TimePart.MINUTES)
        expected = self.test_date - timedelta(minutes=30)
        self.assertEqual(result, expected)

        result = self.py_datetime.clone().subtract_minute()
        expected = self.test_date - timedelta(minutes=1)
        self.assertEqual(result, expected)

        # Test subtracting seconds
        result = self.py_datetime.clone().subtract(value=30, key=TimePart.SECOND)
        expected = self.test_date - timedelta(seconds=30)
        self.assertEqual(result, expected)

        result = self.py_datetime.clone().subtract_second()
        expected = self.test_date - timedelta(seconds=1)
        self.assertEqual(result, expected)

        # Test subtracting microseconds
        result = self.py_datetime.clone().subtract(value=30, key=TimePart.MICROSECOND)
        expected = self.test_date - timedelta(microseconds=30)
        self.assertEqual(result, expected)

        result = self.py_datetime.clone().subtract_microsecond()
        expected = self.test_date - timedelta(microseconds=1)
        self.assertEqual(result, expected)

        self.assertRaises(KeyError, self.py_datetime.subtract, value=30, key='not_a_part')

    def test_clone(self):
        clone = self.py_datetime.clone()
        self.assertEqual(clone, self.py_datetime)
        self.assertIsNot(clone, self.py_datetime)

    def test_iter(self):
        # Default iter, with end date
        expect_date = datetime.now()
        end = PyDateTime.from_value(expect_date).add(value=1, key=DatePart.MONTHS)
        for value in PyDateTime.iter(end=end):
            self.assertTrue((value - expect_date).total_seconds() < 1)
            expect_date += timedelta(days=1)

        start = datetime(2024, 1, 1, 0, 0, 0, 0)
        end = datetime(2024, 1, 31, 0, 0, 0, 0)
        expect_date = datetime(2024, 1, 1, 0, 0, 0, 0)
        for value in PyDateTime.iter(start=start, end=end):
            self.assertEqual(expect_date, value)
            expect_date += timedelta(days=1)

        start = datetime(2024, 1, 1, 0, 0, 0, 0)
        end = datetime(2024, 1, 31, 0, 0, 0, 0)
        expect_date = datetime(2024, 1, 1, 0, 0, 0, 0)
        for value in PyDateTime.iter(start=start, end=end, step=(2, DatePart.DAYS)):
            self.assertEqual(expect_date, value)
            expect_date += timedelta(days=2)

        start = datetime(2024, 1, 1, 0, 0, 0, 0)
        end = datetime(2024, 1, 31, 0, 0, 0, 0)
        expect_date = datetime(2024, 1, 1, 0, 0, 0, 0)
        for value in PyDateTime.iter(start=start, end=end, step=(1, TimePart.HOUR)):
            self.assertEqual(expect_date, value)
            expect_date += timedelta(hours=1)

        start = datetime(2024, 1, 1, 0, 0, 0, 0)
        end = datetime(2024, 1, 31, 0, 0, 0, 0)
        expect_date = datetime(2024, 1, 1, 0, 0, 0, 0)
        for value in PyDateTime.iter(start=start, end=end, step=(2, TimePart.MINUTE)):
            self.assertEqual(expect_date, value)
            expect_date += timedelta(minutes=2)

    def test_start_of(self):
        now = datetime.now()
        start_of = PyDateTime.from_value(now)

        # Date part
        expected = now.replace(month=1, day=1)
        self.assertEqual(expected, start_of.start_of(DatePart.YEAR))

        # Day
        expected = datetime.combine(date.today(), datetime.min.time())
        self.assertEqual(expected, start_of.start_of(DatePart.DAY))

        # Hour
        expected = now.replace(minute=0, second=0, microsecond=0)
        self.assertEqual(expected, start_of.start_of(TimePart.HOUR))

        # Minute
        expected = now.replace(second=0, microsecond=0)
        self.assertEqual(expected, start_of.start_of(TimePart.MINUTE))

        # Second
        expected = now.replace(microsecond=0)
        self.assertEqual(expected, start_of.start_of(TimePart.SECOND))

        self.assertIs(start_of, start_of.start_of(TimePart.MICROSECONDS))
        self.assertRaises(KeyError, start_of.start_of, 'not_a_part')

    def test_end_of(self):
        now = datetime.now()
        end_of = PyDateTime.from_value(now)

        # Date part
        expected = now.replace(month=12, day=31)
        self.assertEqual(expected, end_of.end_of(DatePart.YEAR))

        # Day
        expected = now.replace(hour=23, minute=59, second=59, microsecond=999)
        self.assertEqual(expected, end_of.end_of(DatePart.DAY))

        # Hour
        expected = now.replace(minute=59, second=59, microsecond=999)
        self.assertEqual(expected, end_of.end_of(TimePart.HOUR))

        # Minute
        expected = now.replace(second=59, microsecond=999)
        self.assertEqual(expected, end_of.end_of(TimePart.MINUTE))

        # Second
        expected = now.replace(microsecond=999)
        self.assertEqual(expected, end_of.end_of(TimePart.SECOND))

        self.assertIs(end_of, end_of.end_of(TimePart.MICROSECONDS))
        self.assertRaises(KeyError, end_of.end_of, 'not_a_part')


if __name__ == '__main__':
    unittest.main()
