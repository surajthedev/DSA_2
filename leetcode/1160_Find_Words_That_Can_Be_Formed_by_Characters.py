# You are given an array of strings words and a string chars.

# A string is good if it can be formed by characters from chars (each character can only be used once for each word in words).

# Return the sum of lengths of all good strings in words.



# Example 1:

# Input: words = ["cat","bt","hat","tree"], chars = "atach"
# Output: 6
# Explanation: The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.
# Example 2:

# Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
# Output: 10
# Explanation: The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.


# Constraints:

# 1 <= words.length <= 1000
# 1 <= words[i].length, chars.length <= 100
# words[i] and chars consist of lowercase English letters.
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
# ### Brute Force — Python

python
```
from collections import Counter

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ans = 0

        for word in words:
            temp = list(chars)

            for ch in word:
                if ch in temp:
                    temp.remove(ch)
                else:
                    break
            else:
                ans += len(word)

        return ans
```

### Optimal — Python

python
```
from collections import Counter

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_count = Counter(chars)
        ans = 0

        for word in words:
            word_count = Counter(word)

            if all(word_count[ch] <= chars_count[ch] for ch in word_count):
                ans += len(word)

        return ans
```
