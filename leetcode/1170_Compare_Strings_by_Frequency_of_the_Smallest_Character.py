# Let the function f(s) be the frequency of the lexicographically smallest character in a non-empty string s. For example, if s = "dcce" then f(s) = 2 because the lexicographically smallest character is 'c', which has a frequency of 2.

# You are given an array of strings words and another array of query strings queries. For each query queries[i], count the number of words in words such that f(queries[i]) < f(W) for each W in words.

# Return an integer array answer, where each answer[i] is the answer to the ith query.



# Example 1:

# Input: queries = ["cbd"], words = ["zaaaz"]
# Output: [1]
# Explanation: On the first query we have f("cbd") = 1, f("zaaaz") = 3 so f("cbd") < f("zaaaz").
# Example 2:

# Input: queries = ["bbb","cc"], words = ["a","aa","aaa","aaaa"]
# Output: [1,2]
# Explanation: On the first query only f("bbb") < f("aaaa"). On the second query both f("aaa") and f("aaaa") are both > f("cc").


# Constraints:

# 1 <= queries.length <= 2000
# 1 <= words.length <= 2000
# 1 <= queries[i].length, words[i].length <= 10
# queries[i][j], words[i][j] consist of lowercase English letters.
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
# ### 1. Brute Force — O(Q × W × L)

python
```
class Solution:
    def numSmallerByFrequency(self, queries: list[str], words: list[str]) -> list[int]:

        def f(s):
            smallest = min(s)
            return s.count(smallest)

        answer = []

        for q in queries:
            count = 0

            for w in words:
                if f(q) < f(w):
                    count += 1

            answer.append(count)

        return answer
```

### 2. Optimal Solution — O(W × L + Q log W)

python
```
from bisect import bisect_right

class Solution:
    def numSmallerByFrequency(self, queries: list[str], words: list[str]) -> list[int]:

        def f(s):
            smallest = min(s)
            return s.count(smallest)

        word_freq = sorted(f(w) for w in words)
        n = len(words)

        answer = []

        for q in queries:
            freq = f(q)
            idx = bisect_right(word_freq, freq)
            answer.append(n - idx)

        return answer
```
