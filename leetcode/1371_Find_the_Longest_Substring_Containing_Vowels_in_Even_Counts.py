# Given the string s, return the size of the longest substring containing each vowel an even number of times. That is, 'a', 'e', 'i', 'o', and 'u' must appear an even number of times.



# Example 1:

# Input: s = "eleetminicoworoep"
# Output: 13
# Explanation: The longest substring is "leetminicowor" which contains two each of the vowels: e, i and o and zero of the vowels: a and u.
# Example 2:

# Input: s = "leetcodeisgreat"
# Output: 5
# Explanation: The longest substring is "leetc" which contains two e's.
# Example 3:

# Input: s = "bcbcbc"
# Output: 6
# Explanation: In this case, the given string "bcbcbc" is the longest because all vowels: a, e, i, o and u appear zero times.


# Constraints:

# 1 <= s.length <= 5 x 10^5
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
# LeetCode 1371. Find the Longest Substring Containing Vowels in Even Counts

### 1. Brute Force

python

```python
class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0

        vowels = set("aeiou")

        for i in range(n):
            count = [0] * 5

            for j in range(i, n):
                if s[j] in vowels:
                    count["aeiou".index(s[j])] += 1

                if all(x % 2 == 0 for x in count):
                    ans = max(ans, j - i + 1)

        return ans
```

### 2. Optimal (Bitmask + HashMap)

python

```python
class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        mask = 0
        first = {0: -1}
        ans = 0

        vowels = {
            'a': 0,
            'e': 1,
            'i': 2,
            'o': 3,
            'u': 4
        }

        for i, ch in enumerate(s):

            if ch in vowels:
                mask ^= (1 << vowels[ch])

            if mask in first:
                ans = max(ans, i - first[mask])
            else:
                first[mask] = i

        return ans
```

### Complexity

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(n²) | O(1) |
| Optimal | O(n) | O(1) |

Optimal: O(n)
