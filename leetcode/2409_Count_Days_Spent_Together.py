# Alice and Bob are traveling to Rome for separate business meetings.

# You are given 4 strings arriveAlice, leaveAlice, arriveBob, and leaveBob. Alice will be in the city from the dates arriveAlice to leaveAlice (inclusive), while Bob will be in the city from the dates arriveBob to leaveBob (inclusive). Each will be a 5-character string in the format "MM-DD", corresponding to the month and day of the date.

# Return the total number of days that Alice and Bob are in Rome together.

# You can assume that all dates occur in the same calendar year, which is not a leap year. Note that the number of days per month can be represented as: [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31].



# Example 1:

# Input: arriveAlice = "08-15", leaveAlice = "08-18", arriveBob = "08-16", leaveBob = "08-19"
# Output: 3
# Explanation: Alice will be in Rome from August 15 to August 18. Bob will be in Rome from August 16 to August 19. They are both in Rome together on August 16th, 17th, and 18th, so the answer is 3.
# Example 2:

# Input: arriveAlice = "10-01", leaveAlice = "10-31", arriveBob = "11-01", leaveBob = "12-31"
# Output: 0
# Explanation: There is no day when Alice and Bob are in Rome together, so we return 0.


# Constraints:

# All dates are provided in the format "MM-DD".
# Alice and Bob's arrival dates are earlier than or equal to their leaving dates.
# The given dates are valid dates of a non-leap year.
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
#
# BRute force:
class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        def to_day(date):
            month, day = map(int, date.split("-"))
            return sum(days[:month - 1]) + day

        start = max(to_day(arriveAlice), to_day(arriveBob))
        end = min(to_day(leaveAlice), to_day(leaveBob))

        count = 0
        for day in range(start, end + 1):
            count += 1

        return count










# Optimal:
class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        start = max(arriveAlice, arriveBob)
        end = min(leaveAlice, leaveBob)

        if start > end:
            return 0

        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        def to_day(date):
            month, day = map(int, date.split("-"))
            return sum(days[:month - 1]) + day

        return to_day(end) - to_day(start) + 1
