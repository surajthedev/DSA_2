# Given a string s. Return all the words vertically in the same order in which they appear in s.
# Words are returned as a list of strings, complete with spaces when is necessary. (Trailing spaces are not allowed).
# Each word would be put on only one column and that in one column there will be only one word.



# Example 1:

# Input: s = "HOW ARE YOU"
# Output: ["HAY","ORO","WEU"]
# Explanation: Each word is printed vertically.
#  "HAY"
#  "ORO"
#  "WEU"
# Example 2:

# Input: s = "TO BE OR NOT TO BE"
# Output: ["TBONTB","OEROOE","   T"]
# Explanation: Trailing spaces is not allowed.
# "TBONTB"
# "OEROOE"
# "   T"
# Example 3:

# Input: s = "CONTEST IS COMING"
# Output: ["CIC","OSO","N M","T I","E N","S G","T"]


# Constraints:

# 1 <= s.length <= 200
# s contains only upper case English letters.
# It's guaranteed that there is only one space between 2 words.
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
# ### 1. Brute Force

python

```

class Solution:
    def printVertically(self, s: str) -> list[str]:
        words = s.split(" ")
        max_len = max(len(word) for word in words)
        result = []

        for i in range(max_len):
            row = ""

            for j in range(len(words)):
                if i < len(words[j]):
                    row += words[j][i]
                else:
                    row += " "

            result.append(row.rstrip())

        return result
```

### 2. Optimal Solution

python

```

class Solution:
    def printVertically(self, s: str) -> list[str]:
        words = s.split()
        result = []

        for i in range(max(map(len, words))):
            result.append(
                "".join(word[i] if i < len(word) else " " for word in words).rstrip()
            )

        return result
```
