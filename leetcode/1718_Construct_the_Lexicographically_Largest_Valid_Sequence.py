# Given an integer n, find a sequence with elements in the range [1, n] that satisfies all of the following:

# The integer 1 occurs once in the sequence.
# Each integer between 2 and n occurs twice in the sequence.
# For every integer i between 2 and n, the distance between the two occurrences of i is exactly i.
# The distance between two numbers on the sequence, a[i] and a[j], is the absolute difference of their indices, |j - i|.

# Return the lexicographically largest sequence. It is guaranteed that under the given constraints, there is always a solution.

# A sequence a is lexicographically larger than a sequence b (of the same length) if in the first position where a and b differ, sequence a has a number greater than the corresponding number in b. For example, [0,1,9,0] is lexicographically larger than [0,1,5,6] because the first position they differ is at the third number, and 9 is greater than 5.



# Example 1:

# Input: n = 3
# Output: [3,1,2,3,2]
# Explanation: [2,3,2,1,3] is also a valid sequence, but [3,1,2,3,2] is the lexicographically largest valid sequence.
# Example 2:

# Input: n = 5
# Output: [5,3,1,4,3,5,2,4,2]


# Constraints:

# 1 <= n <= 20
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
#
#
#
#
# ### 1. Brute Force Approach (Backtracking)

python

```python
from typing import List

class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        size = 2 * n - 1
        ans = [0] * size
        used = [False] * (n + 1)

        def backtrack(index):
            if index == size:
                return True

            if ans[index] != 0:
                return backtrack(index + 1)

            for num in range(1, n + 1):
                if used[num]:
                    continue

                if num == 1:
                    ans[index] = 1
                    used[num] = True

                    if backtrack(index + 1):
                        return True

                    ans[index] = 0
                    used[num] = False

                else:
                    j = index + num

                    if j < size and ans[j] == 0:
                        ans[index] = num
                        ans[j] = num
                        used[num] = True

                        if backtrack(index + 1):
                            return True

                        ans[index] = 0
                        ans[j] = 0
                        used[num] = False

            return False

        backtrack(0)
        return ans
```

### 2. Optimal Approach (Greedy + Backtracking)

python

```python
from typing import List

class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        ans = [0] * (2 * n - 1)
        used = [False] * (n + 1)

        def backtrack(index):
            while index < len(ans) and ans[index] != 0:
                index += 1

            if index == len(ans):
                return True

            for num in range(n, 0, -1):
                if used[num]:
                    continue

                if num == 1:
                    ans[index] = 1
                    used[num] = True

                    if backtrack(index + 1):
                        return True

                    ans[index] = 0
                    used[num] = False

                else:
                    j = index + num

                    if j < len(ans) and ans[j] == 0:
                        ans[index] = num
                        ans[j] = num
                        used[num] = True

                        if backtrack(index + 1):
                            return True

                        ans[index] = 0
                        ans[j] = 0
                        used[num] = False

            return False

        backtrack(0)
        return ans
```

Time Complexity: $O(n!)$ worst case (backtracking)

Space Complexity: $O(n)$ auxiliary space.
