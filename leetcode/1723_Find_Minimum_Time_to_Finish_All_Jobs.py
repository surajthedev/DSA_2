# You are given an integer array jobs, where jobs[i] is the amount of time it takes to complete the ith job.

# There are k workers that you can assign jobs to. Each job should be assigned to exactly one worker. The working time of a worker is the sum of the time it takes to complete all jobs assigned to them. Your goal is to devise an optimal assignment such that the maximum working time of any worker is minimized.

# Return the minimum possible maximum working time of any assignment.



# Example 1:

# Input: jobs = [3,2,3], k = 3
# Output: 3
# Explanation: By assigning each person one job, the maximum time is 3.
# Example 2:

# Input: jobs = [1,2,4,7,8], k = 2
# Output: 11
# Explanation: Assign the jobs the following way:
# Worker 1: 1, 2, 8 (working time = 1 + 2 + 8 = 11)
# Worker 2: 4, 7 (working time = 4 + 7 = 11)
# The maximum working time is 11.


# Constraints:

# 1 <= k <= jobs.length <= 12
# 1 <= jobs[i] <= 107
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
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        workers = [0] * k
        ans = float('inf')

        def backtrack(index):
            nonlocal ans

            if index == len(jobs):
                ans = min(ans, max(workers))
                return

            for i in range(k):
                workers[i] += jobs[index]

                if workers[i] < ans:
                    backtrack(index + 1)

                workers[i] -= jobs[index]

                if workers[i] == 0:
                    break

        backtrack(0)
        return ans
```

### 2. Optimal Approach (Backtracking + Binary Search)

python

```python
from typing import List

class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        jobs.sort(reverse=True)

        left = max(jobs)
        right = sum(jobs)

        def canAssign(limit):
            workers = [0] * k

            def backtrack(index):
                if index == len(jobs):
                    return True

                job = jobs[index]
                seen = set()

                for i in range(k):
                    if workers[i] + job > limit:
                        continue

                    if workers[i] in seen:
                        continue

                    seen.add(workers[i])
                    workers[i] += job

                    if backtrack(index + 1):
                        return True

                    workers[i] -= job

                    if workers[i] == 0:
                        break

                return False

            return backtrack(0)

        while left < right:
            mid = (left + right) // 2

            if canAssign(mid):
                right = mid
            else:
                left = mid + 1

        return left
```

Time Complexity:

- Brute Force: $O(k^n)$ worst case.
- Optimal: $O(\log(\sum jobs) \times k^n)$ worst case.

Space Complexity: $O(n+k)$ for recursion and worker storage.
