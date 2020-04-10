# Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

# Your algorithm should run in O(n) complexity.

# Example:

# Input: [100, 4, 200, 1, 3, 2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

class Solution:
    def longestConsecutive(self, nums) -> int:
        length = 0
        max_num = len(nums)
        num_set = set(nums)
        if len(nums) != 0:
            length = 1
            for i in range (min(nums), max(nums), 1):
                print(i)
                if (i - 1 in num_set): continue  
                accumulator = i + 1
                while (accumulator in num_set):
                    accumulator += 1
                    length = max(length, accumulator - i)
                    

        return length

s = Solution()
print (s.longestConsecutive([0, -1]))
print (s.longestConsecutive([2]))
## print (s.longestConsecutive([10,4,20,1,3,2]))
