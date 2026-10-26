# Given two binary search trees root1 and root2, return a list containing all the integers from both trees sorted in ascending order.



# Example 1:


# Input: root1 = [2,1,4], root2 = [1,0,3]
# Output: [0,1,1,2,3,4]
# Example 2:


# Input: root1 = [1,null,8], root2 = [8,1]
# Output: [1,1,8,8]


# Constraints:

# The number of nodes in each tree is in the range [0, 5000].
# -105 <= Node.val <= 105
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
# ### 1. Brute Force (Inorder Traversal + Sorting)

python

```
class Solution:
    def getAllElements(self, root1, root2):
        def inorder(root, arr):
            if not root:
                return
            inorder(root.left, arr)
            arr.append(root.val)
            inorder(root.right, arr)

        arr = []
        inorder(root1, arr)
        inorder(root2, arr)

        arr.sort()
        return arr
```

### 2. Optimal (Inorder Traversal + Two Pointers)

python

```
class Solution:
    def getAllElements(self, root1, root2):
        def inorder(root):
            stack = []
            arr = []

            while root or stack:
                while root:
                    stack.append(root)
                    root = root.left

                root = stack.pop()
                arr.append(root.val)
                root = root.right

            return arr

        arr1 = inorder(root1)
        arr2 = inorder(root2)

        i = j = 0
        result = []

        while i < len(arr1) and j < len(arr2):
            if arr1[i] <= arr2[j]:
                result.append(arr1[i])
                i += 1
            else:
                result.append(arr2[j])
                j += 1

        result.extend(arr1[i:])
        result.extend(arr2[j:])

        return result
```
