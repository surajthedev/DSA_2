# A string s is called good if there are no two different characters in s that have the same frequency.

# Given a string s, return the minimum number of characters you need to delete to make s good.

# The frequency of a character in a string is the number of times it appears in the string. For example, in the string "aab", the frequency of 'a' is 2, while the frequency of 'b' is 1.



# Example 1:

# Input: s = "aab"
# Output: 0
# Explanation: s is already good.
# Example 2:

# Input: s = "aaabbbcc"
# Output: 2
# Explanation: You can delete two 'b's resulting in the good string "aaabcc".
# Another way it to delete one 'b' and one 'c' resulting in the good string "aaabbc".
# Example 3:

# Input: s = "ceabaacb"
# Output: 2
# Explanation: You can delete both 'c's resulting in the good string "eabaab".
# Note that we only care about characters that are still in the string at the end (i.e. frequency of 0 is ignored).


# Constraints:

# 1 <= s.length <= 105
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
# ### 1. Brute Force Solution

python

```python
from collections import Counter

class Solution:
    def minDeletions(self, s: str) -> int:
        freq = list(Counter(s).values())
        ans = 0

        for i in range(len(freq)):
            while freq[i] > 0 and freq[i] in freq[:i]:
                freq[i] -= 1
                ans += 1

        return ans
```

Time Complexity: O(n × 26)

Space Complexity: O(26)

### 2. Optimal Solution (Greedy + Set)

python

```python
from collections import Counter

class Solution:
    def minDeletions(self, s: str) -> int:
        freq = Counter(s)
        used = set()
        ans = 0

        for count in freq.values():
            while count > 0 and count in used:
                count -= 1
                ans += 1

            if count > 0:
                used.add(count)

        return ans
```

Time Complexity: O(n + 26²)

Space Complexity: O(26)
