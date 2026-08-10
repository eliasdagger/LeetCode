# LeetCode 2535 - Difference Between Element Sum and Digit Sum of an Array (Easy)
#
# Given an array nums of positive integers, compute two totals:
#
#   the element sum - add up the numbers themselves
#   the digit sum   - add up every individual digit of every number
#
# Return the absolute difference between the two.
#
# Example: nums = [1,15,6,3]
#          element sum = 1 + 15 + 6 + 3 = 25
#          digit sum   = 1 + 1 + 5 + 6 + 3 = 16
#          answer      = 9

class Solution(object):
    def differenceOfSum(self, nums):
        elem = sum(nums)
        dig = 0 
        # nested for loop to access each index of integer within each integer of list nums 
        for idx, integer in enumerate(nums):
            # convert to string in order so we can iterate by index
            num = str(integer)
            for i in range(len(num)):
                dig += int(num[i])
                
        return abs(elem - dig)
        