# A string s is called happy if it satisfies the following conditions:

# s only contains the letters 'a', 'b', and 'c'.
# s does not contain any of "aaa", "bbb", or "ccc" as a substring.
# s contains at most a occurrences of the letter 'a'.
# s contains at most b occurrences of the letter 'b'.
# s contains at most c occurrences of the letter 'c'.
# Given three integers a, b, and c, return the longest possible happy string. If there are multiple longest happy strings, return any of them. If there is no such string, return the empty string "".

# A substring is a contiguous sequence of characters within a string.



# Example 1:

# Input: a = 1, b = 1, c = 7
# Output: "ccaccbcc"
# Explanation: "ccbccacc" would also be a correct answer.
# Example 2:

# Input: a = 7, b = 1, c = 0
# Output: "aabaa"
# Explanation: It is the only correct answer in this case.


# Constraints:

# 0 <= a, b, c <= 100
# a + b + c > 0a
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
# ### Brute Force

python

```python
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        from functools import lru_cache

        @lru_cache(None)
        def solve(a, b, c, last, count):
            ans = ""

            for ch, rem in [('a', a), ('b', b), ('c', c)]:
                if rem == 0:
                    continue

                if ch == last and count == 2:
                    continue

                na, nb, nc = a, b, c

                if ch == 'a':
                    na -= 1
                elif ch == 'b':
                    nb -= 1
                else:
                    nc -= 1

                new_count = count + 1 if ch == last else 1

                candidate = ch + solve(
                    na, nb, nc, ch, new_count
                )

                if len(candidate) > len(ans):
                    ans = candidate

            return ans

        return solve(a, b, c, '', 0)
```

### Optimal (Greedy + Max Heap)

python

```python
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        import heapq

        heap = []

        for count, ch in [(a, 'a'), (b, 'b'), (c, 'c')]:
            if count > 0:
                heapq.heappush(heap, (-count, ch))

        ans = []

        while heap:
            count, ch = heapq.heappop(heap)

            if len(ans) >= 2 and ans[-1] == ans[-2] == ch:
                if not heap:
                    break

                count2, ch2 = heapq.heappop(heap)

                ans.append(ch2)
                count2 += 1

                if count2 < 0:
                    heapq.heappush(heap, (count2, ch2))

                heapq.heappush(heap, (count, ch))
            else:
                ans.append(ch)
                count += 1

                if count < 0:
                    heapq.heappush(heap, (count, ch))

        return ''.join(ans)
```
