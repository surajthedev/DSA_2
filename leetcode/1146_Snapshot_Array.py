# Implement a SnapshotArray that supports the following interface:

# SnapshotArray(int length) initializes an array-like data structure with the given length. Initially, each element equals 0.
# void set(index, val) sets the element at the given index to be equal to val.
# int snap() takes a snapshot of the array and returns the snap_id: the total number of times we called snap() minus 1.
# int get(index, snap_id) returns the value at the given index, at the time we took the snapshot with the given snap_id


# Example 1:

# Input: ["SnapshotArray","set","snap","set","get"]
# [[3],[0,5],[],[0,6],[0,0]]
# Output: [null,null,0,null,5]
# Explanation:
# SnapshotArray snapshotArr = new SnapshotArray(3); // set the length to be 3
# snapshotArr.set(0,5);  // Set array[0] = 5
# snapshotArr.snap();  // Take a snapshot, return snap_id = 0
# snapshotArr.set(0,6);
# snapshotArr.get(0,0);  // Get the value of array[0] with snap_id = 0, return 5


# Constraints:

# 1 <= length <= 5 * 104
# 0 <= index < length
# 0 <= val <= 109
# 0 <= snap_id < (the total number of times we call snap())
# At most 5 * 104 calls will be made to set, snap, and get.
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
# ### Brute Force — `O(n × snaps)` per snapshot

python
```
class SnapshotArray:

    def __init__(self, length: int):
        self.arr = [0] * length
        self.snaps = []

    def set(self, index: int, val: int) -> None:
        self.arr[index] = val

    def snap(self) -> int:
        self.snaps.append(self.arr[:])
        return len(self.snaps) - 1

    def get(self, index: int, snap_id: int) -> int:
        return self.snaps[snap_id][index]
```

### Optimal — `O(1)` set, `O(log k)` get

python
```
from bisect import bisect_right

class SnapshotArray:

    def __init__(self, length: int):
        self.snap_id = 0
        self.history = [[(0, 0)] for _ in range(length)]

    def set(self, index: int, val: int) -> None:
        history = self.history[index]

        if history[-1][0] == self.snap_id:
            history[-1] = (self.snap_id, val)
        else:
            history.append((self.snap_id, val))

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        history = self.history[index]
        pos = bisect_right(history, (snap_id, float('inf'))) - 1
        return history[pos][1]
```
