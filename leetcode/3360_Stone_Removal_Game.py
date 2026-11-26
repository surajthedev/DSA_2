# Alice and Bob are playing a game where they take turns removing stones from a pile, with Alice going first.

# Alice starts by removing exactly 10 stones on her first turn.
# For each subsequent turn, each player removes exactly 1 fewer stone than the previous opponent.
# The player who cannot make a move loses the game.

# Given a positive integer n, return true if Alice wins the game and false otherwise.



# Example 1:

# Input: n = 12

# Output: true

# Explanation:

# Alice removes 10 stones on her first turn, leaving 2 stones for Bob.
# Bob cannot remove 9 stones, so Alice wins.
# Example 2:

# Input: n = 1

# Output: false

# Explanation:

# Alice cannot remove 10 stones, so Alice loses.


# Constraints:

# 1 <= n <= 50
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
#```python
class Solution:
    # Brute Force: simulate the game
    def canAliceWin_brute(self, n: int) -> bool:
        stones = 10
        alice_turn = True
        while True:
            if n < stones:
                # current player can't move -> loses
                return not alice_turn
            n -= stones
            stones -= 1
            alice_turn = not alice_turn

    # Optimal: precompute / O(1) using constant-length game (max 10 moves)
    def canAliceWin(self, n: int) -> bool:
        # cumulative stones removed after k moves: 10, 19, 27, 34, 40, 45, 49, 52, 54, 55
        # Alice wins if the number of moves made is odd
        thresholds = [10, 19, 27, 34, 40, 45, 49, 52, 54, 55]
        moves = 0
        for t in thresholds:
            if n >= t:
                moves += 1
            else:
                break
        return moves % 2 == 1
```
