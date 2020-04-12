"""
used in  Linked List Cycle detection problem
cycle detection -> endless loop determination (or can use hashset/set)

"""


# Write an algorithm to determine if a number n is "happy".

# A happy number is a number defined by the following process: 
# Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), 
# or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

# Example: 

# Input: 19
# Output: true
# Explanation: 
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1


class Solution:
    def isHappy(self, n: int) -> bool:
        import math
        # mem = set() # method 1 hashset
        n_fast = sum([int(math.pow(int(num), 2)) for num in str(n)])
        while n != 1 and n != n_fast:
            print (n)
            print (n_fast)
            n = sum([int(math.pow(int(num), 2)) for num in str(n)])
            n_fast = sum([int(math.pow(int(num3), 2)) for num3 in str(sum([int(math.pow(int(num2), 2)) for num2 in str(n_fast)]))])
        if n == 1: 
            return True
        if n == n_fast:
            return False
            # method 1 hashset
        # if n in mem: 
        #     return False 
        # mem.add(n)
        return True
