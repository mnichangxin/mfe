# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Example:

# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_idx = 0
        nonzero_idx = 0
        while zero_idx < len(nums) and nonzero_idx < len(nums) :
            if nums[nonzero_idx] == 0 and nums[zero_idx] != 0:
                nums[zero_idx], nums[nonzero_idx] =  nums[nonzero_idx], nums[zero_idx] 
            print (nonzero_idx)
            if (nums[nonzero_idx] != 0):
                nonzero_idx += 1

            zero_idx += 1
            
        return nums
