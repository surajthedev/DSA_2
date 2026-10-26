# You are given a string s containing lowercase letters and an integer k. You need to :

# First, change some characters of s to other lowercase English letters.
# Then divide s into k non-empty disjoint substrings such that each substring is a palindrome.
# Return the minimal number of characters that you need to change to divide the string.



# Example 1:

# Input: s = "abc", k = 2
# Output: 1
# Explanation: You can split the string into "ab" and "c", and change 1 character in "ab" to make it palindrome.
# Example 2:

# Input: s = "aabbc", k = 3
# Output: 0
# Explanation: You can split the string into "aa", "bb" and "c", all of them are palindrome.
# Example 3:

# Input: s = "leetcode", k = 8
# Output: 0


# Constraints:

# 1 <= k <= s.length <= 100.
# s only contains lowercase English letters.
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
# Brute force:

from functools import lru_cache

class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        n = len(s)

        def cost(i, j):
            changes = 0
            while i < j:
                if s[i] != s[j]:
                    changes += 1
                i += 1
                j -= 1
            return changes

        @lru_cache(None)
        def dfs(start, parts):
            if parts == 1:
                return cost(start, n - 1)

            ans = float('inf')

            for end in range(start, n - parts + 1):
                ans = min(
                    ans,
                    cost(start, end) + dfs(end + 1, parts - 1)
                )

            return ans

        return dfs(0, k)











# Optimal:

class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        n = len(s)
        cost = [[0] * n for _ in range(n)]

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                cost[i][j] = cost[i + 1][j - 1] + (s[i] != s[j])

        dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0

        for i in range(1, n + 1):
            for parts in range(1, min(i, k) + 1):
                for j in range(parts - 1, i):
                    dp[i][parts] = min(
                        dp[i][parts],
                        dp[j][parts - 1] + cost[j][i - 1]
                    )

        return dp[n][k]
