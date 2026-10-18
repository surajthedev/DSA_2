# You are given a string s and array queries where queries[i] = [lefti, righti, ki]. We may rearrange the substring s[lefti...righti] for each query and then choose up to ki of them to replace with any lowercase English letter.

# If the substring is possible to be a palindrome string after the operations above, the result of the query is true. Otherwise, the result is false.

# Return a boolean array answer where answer[i] is the result of the ith query queries[i].

# Note that each letter is counted individually for replacement, so if, for example s[lefti...righti] = "aaa", and ki = 2, we can only replace two of the letters. Also, note that no query modifies the initial string s.



# Example :

# Input: s = "abcda", queries = [[3,3,0],[1,2,0],[0,3,1],[0,3,2],[0,4,1]]
# Output: [true,false,false,true,true]
# Explanation:
# queries[0]: substring = "d", is palidrome.
# queries[1]: substring = "bc", is not palidrome.
# queries[2]: substring = "abcd", is not palidrome after replacing only 1 character.
# queries[3]: substring = "abcd", could be changed to "abba" which is palidrome. Also this can be changed to "baab" first rearrange it "bacd" then replace "cd" with "ab".
# queries[4]: substring = "abcda", could be changed to "abcba" which is palidrome.
# Example 2:

# Input: s = "lyb", queries = [[0,1,0],[2,2,1]]
# Output: [false,true]


# Constraints:
# 1 <= s.length, queries.length <= 105
# 0 <= lefti <= righti < s.length
# 0 <= ki <= s.length
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
# ### 1. Brute Force — O(n × q)

python
```
class Solution:
    def canMakePaliQueries(self, s: str, queries: list[list[int]]) -> list[bool]:
        ans = []

        for left, right, k in queries:
            freq = [0] * 26

            for ch in s[left:right + 1]:
                freq[ord(ch) - ord('a')] += 1

            odd = sum(count % 2 for count in freq)
            ans.append(odd // 2 <= k)

        return ans
```

### 2. Optimal Solution — O(n + q)

python
```
class Solution:
    def canMakePaliQueries(self, s: str, queries: list[list[int]]) -> list[bool]:
        prefix = [0]

        for ch in s:
            prefix.append(prefix[-1] ^ (1 << (ord(ch) - ord('a'))))

        ans = []

        for left, right, k in queries:
            mask = prefix[right + 1] ^ prefix[left]
            odd = mask.bit_count()
            ans.append(odd // 2 <= k)

        return ans
```
