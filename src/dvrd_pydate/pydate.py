from calendar import monthrange
from datetime import date, timedelta
from typing import Self, Generator

from dvrd_pydate.enums import ModifyKey

days_in_week = 7
months_in_year = 12


class PYDate(date):
    @staticmethod
    def from_value(value: date | str = None):
        if isinstance(value, str):
            value = date.fromisoformat(value)
        elif value is None:
            value = date.today()
        return PYDate(value.year, value.month, value.day)

    @staticmethod
    def iter(*, start: date | str, end: date | str | None = None,
             step: ModifyKey | tuple[int, ModifyKey] = ModifyKey.DAY) -> Generator["PYDate", None, None]:
        current = PYDate.from_value(start)
        end_value = None if end is None else PYDate.from_value(end)
        if isinstance(step, tuple):
            step_value = step[0]
            step_key = step[1]
        else:
            if step not in (ModifyKey.DAYS, ModifyKey.DAY, ModifyKey.MONTHS, ModifyKey.MONTH, ModifyKey.YEAR,
                            ModifyKey.YEARS):
                raise KeyError(f'Invalid step key for PYDate: {step}')
            step_value = 1
            step_key = step
        while end_value is None or current < end_value:
            yield current
            current = current.add(value=step_value, key=step_key)

    def add(self, *, value: int, key: ModifyKey) -> Self:
        if key in [ModifyKey.YEAR, ModifyKey.YEARS]:
            return self.add_years(value)
        elif key in [ModifyKey.MONTH, ModifyKey.MONTHS]:
            return self.add_months(value)
        elif key in [ModifyKey.WEEK, ModifyKey.WEEKS]:
            return self.add_weeks(value)
        elif key in [ModifyKey.DAY, ModifyKey.DAYS]:
            return self.add_days(value)
        else:
            raise KeyError(f'Key "{key}" cannot be used in PYDate')

    def subtract(self, *, value: int, key: ModifyKey) -> Self:
        if key in [ModifyKey.YEAR, ModifyKey.YEARS]:
            return self.subtract_years(value)
        elif key in [ModifyKey.MONTH, ModifyKey.MONTHS]:
            return self.subtract_months(value)
        elif key in [ModifyKey.WEEK, ModifyKey.WEEKS]:
            return self.subtract_weeks(value)
        elif key in [ModifyKey.DAY, ModifyKey.DAYS]:
            return self.subtract_days(value)
        else:
            raise KeyError(f'Key "{key}" cannot be used in PYDate')

    def add_years(self, value: int) -> Self:
        return self.replace(year=self.year + value)

    def add_year(self) -> Self:
        return self.add_years(1)

    def subtract_years(self, value: int) -> Self:
        return self.replace(year=self.year - value)

    def subtract_year(self) -> Self:
        return self.subtract_years(1)

    def add_months(self, value: int) -> Self:
        new_date = self.clone()
        add_years, month_value = divmod(new_date.month + value, months_in_year + 1)
        if add_years:
            month_value += 1
        year = new_date.year + add_years
        max_date = monthrange(year, month_value)[1]
        return new_date.replace(year=new_date.year + add_years, month=month_value, day=min(max_date, new_date.day))

    def add_month(self) -> Self:
        return self.add_months(1)

    def subtract_months(self, value: int) -> Self:
        new_date = self.clone()
        subtract_years, remaining_months = divmod(value, months_in_year)
        if subtract_years:
            new_date = new_date.subtract_years(subtract_years)
        if (month_value := new_date.month - remaining_months) < 1:
            new_date = new_date.subtract_year()
            month_value = 12 - abs(month_value)
        max_date = monthrange(new_date.year, month_value)[1]
        return new_date.replace(month=month_value, day=min(new_date.day, max_date))

    def subtract_month(self) -> Self:
        return self.subtract_months(1)

    def add_weeks(self, value: int) -> Self:
        return self + timedelta(weeks=value)

    def add_week(self) -> Self:
        return self.add_weeks(1)

    def subtract_weeks(self, value: int) -> Self:
        return self - timedelta(weeks=value)

    def subtract_week(self) -> Self:
        return self.subtract_weeks(1)

    def add_days(self, value: int) -> Self:
        return self + timedelta(days=value)

    def add_day(self) -> Self:
        return self.add_days(1)

    def subtract_days(self, value: int) -> Self:
        return self - timedelta(days=value)

    def subtract_day(self) -> Self:
        return self.subtract_days(1)

    def clone(self) -> "PYDate":
        return type(self).from_value(self)
