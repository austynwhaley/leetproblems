# Function twoSum(nums, target):
#     1. Create an empty hash map to store complements
#     2. Iterate through the array
#     3. Calculate the complement (target - current number)
#     4. Check if complement exists in hash map
#     5. If found, return indices of current number and its complement
#     6. If not found, add current number and its index to hash map
#     7. If no solution found, return empty list or raise an error

from typing import List


class Solution:
    def twoSum(nums:List[int], target:int) -> List[int]:
        table = {}

        for i, num in enumerate(nums):
            curr = target - num
            if curr in table:
                return [table[curr], i]

            table[num] = i
            
        return []



# got 99.9% right just put table[num] instead of table[curr] on line 20 