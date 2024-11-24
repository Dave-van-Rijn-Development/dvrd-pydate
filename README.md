# dvrd_pydate

Python `date` and `datetime` extensions, adding useful init and mutation functions.

## Example

```python
from datetime import date
from dvrd_pydate import PYDate, ModifyKey

# Default date functions are still available
today = PYDate.today()

# Create date from string or existing date
date_value = PYDate.from_value('2024-01-01')
date_value = PYDate.from_value(date(2024, 1, 1))

# Mutation functions are available for all properties
date_value = date_value.add(value=3, key=ModifyKey.DAYS)  # 2024-01-04
date_value = date_value.subtract(value=1, key=ModifyKey.YEAR)  # 2023-01-04

# Simplified functions are available for mutations with value 1
date_value = date_value.add_year()  # 2024-01-04
date_value = date_value.subtract_month()  # 2023-12-04
```

### PYDate

Python `date` extension.

| **Function**      | Arguments                      | **Description**                                                                                                                     |
|-------------------|--------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| `add`             | `value: int`, `key: ModifyKey` | Adds the `value` in `key` to the current value. Raises a `KeyError` when an unsupported key is supplied (like ModifyKey.HOUR).      |
| `subtract`        | `value: int`, `key: ModifyKey` | Subtracts the `value` in `key` to the current value. Raises a `KeyError` when an unsupported key is supplied (like ModifyKey.HOUR). |
| `add_years`       | `value: int`                   | Add `value` years to the current value.                                                                                             |
| `add_year`        | N/A                            | Add 1 year to the current value.                                                                                                    |
| `subtract_years`  | `value: int`                   | Subtract `value` years from the current value.                                                                                      |
| `subtract_year`   | N/A                            | Subtract 1 year from the current value.                                                                                             |
| `add_months`      | `value: int`                   | Add `value` months to the current value.                                                                                            |
| `add_month`       | N/A                            | Add 1 month to the current value.                                                                                                   |
| `subtract_months` | `value: int`                   | Subtract `value` months from the current value.                                                                                     |
| `subtract_month`  | N/A                            | Subtract 1 month from the current value.                                                                                            |
| `add_weeks`       | `value: int`                   | Add `value` weeks to the current value.                                                                                             |
| `add_week`        | N/A                            | Add 1 week to the current value.                                                                                                    |
| `subtract_weeks`  | `value: int`                   | Subtract `value` weeks from the current value.                                                                                      |
| `subtract_week`   | N/A                            | Subtract 1 week from the current value.                                                                                             |
| `add_days`        | `value: int`                   | Add `value` days to the current value.                                                                                              |
| `add_day`         | N/A                            | Add 1 day to the current value.                                                                                                     |
| `subtract_days`   | `value: int`                   | Subtract `value` days from the current value.                                                                                       |
| `subtract_day`    | N/A                            | Subtract 1 day from the current value.                                                                                              |
| `clone`           | N/A                            | Returns a new `PYDate` object with the current value.                                                                               |

### PYDateTime

Python `datetime` extension. Inherits all functions from `PYDate`, but extends the `add` and `subtract` support to the
time parts.

| **Function**            | Arguments    | **Description**                                       |
|-------------------------|--------------|-------------------------------------------------------|
| `add_hours`             | `value: int` | Add `value` hours to the current value.               |
| `add_hour`              | N/A          | Add 1 hour to the current value.                      |
| `subtract_hours`        | `value: int` | Subtract `value` hours from the current value.        |
| `subtract_hour`         | N/A          | Subtract 1 hour from the current value.               |
| `add_minutes`           | `value: int` | Add `value` minutes to the current value.             |
| `add_minute`            | N/A          | Add 1 minute to the current value.                    |
| `subtract_minutes`      | `value: int` | Subtract `value` minutes from the current value.      |
| `subtract_minute`       | N/A          | Subtract 1 minute from the current value.             |
| `add_seconds`           | `value: int` | Add `value` seconds to the current value.             |
| `add_second`            | N/A          | Add 1 second to the current value.                    |
| `subtract_seconds`      | `value: int` | Subtract `value` seconds from the current value.      |
| `subtract_second`       | N/A          | Subtract 1 second from the current value.             |
| `add_microseconds`      | `value: int` | Add `value` microseconds to the current value.        |
| `add_microsecond`       | N/A          | Add 1 microsecond to the current value.               |
| `subtract_microseconds` | `value: int` | Subtract `value` microseconds from the current value. |
| `subtract_microsecond`  | N/A          | Subtract 1 microsecond from the current value.        |