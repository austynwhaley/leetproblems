# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        if root.val > high:
            return self.rangeSumBST(root.left, low, high)
        if root.val < low:
            return self.rangeSumBST(root.right, low, high)
        return (
            root.val + 
            self.rangeSumBST(root.right, low, high) + 
            self.rangeSumBST(root.left, low, high)
        )
    


solution = Solution()
tree = [10,5,15,3,7,None,18] # type: ignore
low_num = 7
high_num = 15

print(solution.rangeSumBST(tree,low_num, high_num ))