# Given a date, return the corresponding day of the week for that date.

# The input is given as three integers representing the day, month and year respectively.

# Return the answer as one of the following values {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}.

# Note: January 1, 1971 was a Friday.



# Example 1:

# Input: day = 31, month = 8, year = 2019
# Output: "Saturday"
# Example 2:

# Input: day = 18, month = 7, year = 1999
# Output: "Sunday"
# Example 3:

# Input: day = 15, month = 8, year = 1993
# Output: "Sunday"


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
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        from datetime import date

        return date(year, month, day).strftime("%A")
```

### Optimal

python
```

class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        days = ["Sunday", "Monday", "Tuesday", "Wednesday",
                "Thursday", "Friday", "Saturday"]

        total = 0

        for y in range(1971, year):
            total += 366 if (y % 400 == 0 or (y % 4 == 0 and y % 100 != 0)) else 365

        month_days = [31, 28, 31, 30, 31, 30,
                      31, 31, 30, 31, 30, 31]

        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            month_days[1] = 29

        total += sum(month_days[:month - 1])
        total += day - 1

        return days[(total + 5) % 7]
```
