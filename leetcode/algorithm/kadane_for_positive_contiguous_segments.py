
# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# Example:

# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1: 
            return nums[0]
        max_num = nums[0] 
        min_num = nums[0]
        value = 0
        result = nums[0]
        for i in  nums:
            value += i
            if value > max_num:
                max_num = value
                result = max(result, max_num - min_num)
            if value < min_num:
                min_num = value
            
            print (min_num)
            print (max_num)
            
        return result
