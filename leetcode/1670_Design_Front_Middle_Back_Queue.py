# Design a queue that supports push and pop operations in the front, middle, and back.

# Implement the FrontMiddleBackQueue class:

# FrontMiddleBackQueue() Initializes the queue.
# void pushFront(int val) Adds val to the front of the queue.
# void pushMiddle(int val) Adds val to the middle of the queue.
# void pushBack(int val) Adds val to the back of the queue.
# int popFront() Removes the front element of the queue and returns it. If the queue is empty, return -1.
# int popMiddle() Removes the middle element of the queue and returns it. If the queue is empty, return -1.
# int popBack() Removes the back element of the queue and returns it. If the queue is empty, return -1.
# Notice that when there are two middle position choices, the operation is performed on the frontmost middle position choice. For example:

# Pushing 6 into the middle of [1, 2, 3, 4, 5] results in [1, 2, 6, 3, 4, 5].
# Popping the middle from [1, 2, 3, 4, 5, 6] returns 3 and results in [1, 2, 4, 5, 6].


# Example 1:

# Input:
# ["FrontMiddleBackQueue", "pushFront", "pushBack", "pushMiddle", "pushMiddle", "popFront", "popMiddle", "popMiddle", "popBack", "popFront"]
# [[], [1], [2], [3], [4], [], [], [], [], []]
# Output:
# [null, null, null, null, null, 1, 3, 4, 2, -1]

# Explanation:
# FrontMiddleBackQueue q = new FrontMiddleBackQueue();
# q.pushFront(1);   // [1]
# q.pushBack(2);    // [1, 2]
# q.pushMiddle(3);  // [1, 3, 2]
# q.pushMiddle(4);  // [1, 4, 3, 2]
# q.popFront();     // return 1 -> [4, 3, 2]
# q.popMiddle();    // return 3 -> [4, 2]
# q.popMiddle();    // return 4 -> [2]
# q.popBack();      // return 2 -> []
# q.popFront();     // return -1 -> [] (The queue is empty)


# Constraints:

# 1 <= val <= 109
# At most 1000 calls will be made to pushFront, pushMiddle, pushBack, popFront, popMiddle, and popBack.
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
# ### 1. Brute Force Approach (Using List)

Time: O(N) per operation — Space: O(N)python

```python
class FrontMiddleBackQueue:

    def __init__(self):
        self.q = []

    def pushFront(self, val: int) -> None:
        self.q.insert(0, val)

    def pushMiddle(self, val: int) -> None:
        self.q.insert(len(self.q) // 2, val)

    def pushBack(self, val: int) -> None:
        self.q.append(val)

    def popFront(self) -> int:
        if not self.q:
            return -1
        return self.q.pop(0)

    def popMiddle(self) -> int:
        if not self.q:
            return -1
        return self.q.pop((len(self.q) - 1) // 2)

    def popBack(self) -> int:
        if not self.q:
            return -1
        return self.q.pop()
```

### 2. Optimal Approach (Using Two Deques)

Time: O(1) per operation — Space: O(N)python

```python
from collections import deque

class FrontMiddleBackQueue:

    def __init__(self):
        self.left = deque()
        self.right = deque()

    def balance(self):
        while len(self.left) > len(self.right) + 1:
            self.right.appendleft(self.left.pop())

        while len(self.left) < len(self.right):
            self.left.append(self.right.popleft())

    def pushFront(self, val: int) -> None:
        self.left.appendleft(val)
        self.balance()

    def pushMiddle(self, val: int) -> None:
        if len(self.left) > len(self.right):
            self.right.appendleft(self.left.pop())

        self.left.append(val)
        self.balance()

    def pushBack(self, val: int) -> None:
        self.right.append(val)
        self.balance()

    def popFront(self) -> int:
        if not self.left:
            return -1

        ans = self.left.popleft()
        self.balance()
        return ans

    def popMiddle(self) -> int:
        if not self.left:
            return -1

        ans = self.left.pop()
        self.balance()
        return ans

    def popBack(self) -> int:
        if not self.right and not self.left:
            return -1

        if self.right:
            ans = self.right.pop()
        else:
            ans = self.left.pop()

        self.balance()
        return ans
```
