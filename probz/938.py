# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # we are given a binary tree arr
        # then we are given 2 ints a high and a low
        # we must traverse the tree and find all the numbers within that 
        # given range and caculate the sum
        