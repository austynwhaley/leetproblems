# Problem:
# Write a function that performs a binary search on a sorted array of integers.
# The function should return the index of a target value if found, or -1 if the 
# target value is not in the array.

# Input:
# A sorted array of integers: nums
# A target integer: target
# Output:
# The index of target in nums, or -1 if not found.

nums = [1,2,5,7,9]
target = 2

out: 1


def binary_search(nums: list[int], target: int) -> int:

    if not nums:
        return -1
    
    s, e = 0, len(nums) - 1

    while s <= e:
        m = (s + e) // 2
  
        if nums[m] == target:
            return m
        elif nums[m] < target:
            s = m + 1
        else:
            e = m - 1

    return -1

print(binary_search(nums, target))





            
