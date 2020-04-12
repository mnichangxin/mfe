# Given a non-empty array of integers, 
# every element appears twice except for one. Find that single one.

# Example 1:

# Input: [2,2,1]
# Output: 1

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in range (1, len(nums)):
            nums[0] ^= nums[i]
        return nums[0]
