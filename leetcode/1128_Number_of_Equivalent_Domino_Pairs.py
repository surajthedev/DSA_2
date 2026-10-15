# Given a list of dominoes, dominoes[i] = [a, b] is equivalent to dominoes[j] = [c, d] if and only if either (a == c and b == d), or (a == d and b == c) - that is, one domino can be rotated to be equal to another domino.

# Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length, and dominoes[i] is equivalent to dominoes[j].



# Example 1:

# Input: dominoes = [[1,2],[2,1],[3,4],[5,6]]
# Output: 1
# Example 2:

# Input: dominoes = [[1,2],[1,2],[1,1],[1,2],[2,2]]
# Output: 3


# Constraints:

# 1 <= dominoes.length <= 4 * 104
# dominoes[i].length == 2
# 1 <= dominoes[i][j] <= 9
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
# ### Brute Force — O(n²)

python
```
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        n = len(dominoes)
        ans = 0

        for i in range(n):
            for j in range(i + 1, n):
                a, b = dominoes[i]
                c, d = dominoes[j]

                if (a == c and b == d) or (a == d and b == c):
                    ans += 1

        return ans
```

### Optimal — Hash Map — O(n)

python
```
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        count = {}
        ans = 0

        for a, b in dominoes:
            key = (min(a, b), max(a, b))

            ans += count.get(key, 0)
            count[key] = count.get(key, 0) + 1

        return ans
```
