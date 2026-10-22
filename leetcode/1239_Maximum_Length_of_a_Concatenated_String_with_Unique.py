# You are given an array of strings arr. A string s is formed by the concatenation of a subsequence of arr that has unique characters.

# Return the maximum possible length of s.

# A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.



# Example 1:

# Input: arr = ["un","iq","ue"]
# Output: 4
# Explanation: All the valid concatenations are:
# - ""
# - "un"
# - "iq"
# - "ue"
# - "uniq" ("un" + "iq")
# - "ique" ("iq" + "ue")
# Maximum length is 4.
# Example 2:

# Input: arr = ["cha","r","act","ers"]
# Output: 6
# Explanation: Possible longest valid concatenations are "chaers" ("cha" + "ers") and "acters" ("act" + "ers").
# Example 3:

# Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
# Output: 26
# Explanation: The only string in arr has all 26 characters.


# Constraints:

# 1 <= arr.length <= 16
# 1 <= arr[i].length <= 26
# arr[i] contains only lowercase English letters.
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
# ### Brute Force

python
```
class Solution:
    def maxLength(self, arr: list[str]) -> int:
        n = len(arr)
        ans = 0

        for mask in range(1 << n):
            s = ""
            valid = True

            for i in range(n):
                if mask & (1 << i):
                    s += arr[i]

            if len(s) != len(set(s)):
                valid = False

            if valid:
                ans = max(ans, len(s))

        return ans
```

### Optimal — Bitmask + Backtracking

python
```
class Solution:
    def maxLength(self, arr: list[str]) -> int:
        masks = []

        for s in arr:
            mask = 0

            for ch in s:
                bit = 1 << (ord(ch) - ord('a'))

                if mask & bit:
                    break

                mask |= bit
            else:
                masks.append(mask)

        def backtrack(i, used):
            if i == len(masks):
                return used.bit_count()

            skip = backtrack(i + 1, used)

            if used & masks[i] == 0:
                take = backtrack(i + 1, used | masks[i])
                return max(skip, take)

            return skip

        return backtrack(0, 0)
```
