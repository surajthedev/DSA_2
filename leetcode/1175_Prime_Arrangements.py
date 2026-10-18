# Return the number of permutations of 1 to n so that prime numbers are at prime indices (1-indexed.)

# (Recall that an integer is prime if and only if it is greater than 1, and cannot be written as a product of two positive integers both smaller than it.)

# Since the answer may be large, return the answer modulo 10^9 + 7.



# Example 1:

# Input: n = 5
# Output: 12
# Explanation: For example [1,2,5,4,3] is a valid permutation, but [5,2,3,4,1] is not because the prime number 5 is at index 1.
# Example 2:

# Input: n = 100
# Output: 682289015


# Constraints:

# 1 <= n <= 100
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
# ### 1. Brute Force

python
```
from itertools import permutations

class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        MOD = 10**9 + 7

        primes = []
        for i in range(2, n + 1):
            if all(i % j != 0 for j in range(2, int(i**0.5) + 1)):
                primes.append(i)

        count = 0

        for p in permutations(range(1, n + 1)):
            if all(
                (p[i - 1] in primes) == (i in primes)
                for i in range(1, n + 1)
            ):
                count += 1

        return count % MOD
```

### 2. Optimal Solution

python
```
class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        MOD = 10**9 + 7

        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False

        for i in range(2, int(n**0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, n + 1, i):
                    is_prime[j] = False

        prime_count = sum(is_prime)
        non_prime_count = n - prime_count

        return (
            self.factorial(prime_count, MOD)
            * self.factorial(non_prime_count, MOD)
        ) % MOD

    def factorial(self, n: int, mod: int) -> int:
        result = 1
        for i in range(2, n + 1):
            result = result * i % mod
        return result
```
