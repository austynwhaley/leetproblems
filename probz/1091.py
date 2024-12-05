from collections import deque
from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        n = len(grid)
        occupied = set([0, 0, 1])
        queue = deque([(0, 0, 1)])  # row column and number of nodes traversed
        # directional movement in matrix
        directions = [
            (-1, 0),  # up
            (1, 0),  # down
            (0, -1),  # left
            (0, 1),  # right
            (-1, -1),  # top-left
            (-1, 1),  # top-right
            (1, -1),  # bottom-left
            (1, 1)  # bottom-right
        ]

        # write in edge cases to prevent unnecessary runtime
        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return -1

        while queue:
            row, column, trav = queue.popleft()

            if row == n - 1 and column == n - 1:
                return trav

            for drow, dcolumn in directions:
                nrow, ncolumn = row + drow, column + dcolumn

                if (
                    0 <= nrow < n and
                    0 <= ncolumn < n and
                    grid[nrow][ncolumn] == 0 and
                    (nrow, ncolumn) not in occupied
                ):
                    occupied.add((nrow, ncolumn))
                    queue.append((nrow, ncolumn, trav + 1))

        return -1
