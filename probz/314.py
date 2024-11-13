# Definition for a binary tree node.
from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if curr_node is None:
            return []
        
        queue = deque([(root, 0)])
        hasher = {}

        while queue:
            curr_node, col = queue.popleft()

            if curr_node.left:
                queue.append((curr_node.left, col - 1))
            if curr_node.right:
                queue.append((curr_node.right, col + 1))
            if col in hasher:
                hasher[col].append(curr_node.val)
            else:
                hasher[col] = [curr_node.val]

        sorted_columns = sorted(hasher.keys())
        result = []
        for col in sorted_columns:
            result.append(hasher[col])

        return result