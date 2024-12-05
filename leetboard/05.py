# Handle Edge Case: If the root is None, return an empty list.
# Initialize Structures:
# Create a result list res to store the final output.
# Create a queue q initialized with the root node.
# Perform BFS:
# While the queue is not empty:
# Get the number of nodes at the current level (level_size = len(q)).
# Create an empty list level to store the current level’s values.
# For each node in this level (for _ in range(level_size)):
# Dequeue a node.
# Add its value to level.
# If the node has a left child, enqueue it.
# If the node has a right child, enqueue it.
# Append level to res.
# Return the result list.
from collections import deque

class Solution:
    def btsTraverse(root):
        if root is None:
            return []
        
        res = []
        q = deque([root])

        while q:
            level_len = len(q)
            level = list()

            for _ in range(level_len):
                curr_node = q.popleft()
                level.append(curr_node.val)

                if curr_node.left:
                    q.append(curr_node.left)

                if curr_node.right:
                    q.append(curr_node.right)

            res.append(level)

        return res
    

    
