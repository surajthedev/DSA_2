# Run-length encoding is a string compression method that works by replacing consecutive identical characters (repeated 2 or more times) with the concatenation of the character and the number marking the count of the characters (length of the run). For example, to compress the string "aabccc" we replace "aa" by "a2" and replace "ccc" by "c3". Thus the compressed string becomes "a2bc3".

# Notice that in this problem, we are not adding '1' after single characters.

# Given a string s and an integer k. You need to delete at most k characters from s such that the run-length encoded version of s has minimum length.

# Find the minimum length of the run-length encoded version of s after deleting at most k characters.



# Example 1:

# Input: s = "aaabcccd", k = 2
# Output: 4
# Explanation: Compressing s without deleting anything will give us "a3bc3d" of length 6. Deleting any of the characters 'a' or 'c' would at most decrease the length of the compressed string to 5, for instance delete 2 'a' then we will have s = "abcccd" which compressed is abc3d. Therefore, the optimal way is to delete 'b' and 'd', then the compressed version of s will be "a3c3" of length 4.
# Example 2:

# Input: s = "aabbaa", k = 2
# Output: 2
# Explanation: If we delete both 'b' characters, the resulting compressed string would be "a4" of length 2.
# Example 3:

# Input: s = "aaaaaaaaaaa", k = 0
# Output: 3
# Explanation: Since k is zero, we cannot delete anything. The compressed string is "a11" of length 3.


# Constraints:

# 1 <= s.length <= 100
# 0 <= k <= s.length
# s contains only lowercase English letters.
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
#
#
#
#
#
#
#
#
# ### 1. Brute Force – Recursion + Memoization (DP)

Time Complexity: O(n² × k) Space Complexity: O(n × k)

python

```python
from functools import lru_cache

class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:

        n = len(s)

        @lru_cache(None)
        def dp(i, k):
            if k < 0:
                return float('inf')

            if i == n or n - i <= k:
                return 0

            # Delete current character
            ans = dp(i + 1, k - 1)

            # Keep current character
            count = 0
            deleted = 0

            for j in range(i, n):
                if s[j] == s[i]:
                    count += 1
                else:
                    deleted += 1

                if deleted <= k:
                    length = 1 if count == 1 else 1 + len(str(count))
                    ans = min(ans, length + dp(j + 1, k - deleted))

            return ans

        return dp(0, k)
```

### 2. Optimal – Dynamic Programming (DP)

Time Complexity: O(n² × k) Space Complexity: O(n × k)

python

```python
class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        n = len(s)
        INF = float('inf')

        dp = [[INF] * (k + 1) for _ in range(n + 1)]

        dp[n] = [0] * (k + 1)

        for i in range(n - 1, -1, -1):
            for rem in range(k + 1):

                # Delete current character
                if rem > 0:
                    dp[i][rem] = dp[i + 1][rem - 1]

                count = 0
                deleted = 0

                for j in range(i, n):
                    if s[j] == s[i]:
                        count += 1
                    else:
                        deleted += 1

                    if deleted > rem:
                        break

                    length = 1
                    if count >= 2:
                        length += len(str(count))

                    dp[i][rem] = min(
                        dp[i][rem],
                        length + dp[j + 1][rem - deleted]
                    )

        return dp[0][k]
```
