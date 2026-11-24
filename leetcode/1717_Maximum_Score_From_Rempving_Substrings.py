# You are given a string s and two integers x and y. You can perform two types of operations any number of times.

# Remove substring "ab" and gain x points.
# For example, when removing "ab" from "cabxbae" it becomes "cxbae".
# Remove substring "ba" and gain y points.
# For example, when removing "ba" from "cabxbae" it becomes "cabxe".
# Return the maximum points you can gain after applying the above operations on s.



# Example 1:

# Input: s = "cdbcbbaaabab", x = 4, y = 5
# Output: 19
# Explanation:
# - Remove the "ba" underlined in "cdbcbbaaabab". Now, s = "cdbcbbaaab" and 5 points are added to the score.
# - Remove the "ab" underlined in "cdbcbbaaab". Now, s = "cdbcbbaa" and 4 points are added to the score.
# - Remove the "ba" underlined in "cdbcbbaa". Now, s = "cdbcba" and 5 points are added to the score.
# - Remove the "ba" underlined in "cdbcba". Now, s = "cdbc" and 5 points are added to the score.
# Total score = 5 + 4 + 5 + 5 = 19.
# Example 2:

# Input: s = "aabbaaxybbaabb", x = 5, y = 4
# Output: 20


# Constraints:

# 1 <= s.length <= 105
# 1 <= x, y <= 104
# s consists of lowercase English letters.
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
#
#
#
# ### 1. Brute Force Approach

python

```python
class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        ans = 0

        while "ab" in s or "ba" in s:
            if x >= y:
                if "ab" in s:
                    s = s.replace("ab", "", 1)
                    ans += x
                elif "ba" in s:
                    s = s.replace("ba", "", 1)
                    ans += y
            else:
                if "ba" in s:
                    s = s.replace("ba", "", 1)
                    ans += y
                elif "ab" in s:
                    s = s.replace("ab", "", 1)
                    ans += x

        return ans
```

Time Complexity: $O(n^2)$

Space Complexity: $O(n)$

### 2. Optimal Approach (Greedy + Stack)

python

```python
class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        if x < y:
            s = s.replace("a", "#").replace("b", "a").replace("#", "b")
            x, y = y, x

        def remove(s, first, second, points):
            stack = []
            score = 0

            for ch in s:
                if stack and stack[-1] == first and ch == second:
                    stack.pop()
                    score += points
                else:
                    stack.append(ch)

            return "".join(stack), score

        s, ans = remove(s, 'a', 'b', x)
        s, score = remove(s, 'b', 'a', y)

        return ans + score
```

Time Complexity: $O(n)$

Space Complexity: $O(n)$
