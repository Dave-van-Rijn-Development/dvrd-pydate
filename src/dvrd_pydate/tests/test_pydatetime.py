import unittest
from datetime import datetime, timedelta

from dvrd_pydate.enums import ModifyKey
from dvrd_pydate.pydatetime import PYDateTime


class TestPYDateTime(unittest.TestCase):
    def setUp(self):
        self.test_date = datetime(2023, 1, 1, 12, 30, 45, 123456)
        self.py_datetime = PYDateTime.from_value(self.test_date)

    def test_initialization(self):
        self.assertEqual(PYDateTime.from_value(self.test_date), self.test_date)
        self.assertEqual(PYDateTime.from_value('2023-01-01 00:00:00.000'), datetime(2023, 1, 1, 0, 0, 0, 0))
        now = datetime.now()
        self.assertTrue((PYDateTime.from_value() - now).total_seconds() < 1)

    def test_add_methods(self):
        # Test adding hours
        result = self.py_datetime.clone().add(value=2, key=ModifyKey.HOURS)
        expected = self.test_date + timedelta(hours=2)
        self.assertEqual(expected, result)

        result = self.py_datetime.clone().add_hour()
        expected = self.test_date + timedelta(hours=1)
        self.assertEqual(expected, result)

        # Test adding minutes
        result = self.py_datetime.clone().add(value=30, key=ModifyKey.MINUTES)
        expected = self.test_date + timedelta(minutes=30)
        self.assertEqual(expected, result)

        result = self.py_datetime.clone().add_minute()
        expected = self.test_date + timedelta(minutes=1)
        self.assertEqual(expected, result)

        # Test adding seconds
        result = self.py_datetime.clone().add(value=30, key=ModifyKey.SECOND)
        expected = self.test_date + timedelta(seconds=30)
        self.assertEqual(expected, result)

        result = self.py_datetime.clone().add_second()
        expected = self.test_date + timedelta(seconds=1)
        self.assertEqual(expected, result)

        # Test adding microseconds
        result = self.py_datetime.clone().add(value=30, key=ModifyKey.MICROSECOND)
        expected = self.test_date + timedelta(microseconds=30)
        self.assertEqual(expected, result)

        result = self.py_datetime.clone().add_microsecond()
        expected = self.test_date + timedelta(microseconds=1)
        self.assertEqual(expected, result)

        self.assertRaises(KeyError, self.py_datetime.add, value=30, key='not_a_key')

    def test_subtract_methods(self):
        # Test subtracting hours
        result = self.py_datetime.clone().subtract(value=2, key=ModifyKey.HOURS)
        expected = self.test_date - timedelta(hours=2)
        self.assertEqual(result, expected)

        result = self.py_datetime.clone().subtract_hour()
        expected = self.test_date - timedelta(hours=1)
        self.assertEqual(result, expected)

        # Test subtracting minutes
        result = self.py_datetime.clone().subtract(value=30, key=ModifyKey.MINUTES)
        expected = self.test_date - timedelta(minutes=30)
        self.assertEqual(result, expected)

        result = self.py_datetime.clone().subtract_minute()
        expected = self.test_date - timedelta(minutes=1)
        self.assertEqual(result, expected)

        # Test subtracting seconds
        result = self.py_datetime.clone().subtract(value=30, key=ModifyKey.SECOND)
        expected = self.test_date - timedelta(seconds=30)
        self.assertEqual(result, expected)

        result = self.py_datetime.clone().subtract_second()
        expected = self.test_date - timedelta(seconds=1)
        self.assertEqual(result, expected)

        # Test subtracting microseconds
        result = self.py_datetime.clone().subtract(value=30, key=ModifyKey.MICROSECOND)
        expected = self.test_date - timedelta(microseconds=30)
        self.assertEqual(result, expected)

        result = self.py_datetime.clone().subtract_microsecond()
        expected = self.test_date - timedelta(microseconds=1)
        self.assertEqual(result, expected)

        self.assertRaises(KeyError, self.py_datetime.subtract, value=30, key='not_a_key')

    def test_clone(self):
        clone = self.py_datetime.clone()
        self.assertEqual(clone, self.py_datetime)
        self.assertIsNot(clone, self.py_datetime)


if __name__ == '__main__':
    unittest.main()
