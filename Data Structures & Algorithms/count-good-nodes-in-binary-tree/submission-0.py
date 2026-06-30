# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def helper(root, count, max_):
            if not root:
                return count

            if root.val >= max_:
                count += 1
                max_ = root.val
            
            count = helper(root.left, count, max_)
            count = helper(root.right, count, max_)

            return count

        return helper(root, 0, float('-inf'))
