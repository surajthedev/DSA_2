# With respect to a given puzzle string, a word is valid if both the following conditions are satisfied:
# word contains the first letter of puzzle.
# For each letter in word, that letter is in puzzle.
# For example, if the puzzle is "abcdefg", then valid words are "faced", "cabbage", and "baggage", while
# invalid words are "beefed" (does not include 'a') and "based" (includes 's' which is not in the puzzle).
# Return an array answer, where answer[i] is the number of words in the given word list words that is valid with respect to the puzzle puzzles[i].


# Example 1:

# Input: words = ["aaaa","asas","able","ability","actt","actor","access"], puzzles = ["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"]
# Output: [1,1,3,2,4,0]
# Explanation:
# 1 valid word for "aboveyz" : "aaaa"
# 1 valid word for "abrodyz" : "aaaa"
# 3 valid words for "abslute" : "aaaa", "asas", "able"
# 2 valid words for "absoryz" : "aaaa", "asas"
# 4 valid words for "actresz" : "aaaa", "asas", "actt", "access"
# There are no valid words for "gaswxyz" cause none of the words in the list contains letter 'g'.
# Example 2:

# Input: words = ["apple","pleas","please"], puzzles = ["aelwxyz","aelpxyz","aelpsxy","saelpxy","xaelpsy"]
# Output: [0,1,3,2,0]


# Constraints:

# 1 <= words.length <= 105
# 4 <= words[i].length <= 50
# 1 <= puzzles.length <= 104
# puzzles[i].length == 7
# words[i] and puzzles[i] consist of lowercase English letters.
# Each puzzles[i] does not contain repeated characters.
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
# ### 1. Brute Force — O(W × P × L)

python
```
class Solution:
    def findNumOfValidWords(self, words: list[str], puzzles: list[str]) -> list[int]:
        ans = []

        for puzzle in puzzles:
            pset = set(puzzle)
            first = puzzle[0]
            count = 0

            for word in words:
                if first in word and all(ch in pset for ch in word):
                    count += 1

            ans.append(count)

        return ans
```

### 2. Optimal Solution — Bitmask + Frequency Map

python
```
from collections import Counter

class Solution:
    def findNumOfValidWords(self, words: list[str], puzzles: list[str]) -> list[int]:
        freq = Counter()

        for word in words:
            mask = 0
            for ch in set(word):
                mask |= 1 << (ord(ch) - ord('a'))
            if mask.bit_count() <= 7:
                freq[mask] += 1

        ans = []

        for puzzle in puzzles:
            first_bit = 1 << (ord(puzzle[0]) - ord('a'))
            mask = 0

            for ch in puzzle:
                mask |= 1 << (ord(ch) - ord('a'))

            sub = mask
            count = 0

            while sub:
                if sub & first_bit:
                    count += freq[sub]
                sub = (sub - 1) & mask

            ans.append(count)

        return ans
```
