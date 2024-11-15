# Definition for a binary tree node.
from collections import deque
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        queue = deque([root])
        r_side = []

        while queue:
            level_length = len(queue)
            for i in range(level_length):
                node = queue.popleft()
                
                # If it's the last node in the level, add its value to r_side
                if i == level_length - 1:
                    r_side.append(node.val)
                
                # Add child nodes to the queue for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return r_side

    

solution = Solution()
root = [1,2,3,None,5,None,4]

print(f"{solution.rightSideView(root)}")

# Output: [1,3,4]
