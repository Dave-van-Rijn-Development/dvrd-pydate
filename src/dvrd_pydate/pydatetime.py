from datetime import datetime, timedelta, date
from typing import Self, Generator

from dvrd_pydate.enums import DatePart, TimePart
from dvrd_pydate.pydate import PYDate

hours_in_day = 24
minutes_in_hour = 60
seconds_in_minute = 60
microseconds_in_second = 1000


class PYDateTime(datetime, PYDate):
    @staticmethod
    def from_value(value: datetime | str = None):
        if isinstance(value, str):
            value = datetime.fromisoformat(value)
        elif value is None:
            value = datetime.now()
        return PYDateTime(value.year, value.month, value.day, value.hour, value.minute, value.second,
                          value.microsecond, value.tzinfo, fold=value.fold)

    @staticmethod
    def iter(*, start: date | str = None, end: date | str | None = None,
             step: DatePart | TimePart | tuple[int, DatePart | TimePart] = DatePart.DAY) -> \
            Generator["PYDateTime", None, None]:
        if start is None:
            start = datetime.now()
        current = PYDateTime.from_value(start)
        end_value = None if end is None else PYDateTime.from_value(end)
        if isinstance(step, tuple):
            step_value = step[0]
            step_key = step[1]
        else:
            step_value = 1
            step_key = step
        while end_value is None or current < end_value:
            yield current
            current = current.add(value=step_value, key=step_key)

    def add(self, *, value: int, key: DatePart | TimePart) -> Self:
        if isinstance(key, DatePart):
            return super().add(value=value, key=key)
        elif key in [TimePart.HOUR, TimePart.HOURS]:
            return self.add_hours(value)
        elif key in [TimePart.MINUTE, TimePart.MINUTES]:
            return self.add_minutes(value)
        elif key in [TimePart.SECOND, TimePart.SECONDS]:
            return self.add_seconds(value)
        elif key in [TimePart.MICROSECOND, TimePart.MICROSECONDS]:
            return self.add_microseconds(value)
        else:
            raise KeyError(f'Key "{key}" cannot be used in PYDateTime')

    def subtract(self, *, value: int, key: DatePart | TimePart) -> Self:
        if isinstance(key, DatePart):
            return super().subtract(value=value, key=key)
        elif key in [TimePart.HOUR, TimePart.HOURS]:
            return self.subtract_hours(value)
        elif key in [TimePart.MINUTE, TimePart.MINUTES]:
            return self.subtract_minutes(value)
        elif key in [TimePart.SECOND, TimePart.SECONDS]:
            return self.subtract_seconds(value)
        elif key in [TimePart.MICROSECOND, TimePart.MICROSECONDS]:
            return self.subtract_microseconds(value)
        else:
            raise KeyError(f'Key "{key}" cannot be used in PYDateTime')

    def add_hours(self, value: int) -> Self:
        return self + timedelta(hours=value)

    def add_hour(self) -> Self:
        return self.add_hours(1)

    def subtract_hours(self, value: int) -> Self:
        return self - timedelta(hours=value)

    def subtract_hour(self) -> Self:
        return self.subtract_hours(1)

    def add_minutes(self, value: int) -> Self:
        return self + timedelta(minutes=value)

    def add_minute(self) -> Self:
        return self.add_minutes(1)

    def subtract_minutes(self, value: int) -> Self:
        return self - timedelta(minutes=value)

    def subtract_minute(self) -> Self:
        return self.subtract_minutes(1)

    def add_seconds(self, value: int) -> Self:
        return self + timedelta(seconds=value)

    def add_second(self) -> Self:
        return self.add_seconds(1)

    def subtract_seconds(self, value: int) -> Self:
        return self - timedelta(seconds=value)

    def subtract_second(self) -> Self:
        return self.subtract_seconds(1)

    def add_microseconds(self, value: int) -> Self:
        return self + timedelta(microseconds=value)

    def add_microsecond(self) -> Self:
        return self.add_microseconds(1)

    def subtract_microseconds(self, value: int) -> Self:
        return self - timedelta(microseconds=value)

    def subtract_microsecond(self) -> Self:
        return self.subtract_microseconds(1)

    def start_of(self, part: DatePart | TimePart) -> Self:
        if isinstance(part, DatePart):
            if part in [DatePart.DAY, DatePart.DAYS]:
                return self.replace(hour=0, minute=0, second=0, microsecond=0)
            return super().start_of(part)
        elif part in [TimePart.HOUR, TimePart.HOURS]:
            return self.replace(minute=0, second=0, microsecond=0)
        elif part in [TimePart.MINUTE, TimePart.MINUTES]:
            return self.replace(second=0, microsecond=0)
        elif part in [TimePart.SECOND, TimePart.SECONDS]:
            return self.replace(microsecond=0)
        elif part in [TimePart.MICROSECOND, TimePart.MICROSECONDS]:
            return self
        else:
            raise KeyError(f'Unsupported start_of part {part}')

    def end_of(self, part: DatePart | TimePart) -> Self:
        if isinstance(part, DatePart):
            if part in [DatePart.DAY, DatePart.DAYS]:
                return self.replace(hour=23, minute=59, second=59, microsecond=999)
            return super().end_of(part)
        elif part in [TimePart.HOUR, TimePart.HOURS]:
            return self.replace(minute=59, second=59, microsecond=999)
        elif part in [TimePart.MINUTE, TimePart.MINUTES]:
            return self.replace(second=59, microsecond=999)
        elif part in [TimePart.SECOND, TimePart.SECONDS]:
            return self.replace(microsecond=999)
        elif part in [TimePart.MICROSECOND, TimePart.MICROSECONDS]:
            return self
        else:
            raise KeyError(f'Unsupported end_of part {part}')
