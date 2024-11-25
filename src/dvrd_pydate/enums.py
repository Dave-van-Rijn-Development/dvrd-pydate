from enum import Enum


class DatePart(Enum):
    YEAR = 'year'
    YEARS = 'years'
    MONTH = 'month'
    MONTHS = 'months'
    DAY = 'day'
    DAYS = 'days'
    WEEK = 'week'
    WEEKS = 'weeks'


class TimePart(Enum):
    HOUR = 'hour'
    HOURS = 'hours'
    MINUTE = 'minute'
    MINUTES = 'minutes'
    SECOND = 'second'
    SECONDS = 'seconds'
    MICROSECOND = 'microsecond'
    MICROSECONDS = 'microseconds'
