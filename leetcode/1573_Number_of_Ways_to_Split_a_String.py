# Given a binary string s, you can split s into 3 non-empty strings s1, s2, and s3 where s1 + s2 + s3 = s.

# Return the number of ways s can be split such that the number of ones is the same in s1, s2, and s3. Since the answer may be too large, return it modulo 109 + 7.



# Example 1:

# Input: s = "10101"
# Output: 4
# Explanation: There are four ways to split s in 3 parts where each part contain the same number of letters '1'.
# "1|010|1"
# "1|01|01"
# "10|10|1"
# "10|1|01"
# Example 2:

# Input: s = "1001"
# Output: 0
# Example 3:

# Input: s = "0000"
# Output: 3
# Explanation: There are three ways to split s in 3 parts.
# "0|0|00"
# "0|00|0"
# "00|0|0"


# Constraints:

# 3 <= s.length <= 105
# s[i] is either '0' or '1'.























 ### 1. Brute Force Approach

 python

 ```python
 class Solution:
     def numWays(self, s: str) -> int:
         MOD = 10**9 + 7
         n = len(s)
         ans = 0

         for i in range(1, n - 1):
             for j in range(i + 1, n):
                 s1 = s[:i]
                 s2 = s[i:j]
                 s3 = s[j:]

                 if s1.count('1') == s2.count('1') == s3.count('1'):
                     ans += 1

         return ans % MOD
 ```

 Time Complexity: O(n³) Space Complexity: O(n)

 ### 2. Optimal Approach (Prefix Sum + Counting)

 python

 ```python
 class Solution:
     def numWays(self, s: str) -> int:
         MOD = 10**9 + 7
         n = len(s)
         ones = s.count('1')

         if ones % 3 != 0:
             return 0

         if ones == 0:
             return ((n - 1) * (n - 2) // 2) % MOD

         target = ones // 3
         first = second = 0
         count = 0

         for i in range(n - 1):
             if s[i] == '1':
                 count += 1

             if count == target:
                 first += 1

             elif count == 2 * target:
                 second += 1

         return (first * second) % MOD
 ```

 Time Complexity: O(n) Space Complexity: O(1)
