# LeetCode 1822 - Sign of the Product of an Array (Easy)
#
# Given an integer array nums, return the sign of the product of all of its
# values: 1 if the product is positive, -1 if it is negative, and 0 if the product
# is zero.
#
# You are not meant to actually multiply everything out - the product can overflow.
# Only two things matter: whether any element is zero, and whether the count of
# negative elements is odd or even.
#
# Example: nums = [-1,-2,-3,-4,3,2,1]  ->  1
#          nums = [1,5,0,2,-3]         ->  0

class Solution(object):
    def arraySign(self, nums):
        # the sign of a prod is:
        # 1) 0, if there is a single 0 anywhere in the list
        # 2) negative, if there are an odd number of negative numbers in the list, and condition 1 is not met
        # 3) positive, if there are an even number of negative numbers in the list, and condition 1 is not met
        if 0 in nums:
            return 0
        elif sum(x < 0 for x in nums) % 2 != 0:
            return -1
        else:
            return 1
