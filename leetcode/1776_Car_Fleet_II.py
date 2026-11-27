# There are n cars traveling at different speeds in the same direction along a one-lane road. You are given an array cars of length n, where cars[i] = [positioni, speedi] represents:

# positioni is the distance between the ith car and the beginning of the road in meters. It is guaranteed that positioni < positioni+1.
# speedi is the initial speed of the ith car in meters per second.
# For simplicity, cars can be considered as points moving along the number line. Two cars collide when they occupy the same position. Once a car collides with another car, they unite and form a single car fleet. The cars in the formed fleet will have the same position and the same speed, which is the initial speed of the slowest car in the fleet.

# Return an array answer, where answer[i] is the time, in seconds, at which the ith car collides with the next car, or -1 if the car does not collide with the next car. Answers within 10-5 of the actual answers are accepted.



# Example 1:

# Input: cars = [[1,2],[2,1],[4,3],[7,2]]
# Output: [1.00000,-1.00000,3.00000,-1.00000]
# Explanation: After exactly one second, the first car will collide with the second car, and form a car fleet with speed 1 m/s. After exactly 3 seconds, the third car will collide with the fourth car, and form a car fleet with speed 2 m/s.
# Example 2:

# Input: cars = [[3,4],[5,4],[6,3],[9,1]]
# Output: [2.00000,1.00000,1.50000,-1.00000]


# Constraints:

# 1 <= cars.length <= 105
# 1 <= positioni, speedi <= 106
# positioni < positioni+1
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
# ### 1. Brute Force Approach

Time Complexity: $O(n^2)$

python

```python
class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        n = len(cars)
        ans = [-1.0] * n

        for i in range(n):
            pos, speed = cars[i]

            for j in range(i + 1, n):
                next_pos, next_speed = cars[j]

                if speed > next_speed:
                    ans[i] = (next_pos - pos) / (speed - next_speed)
                    break

        return ans
```

### 2. Optimal Approach (Monotonic Stack)

O(n) Time | O(n) Spacepython

```python
class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        n = len(cars)
        ans = [-1.0] * n
        stack = []

        for i in range(n - 1, -1, -1):
            pos, speed = cars[i]

            while stack:
                j = stack[-1]
                next_pos, next_speed = cars[j]

                if speed <= next_speed:
                    stack.pop()

                else:
                    time = (next_pos - pos) / (speed - next_speed)

                    if ans[j] == -1 or time <= ans[j]:
                        break

                    stack.pop()

            if stack:
                j = stack[-1]
                ans[i] = (cars[j][0] - pos) / (speed - cars[j][1])

            stack.append(i)

        return ans
```
