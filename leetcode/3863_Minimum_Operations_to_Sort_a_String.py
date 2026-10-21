# You are given a string s consisting of lowercase English letters.

# In one operation, you can select any substring of s that is not the entire string and sort it in non-descending alphabetical order.

# Return the minimum number of operations required to make s sorted in non-descending order. If it is not possible, return -1.



# Example 1:

# Input: s = "dog"

# Output: 1

# Explanation:​​​​​​​

# Sort substring "og" to "go".
# Now, s = "dgo", which is sorted in ascending order. Thus, the answer is 1.
# Example 2:

# Input: s = "card"

# Output: 2

# Explanation:

# Sort substring "car" to "acr", so s = "acrd".
# Sort substring "rd" to "dr", making s = "acdr", which is sorted in ascending order. Thus, the answer is 2.
# Example 3:

# Input: s = "gf"

# Output: -1

# Explanation:

# It is impossible to sort s under the given constraints. Thus, the answer is -1.


# Constraints:

# 1 <= s.length <= 105
# s consists of only lowercase English letters.
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
class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)

        if s == ''.join(sorted(s)):
            return 0

        if s[0] == max(s) and s[-1] == min(s):
            return -1

        for i in range(n):
            for j in range(i + 1, n):
                t = s[:i] + ''.join(sorted(s[i:j + 1])) + s[j + 1:]
                if t == ''.join(sorted(s)):
                    return 1

        return 2
```

### Optimal Solution

python
```
    Bhai, galti `s[0] < s[-1]` wali condition mein thi. `"card"` mein first character `c` minimum nahi hai aur last character `d` maximum nahi hai, isliye answer `2` hona chahiye.

    ### Correct Python Solution — LeetCode 3863

    python
    ```
    class Solution:
        def minOperations(self, s: str) -> int:
            n = len(s)

            if s == ''.join(sorted(s)):
                return 0

            if n == 2:
                return -1

            mn = min(s)
            mx = max(s)

            if s[0] == mn or s[-1] == mx:
                return 1

            if s[0] != mx or s[-1] != mn:
                return 2

            if s.count(mn) > 1 or s.count(mx) > 1:
                return 2

            return 3
    ```
```
