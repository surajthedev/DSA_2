# Given a string s, return the maximum number of occurrences of any substring under the following rules:

# The number of unique characters in the substring must be less than or equal to maxLetters.
# The substring size must be between minSize and maxSize inclusive.


# Example 1:

# Input: s = "aababcaab", maxLetters = 2, minSize = 3, maxSize = 4
# Output: 2
# Explanation: Substring "aab" has 2 occurrences in the original string.
# It satisfies the conditions, 2 unique letters and size 3 (between minSize and maxSize).
# Example 2:

# Input: s = "aaaa", maxLetters = 1, minSize = 3, maxSize = 3
# Output: 2
# Explanation: Substring "aaa" occur 2 times in the string. It can overlap.


# Constraints:

# 1 <= s.length <= 105
# 1 <= maxLetters <= 26
# 1 <= minSize <= maxSize <= min(26, s.length)
# s consists of only lowercase English letters.
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

from collections import Counter

class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        count = Counter()
        n = len(s)

        for size in range(minSize, maxSize + 1):
            for i in range(n - size + 1):
                sub = s[i:i + size]

                if len(set(sub)) <= maxLetters:
                    count[sub] += 1

        return max(count.values(), default=0)
```

### Optimal (Sliding Window + Hash Map)

python

```

from collections import Counter

class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        count = Counter()
        window = Counter()
        distinct = 0
        result = 0

        for i, ch in enumerate(s):
            window[ch] += 1

            if window[ch] == 1:
                distinct += 1

            if i >= minSize:
                left_char = s[i - minSize]
                window[left_char] -= 1

                if window[left_char] == 0:
                    distinct -= 1
                    del window[left_char]

            if i >= minSize - 1 and distinct <= maxLetters:
                sub = s[i - minSize + 1:i + 1]
                count[sub] += 1
                result = max(result, count[sub])

        return result
```
