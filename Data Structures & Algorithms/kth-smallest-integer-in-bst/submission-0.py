# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def helper(root, l):
            if not root:
                return l
            left = helper(root.left, l)
            l.append(root.val)
            right = helper(root.right, l)

            return l


        l = helper(root, [])
        return l[k-1]