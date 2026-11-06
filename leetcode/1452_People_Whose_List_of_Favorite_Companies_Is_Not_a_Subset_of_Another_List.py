# Given the array favoriteCompanies where favoriteCompanies[i] is the list of favorites companies for the ith person (indexed from 0).

# Return the indices of people whose list of favorite companies is not a subset of any other list of favorites companies. You must return the indices in increasing order.



# Example 1:

# Input: favoriteCompanies = [["leetcode","google","facebook"],["google","microsoft"],["google","facebook"],["google"],["amazon"]]
# Output: [0,1,4]
# Explanation:
# Person with index=2 has favoriteCompanies[2]=["google","facebook"] which is a subset of favoriteCompanies[0]=["leetcode","google","facebook"] corresponding to the person with index 0.
# Person with index=3 has favoriteCompanies[3]=["google"] which is a subset of favoriteCompanies[0]=["leetcode","google","facebook"] and favoriteCompanies[1]=["google","microsoft"].
# Other lists of favorite companies are not a subset of another list, therefore, the answer is [0,1,4].
# Example 2:

# Input: favoriteCompanies = [["leetcode","google","facebook"],["leetcode","amazon"],["facebook","google"]]
# Output: [0,1]
# Explanation: In this case favoriteCompanies[2]=["facebook","google"] is a subset of favoriteCompanies[0]=["leetcode","google","facebook"], therefore, the answer is [0,1].
# Example 3:

# Input: favoriteCompanies = [["leetcode"],["google"],["facebook"],["amazon"]]
# Output: [0,1,2,3]


# Constraints:

# 1 <= favoriteCompanies.length <= 100
# 1 <= favoriteCompanies[i].length <= 500
# 1 <= favoriteCompanies[i][j].length <= 20
# All strings in favoriteCompanies[i] are distinct.
# All lists of favorite companies are distinct, that is, If we sort alphabetically each list then favoriteCompanies[i] != favoriteCompanies[j].
# All strings consist of lowercase English letters only.
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
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        n = len(favoriteCompanies)
        ans = []

        for i in range(n):
            is_subset = False
            current = set(favoriteCompanies[i])

            for j in range(n):
                if i == j:
                    continue

                other = set(favoriteCompanies[j])

                if current.issubset(other):
                    is_subset = True
                    break

            if not is_subset:
                ans.append(i)

        return ans
```

Time Complexity: $O(N^2 \times M)$

Space Complexity: $O(N \times M)$

### 2. Optimal — Python (Set + Sorting)

python

```python
class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        companies = [set(company) for company in favoriteCompanies]

        indices = sorted(
            range(len(companies)),
            key=lambda i: len(companies[i]),
            reverse=True
        )

        ans = []

        for i in range(len(companies)):
            is_subset = False

            for j in indices:
                if i == j:
                    continue

                if len(companies[i]) < len(companies[j]):
                    if companies[i].issubset(companies[j]):
                        is_subset = True
                        break

            if not is_subset:
                ans.append(i)

        return sorted(ans)
```

Time Complexity: $O(N^2 \times M)$ worst case

Space Complexity: $O(N \times M)$
