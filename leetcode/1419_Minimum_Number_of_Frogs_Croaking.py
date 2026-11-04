# You are given the string croakOfFrogs, which represents a combination of the string "croak" from different frogs, that is, multiple frogs can croak at the same time, so multiple "croak" are mixed.

# Return the minimum number of different frogs to finish all the croaks in the given string.

# A valid "croak" means a frog is printing five letters 'c', 'r', 'o', 'a', and 'k' sequentially. The frogs have to print all five letters to finish a croak. If the given string is not a combination of a valid "croak" return -1.



# Example 1:

# Input: croakOfFrogs = "croakcroak"
# Output: 1
# Explanation: One frog yelling "croak" twice.
# Example 2:

# Input: croakOfFrogs = "crcoakroak"
# Output: 2
# Explanation: The minimum number of frogs is two.
# The first frog could yell "crcoakroak".
# The second frog could yell later "crcoakroak".
# Example 3:

# Input: croakOfFrogs = "croakcrook"
# Output: -1
# Explanation: The given string is an invalid combination of "croak" from different frogs.


# Constraints:

# 1 <= croakOfFrogs.length <= 105
# croakOfFrogs is either 'c', 'r', 'o', 'a', or 'k'.
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
# ### 1. Brute Force Approach

python

```python
class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        pattern = "croak"
        frogs = []

        for ch in croakOfFrogs:
            found = False

            if ch == 'c':
                for i in range(len(frogs)):
                    if frogs[i] == 0:
                        frogs[i] = 1
                        found = True
                        break

                if not found:
                    frogs.append(1)

            else:
                expected = pattern[0]

                for i in range(len(frogs)):
                    if frogs[i] > 0 and pattern[frogs[i]] == ch:
                        frogs[i] += 1

                        if frogs[i] == 5:
                            frogs[i] = 0

                        found = True
                        break

                if not found:
                    return -1

        if any(frog != 0 for frog in frogs):
            return -1

        return len(frogs)
```

Time Complexity: $O(n^2)$

Space Complexity: $O(n)$

### 2. Optimal Approach (Frequency Counting)

python

```python
class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        count = [0] * 5

        frogs = 0
        max_frogs = 0

        for ch in croakOfFrogs:
            if ch == 'c':
                count[0] += 1
                frogs += 1
                max_frogs = max(max_frogs, frogs)

            elif ch == 'r':
                count[0] -= 1
                count[1] += 1

            elif ch == 'o':
                count[1] -= 1
                count[2] += 1

            elif ch == 'a':
                count[2] -= 1
                count[3] += 1

            elif ch == 'k':
                count[3] -= 1
                frogs -= 1

            if min(count) < 0:
                return -1

        if frogs != 0 or any(count):
            return -1

        return max_frogs
```

Time Complexity: $O(n)$

Space Complexity: $O(1)$
