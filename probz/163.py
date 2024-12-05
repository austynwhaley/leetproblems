from typing import List


class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:

        num_check = lower
        sol = []

        for num in nums:
            if num > num_check:
                sol.append([num_check, num - 1])

            num_check = num + 1

        if num_check <= upper:
            sol.append([num_check, upper])

        return sol
