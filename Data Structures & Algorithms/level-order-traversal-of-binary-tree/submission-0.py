# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        '''
        1. take a queue
        2. insert node
        3. traverse while the node is in queue
        4. add the node element to the curr_result array
        5. add left and right child to the queue if available
        6. if queue is empty come out of the loop
        7. add curr_result to global result 
        '''
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level_size = len(queue)
            curr_level = []

            for i in range(level_size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                val = node.val
                curr_level.append(val)

            result.append(curr_level)
            curr_level = []

        return result