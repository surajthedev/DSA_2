# Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

# You can use each character in text at most once. Return the maximum number of instances that can be formed.



# Example 1:



# Input: text = "nlaebolko"
# Output: 1
# Example 2:



# Input: text = "loonbalxballpoon"
# Output: 2
# Example 3:

# Input: text = "leetcode"
# Output: 0


# Constraints:

# 1 <= text.length <= 104
# text consists of lower case English letters only.
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
    def maxNumberOfBalloons(self, text: str) -> int:
        count = 0

        while True:
            for ch in "balloon":
                if ch not in text:
                    return count
                text = text.replace(ch, "", 1)
            count += 1
```

### Optimal

python
```

from collections import Counter

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = Counter(text)

        return min(
            count['b'],
            count['a'],
            count['l'] // 2,
            count['o'] // 2,
            count['n']
        )
```
