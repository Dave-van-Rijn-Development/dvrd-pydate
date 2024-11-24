from datetime import datetime, timedelta
from typing import Self

from dvrd_pydate.enums import ModifyKey
from dvrd_pydate.pydate import PYDate

hours_in_day = 24
minutes_in_hour = 60
seconds_in_minute = 60
microseconds_in_second = 1000


class PYDateTime(datetime, PYDate):
    @classmethod
    def from_value(cls, value: datetime | str = None):
        if isinstance(value, str):
            value = datetime.fromisoformat(value)
        elif value is None:
            value = datetime.now()
        return PYDateTime(value.year, value.month, value.day, value.hour, value.minute, value.second,
                          value.microsecond, value.tzinfo, fold=value.fold)

    def add(self, *, value: int, key: ModifyKey) -> Self:
        try:
            super().add(value=value, key=key)
        except KeyError:
            if key in [ModifyKey.HOUR, ModifyKey.HOURS]:
                return self.add_hours(value)
            elif key in [ModifyKey.MINUTE, ModifyKey.MINUTES]:
                return self.add_minutes(value)
            elif key in [ModifyKey.SECOND, ModifyKey.SECONDS]:
                return self.add_seconds(value)
            elif key in [ModifyKey.MICROSECOND, ModifyKey.MICROSECONDS]:
                return self.add_microseconds(value)
            raise KeyError(f'Key "{key}" cannot be used in PYDateTime')

    def subtract(self, *, value: int, key: ModifyKey) -> Self:
        try:
            super().subtract(value=value, key=key)
        except KeyError:
            if key in [ModifyKey.HOUR, ModifyKey.HOURS]:
                return self.subtract_hours(value)
            elif key in [ModifyKey.MINUTE, ModifyKey.MINUTES]:
                return self.subtract_minutes(value)
            elif key in [ModifyKey.SECOND, ModifyKey.SECONDS]:
                return self.subtract_seconds(value)
            elif key in [ModifyKey.MICROSECOND, ModifyKey.MICROSECONDS]:
                return self.subtract_microseconds(value)
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
