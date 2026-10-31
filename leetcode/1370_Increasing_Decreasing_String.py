# You are given a string s. Reorder the string using the following algorithm:

# Remove the smallest character from s and append it to the result.
# Remove the smallest character from s that is greater than the last appended character, and append it to the result.
# Repeat step 2 until no more characters can be removed.
# Remove the largest character from s and append it to the result.
# Remove the largest character from s that is smaller than the last appended character, and append it to the result.
# Repeat step 5 until no more characters can be removed.
# Repeat steps 1 through 6 until all characters from s have been removed.
# If the smallest or largest character appears more than once, you may choose any occurrence to append to the result.

# Return the resulting string after reordering s using this algorithm.



# Example 1:

# Input: s = "aaaabbbbcccc"
# Output: "abccbaabccba"
# Explanation: After steps 1, 2 and 3 of the first iteration, result = "abc"
# After steps 4, 5 and 6 of the first iteration, result = "abccba"
# First iteration is done. Now s = "aabbcc" and we go back to step 1
# After steps 1, 2 and 3 of the second iteration, result = "abccbaabc"
# After steps 4, 5 and 6 of the second iteration, result = "abccbaabccba"
# Example 2:

# Input: s = "rat"
# Output: "art"
# Explanation: The word "rat" becomes "art" after re-ordering it with the mentioned algorithm.


# Constraints:

# 1 <= s.length <= 500
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
#
# LeetCode 1370. Increasing Decreasing String

### 1. Brute Force

python

```python
class Solution:
    def sortString(self, s: str) -> str:
        chars = list(s)
        result = []

        while chars:
            chars.sort()

            prev = ''

            for ch in chars[:]:
                if ch > prev:
                    result.append(ch)
                    chars.remove(ch)
                    prev = ch

            chars.sort(reverse=True)

            prev = ''

            for ch in chars[:]:
                if ch < prev or prev == '':
                    result.append(ch)
                    chars.remove(ch)
                    prev = ch

        return ''.join(result)
```

### 2. Optimal (Frequency Counting)

python

```python
class Solution:
    def sortString(self, s: str) -> str:
        freq = [0] * 26

        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        result = []

        while len(result) < len(s):

            # Increasing order
            for i in range(26):
                if freq[i] > 0:
                    result.append(chr(i + ord('a')))
                    freq[i] -= 1

            # Decreasing order
            for i in range(25, -1, -1):
                if freq[i] > 0:
                    result.append(chr(i + ord('a')))
                    freq[i] -= 1

        return ''.join(result)
```

### Complexity

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(n² log n) | O(n) |
| Optimal | O(26 × n) = O(n) | O(26) = O(1) |
