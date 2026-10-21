# n passengers board an airplane with exactly n seats. The first passenger has lost the ticket and picks a seat randomly. But after that, the rest of the passengers will:

# Take their own seat if it is still available, and
# Pick other seats randomly when they find their seat occupied
# Return the probability that the nth person gets his own seat.



# Example 1:

# Input: n = 1
# Output: 1.00000
# Explanation: The first person can only get the first seat.
# Example 2:

# Input: n = 2
# Output: 0.50000
# Explanation: The second person has a probability of 0.5 to get the second seat (when first person gets the first seat).


# Constraints:

# 1 <= n <= 105
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
#
#
#
#
# ### Brute Force (Simulation)

python
```
import random

class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        trials = 100000
        success = 0

        for _ in range(trials):
            seats = [False] * n
            seats[random.randrange(n)] = True

            for person in range(1, n):
                if not seats[person]:
                    seats[person] = True
                else:
                    available = [i for i in range(n) if not seats[i]]
                    if available:
                        seats[random.choice(available)] = True

            if seats[n - 1]:
                success += 1

        return success / trials
```

### Optimal Solution — O(1)

python
```
class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        if n == 1:
            return 1.0
        return 0.5
```
