# A delivery company wants to build a new service center in a new city. The company knows the positions of all the customers in this city on a 2D-Map and wants to build the new center in a position such that the sum of the euclidean distances to all customers is minimum.

# Given an array positions where positions[i] = [xi, yi] is the position of the ith customer on the map, return the minimum sum of the euclidean distances to all customers.

# In other words, you need to choose the position of the service center [xcentre, ycentre] such that the following formula is minimized:


# Answers within 10-5 of the actual value will be accepted.



# Example 1:


# Input: positions = [[0,1],[1,0],[1,2],[2,1]]
# Output: 4.00000
# Explanation: As shown, you can see that choosing [xcentre, ycentre] = [1, 1] will make the distance to each customer = 1, the sum of all distances is 4 which is the minimum possible we can achieve.
# Example 2:


# Input: positions = [[1,1],[3,3]]
# Output: 2.82843
# Explanation: The minimum possible sum of distances = sqrt(2) + sqrt(2) = 2.82843


# Constraints:

# 1 <= positions.length <= 50
# positions[i].length == 2
# 0 <= xi, yi <= 100
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
# ### 1. Brute Force (Grid Search)

python

```python
class Solution:
    def getMinDistSum(self, positions: List[List[int]]) -> float:
        ans = float('inf')

        for x in range(101):
            for y in range(101):
                total = 0

                for px, py in positions:
                    total += ((x - px) ** 2 + (y - py) ** 2) ** 0.5

                ans = min(ans, total)

        return ans
```

### 2. Optimal Solution (Gradient Descent)

python

```python
class Solution:
    def getMinDistSum(self, positions: List[List[int]]) -> float:
        x = sum(p[0] for p in positions) / len(positions)
        y = sum(p[1] for p in positions) / len(positions)

        step = 100.0

        while step > 1e-7:
            improved = True

            while improved:
                improved = False

                for dx, dy in [(step, 0), (-step, 0),
                               (0, step), (0, -step)]:

                    nx = x + dx
                    ny = y + dy

                    old_dist = sum(
                        ((x - px) ** 2 + (y - py) ** 2) ** 0.5
                        for px, py in positions
                    )

                    new_dist = sum(
                        ((nx - px) ** 2 + (ny - py) ** 2) ** 0.5
                        for px, py in positions
                    )

                    if new_dist < old_dist:
                        x, y = nx, ny
                        improved = True

            step /= 2

        return sum(
            ((x - px) ** 2 + (y - py) ** 2) ** 0.5
            for px, py in positions
        )
```
