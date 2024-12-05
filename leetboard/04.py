# Function maxSubArray(nums):
#     1. Initialize max_current and max_global with the first element
#     2. Iterate through the array starting from the second element
#     3. For each element, decide:
#        - Take the current element
#        - Or take the current element + previous max_current
#     4. Update max_global if max_current is larger
#     5. Return max_global

from typing import List

class Solution:
    def maxSubArray(nums: List[int]) -> int:
        max_curr = max_global = nums[0]

        for num in nums[1::]:
            max_curr = max(num, max_curr + num)
            max_global = max(max_curr, max_global)


# saw this on sol page and liked it more than this answer

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sumi = 0
        maxi = float('-inf')
        for num in nums:
            sumi += num
            if sumi > maxi:
                maxi = sumi
            if sumi < 0:
                sumi = 0
        return maxi