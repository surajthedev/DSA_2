# Write a program to count the number of days between two dates.

# The two dates are given as strings, their format is YYYY-MM-DD as shown in the examples.



# Example 1:

# Input: date1 = "2019-06-29", date2 = "2019-06-30"
# Output: 1
# Example 2:

# Input: date1 = "2020-01-15", date2 = "2019-12-31"
# Output: 15


# Constraints:

# The given dates are valid dates between the years 1971 and 2100.
#
#
#
#
#
#
#
#
#
#
#
#
#
# ### Brute Force

python

```
class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        def countDays(date):
            y, m, d = map(int, date.split("-"))
            days = 0

            for year in range(1971, y):
                days += 366 if (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)) else 365

            monthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

            for month in range(m - 1):
                days += monthDays[month]

                if month == 1 and (y % 400 == 0 or (y % 4 == 0 and y % 100 != 0)):
                    days += 1

            days += d
            return days

        return abs(countDays(date1) - countDays(date2))
```

### Optimal Solution (Python Datetime)

python

```
from datetime import date

class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        y1, m1, d1 = map(int, date1.split("-"))
        y2, m2, d2 = map(int, date2.split("-"))

        return abs((date(y1, m1, d1) - date(y2, m2, d2)).days)
```
