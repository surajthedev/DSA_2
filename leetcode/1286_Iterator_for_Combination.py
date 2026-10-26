# Design the CombinationIterator class:

# CombinationIterator(string characters, int combinationLength) Initializes the object with a string characters of sorted distinct lowercase English letters and a number combinationLength as arguments.
# next() Returns the next combination of length combinationLength in lexicographical order.
# hasNext() Returns true if and only if there exists a next combination.


# Example 1:

# Input
# ["CombinationIterator", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
# [["abc", 2], [], [], [], [], [], []]
# Output
# [null, "ab", true, "ac", true, "bc", false]

# Explanation
# CombinationIterator itr = new CombinationIterator("abc", 2);
# itr.next();    // return "ab"
# itr.hasNext(); // return True
# itr.next();    // return "ac"
# itr.hasNext(); // return True
# itr.next();    // return "bc"
# itr.hasNext(); // return False


# Constraints:

# 1 <= combinationLength <= characters.length <= 15
# All the characters of characters are unique.
# At most 104 calls will be made to next and hasNext.
# It is guaranteed that all calls of the function next are valid.
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
# ### Brute Force

python

```

from itertools import combinations

class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.combinations = [
            ''.join(c) for c in combinations(characters, combinationLength)
        ]
        self.index = 0

    def next(self) -> str:
        result = self.combinations[self.index]
        self.index += 1
        return result

    def hasNext(self) -> bool:
        return self.index < len(self.combinations)
```

### Optimal (Backtracking + Lazy Generation)

python

```

class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.characters = characters
        self.k = combinationLength
        self.n = len(characters)
        self.indices = list(range(combinationLength))
        self.finished = False

    def next(self) -> str:
        result = ''.join(self.characters[i] for i in self.indices)

        i = self.k - 1
        while i >= 0 and self.indices[i] == self.n - self.k + i:
            i -= 1

        if i < 0:
            self.finished = True
        else:
            self.indices[i] += 1
            for j in range(i + 1, self.k):
                self.indices[j] = self.indices[j - 1] + 1

        return result

    def hasNext(self) -> bool:
        return not self.finished
```
