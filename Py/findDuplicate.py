# LeetCode 287 - Find the Duplicate Number (Medium)
#
# You are given an array nums of n + 1 integers, where every value is in the range
# [1, n]. By the pigeonhole principle at least one value must repeat, and the
# problem guarantees there is exactly one such value - though it may appear more
# than twice.
#
# Return that repeated number.
#
# The full problem asks you to do it without modifying the array and using only
# constant extra space, which is what makes it a medium rather than a one-liner.
#
# Example: nums = [1,3,4,2,2]  ->  2
#          nums = [3,1,3,4,2]  ->  3

class Solution(object):
    def findDuplicate(self, nums):
        
        hash = {} 
        h_length = 0
        for i in range(len(nums)):
            hash[nums[i]] = nums[i]
            if len(hash) <= h_length:
                return nums[i]
            h_length += 1