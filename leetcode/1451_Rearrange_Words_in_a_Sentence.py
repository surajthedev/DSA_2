# Given a sentence text (A sentence is a string of space-separated words) in the following format:

# First letter is in upper case.
# Each word in text are separated by a single space.
# Your task is to rearrange the words in text such that all words are rearranged in an increasing order of their lengths. If two words have the same length, arrange them in their original order.

# Return the new text following the format shown above.



# Example 1:

# Input: text = "Leetcode is cool"
# Output: "Is cool leetcode"
# Explanation: There are 3 words, "Leetcode" of length 8, "is" of length 2 and "cool" of length 4.
# Output is ordered by length and the new first word starts with capital letter.
# Example 2:

# Input: text = "Keep calm and code on"
# Output: "On and keep calm code"
# Explanation: Output is ordered as follows:
# "On" 2 letters.
# "and" 3 letters.
# "keep" 4 letters in case of tie order by position in original text.
# "calm" 4 letters.
# "code" 4 letters.
# Example 3:

# Input: text = "To be or not to be"
# Output: "To be or to be not"


# Constraints:

# text begins with a capital letter and then contains lowercase letters and single space between words.
# 1 <= text.length <= 10^5
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
# ### 1. Brute Force — Python

python

```python
class Solution:
    def arrangeWords(self, text: str) -> str:
        words = text.split()
        result = []

        while words:
            shortest = min(words, key=len)
            result.append(shortest)
            words.remove(shortest)

        ans = " ".join(result)
        return ans[0].upper() + ans[1:].lower()
```

Time Complexity: $O(N^2)$

Space Complexity: $O(N)$

### 2. Optimal — Python (Sorting)

python

```python
class Solution:
    def arrangeWords(self, text: str) -> str:
        words = text.lower().split()

        words.sort(key=len)

        ans = " ".join(words)

        return ans.capitalize()
```

Time Complexity: $O(N \log N)$

Space Complexity: $O(N)$
