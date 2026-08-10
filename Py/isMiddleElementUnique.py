# LeetCode 3978 - Is the middle element unique
#
# Given an array nums, take the element at the middle index (len(nums) // 2) and
# return true if that value appears exactly once in the whole array, or false if
# it turns up anywhere else as well.
#
# Example: nums = [1,2,3,2,5]  ->  the middle element is 3, which appears once, so true
#          nums = [1,2,3,3,5]  ->  the middle element is 3, which appears twice, so false

class Solution(object):
    def isMiddleElementUnique(self, nums):
        # find the middle element
        mid = len(nums) // 2
        val = nums[mid]
        
        # return count of mid num == 1
        return nums.count(val) == 1
            
            