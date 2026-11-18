# You are given a string s of even length consisting of digits from 0 to 9, and two integers a and b.

# You can apply either of the following two operations any number of times and in any order on s:

# Add a to all odd indices of s (0-indexed). Digits post 9 are cycled back to 0. For example, if s = "3456" and a = 5, s becomes "3951".
# Rotate s to the right by b positions. For example, if s = "3456" and b = 1, s becomes "6345".
# Return the lexicographically smallest string you can obtain by applying the above operations any number of times on s.

# A string a is lexicographically smaller than a string b (of the same length) if in the first position where a and b differ, string a has a letter that appears earlier in the alphabet than the corresponding letter in b. For example, "0158" is lexicographically smaller than "0190" because the first position they differ is at the third letter, and '5' comes before '9'.



# Example 1:

# Input: s = "5525", a = 9, b = 2
# Output: "2050"
# Explanation: We can apply the following operations:
# Start:  "5525"
# Rotate: "2555"
# Add:    "2454"
# Add:    "2353"
# Rotate: "5323"
# Add:    "5222"
# Add:    "5121"
# Rotate: "2151"
# Add:    "2050"​​​​​
# There is no way to obtain a string that is lexicographically smaller than "2050".
# Example 2:

# Input: s = "74", a = 5, b = 1
# Output: "24"
# Explanation: We can apply the following operations:
# Start:  "74"
# Rotate: "47"
# ​​​​​​​Add:    "42"
# ​​​​​​​Rotate: "24"​​​​​​​​​​​​
# There is no way to obtain a string that is lexicographically smaller than "24".
# Example 3:

# Input: s = "0011", a = 4, b = 2
# Output: "0011"
# Explanation: There are no sequence of operations that will give us a lexicographically smaller string than "0011".


# Constraints:

# 2 <= s.length <= 100
# s.length is even.
# s consists of digits from 0 to 9 only.
# 1 <= a <= 9
# # 1 <= b <= s.length - 1
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
#Optimal approach mein bug tha. Correct solution ke liye BFS + Visited Set use karo. Ye saare possible states explore karega aur guaranteed lexicographically smallest string return karega.

### 1. Brute Force Approach (BFS)

python

```python
from collections import deque

class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        q = deque([s])
        visited = {s}
        ans = s

        while q:
            curr = q.popleft()
            ans = min(ans, curr)

            # Operation 1: Add a to odd indices
            temp = list(curr)

            for i in range(1, len(s), 2):
                temp[i] = str((int(temp[i]) + a) % 10)

            new_s = "".join(temp)

            if new_s not in visited:
                visited.add(new_s)
                q.append(new_s)

            # Operation 2: Rotate right by b
            new_s = curr[-b:] + curr[:-b]

            if new_s not in visited:
                visited.add(new_s)
                q.append(new_s)

        return ans
```

### 2. Optimal Approach (Mathematical Enumeration)

python

```python
class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        n = len(s)
        ans = s

        def add(s, inc, start):
            s = list(s)

            for i in range(start, n, 2):
                s[i] = str((int(s[i]) + inc) % 10)

            return "".join(s)

        rotations = n // __import__('math').gcd(n, b)

        for r in range(rotations):
            curr = s[-(r * b % n):] + s[:n - (r * b % n)] if r * b % n else s

            for x in range(10):
                temp = add(curr, (x * a) % 10, 1)

                if b % 2 == 1:
                    for y in range(10):
                        candidate = add(temp, (y * a) % 10, 0)
                        ans = min(ans, candidate)
                else:
                    ans = min(ans, temp)

        return ans
```

Complexity:

- Brute Force: `O(10^n × n)` worst case.
- Optimal: `O(n × 100)` time, `O(n)` space.
