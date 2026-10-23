# Given a list of words, list of  single letters (might be repeating) and score of every character.

# Return the maximum score of any valid set of words formed by using the given letters (words[i] cannot be used two or more times).

# It is not necessary to use all characters in letters and each letter can only be used once. Score of letters 'a', 'b', 'c', ... ,'z' is given by score[0], score[1], ... , score[25] respectively.



# Example 1:

# Input: words = ["dog","cat","dad","good"], letters = ["a","a","c","d","d","d","g","o","o"], score = [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]
# Output: 23
# Explanation:
# Score  a=1, c=9, d=5, g=3, o=2
# Given letters, we can form the words "dad" (5+1+5) and "good" (3+2+2+5) with a score of 23.
# Words "dad" and "dog" only get a score of 21.
# Example 2:

# Input: words = ["xxxz","ax","bx","cx"], letters = ["z","a","b","c","x","x","x"], score = [4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,10]
# Output: 27
# Explanation:
# Score  a=4, b=4, c=4, x=5, z=10
# Given letters, we can form the words "ax" (4+5), "bx" (4+5) and "cx" (4+5) with a score of 27.
# Word "xxxz" only get a score of 25.
# Example 3:

# Input: words = ["leetcode"], letters = ["l","e","t","c","o","d"], score = [0,0,1,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0]
# Output: 0
# Explanation:
# Letter "e" can only be used once.


# Constraints:

# 1 <= words.length <= 14
# 1 <= words[i].length <= 15
# 1 <= letters.length <= 100
# letters[i].length == 1
# score.length == 26
# 0 <= score[i] <= 10
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
# ### Brute Force — Backtracking

python
```
from typing import List
from collections import Counter

class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        available = Counter(letters)

        def backtrack(index):
            if index == len(words):
                return 0

            best = backtrack(index + 1)
            word = words[index]
            freq = Counter(word)
            word_score = sum(score[ord(c) - ord('a')] * count
                             for c, count in freq.items())

            if all(available[c] >= freq[c] for c in freq):
                for c in freq:
                    available[c] -= freq[c]

                best = max(best, word_score + backtrack(index + 1))

                for c in freq:
                    available[c] += freq[c]

            return best

        return backtrack(0)
```

### Optimal — Backtracking with Precomputed Frequencies

python
```
from typing import List
from collections import Counter

class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        available = [0] * 26

        for c in letters:
            available[ord(c) - ord('a')] += 1

        word_freq = []
        word_scores = []

        for word in words:
            freq = [0] * 26
            total = 0

            for c in word:
                idx = ord(c) - ord('a')
                freq[idx] += 1
                total += score[idx]

            word_freq.append(freq)
            word_scores.append(total)

        def backtrack(i):
            if i == len(words):
                return 0

            best = backtrack(i + 1)
            freq = word_freq[i]

            if all(freq[j] <= available[j] for j in range(26)):
                for j in range(26):
                    available[j] -= freq[j]

                best = max(best, word_scores[i] + backtrack(i + 1))

                for j in range(26):
                    available[j] += freq[j]

            return best

        return backtrack(0)
```
