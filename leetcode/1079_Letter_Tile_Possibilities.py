# You have n  tiles, where each tile has one letter tiles[i] printed on it.

# Return the number of possible non-empty sequences of letters you can make using the letters printed on those tiles.



# Example 1:

# Input: tiles = "AAB"
# Output: 8
# Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".
# Example 2:

# Input: tiles = "AAABBC"
# Output: 188
# Example 3:

# Input: tiles = "V"
# Output: 1


# Constraints:

# 1 <= tiles.length <= 7
# tiles consists of uppercase English letters.
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
    def numTilePossibilities(self, tiles: str) -> int:
        sequences = set()

        def backtrack(path, remaining):
            if path:
                sequences.add(path)

            for i in range(len(remaining)):
                backtrack(
                    path + remaining[i],
                    remaining[:i] + remaining[i + 1:]
                )

        backtrack("", tiles)
        return len(sequences)
```

### Optimal (Backtracking + Frequency Count)

python
```
from collections import Counter

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        count = Counter(tiles)

        def backtrack():
            total = 0

            for char in count:
                if count[char] > 0:
                    count[char] -= 1
                    total += 1 + backtrack()
                    count[char] += 1

            return total

        return backtrack()
```
