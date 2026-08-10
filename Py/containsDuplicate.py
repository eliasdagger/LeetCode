# LeetCode 217 - Contains Duplicate (Easy)
#
# Given an integer array nums, return true if any value appears at least twice,
# and false if every element is distinct.
#
# Example: [1,2,3,1]  ->  true
#          [1,2,3,4]  ->  false

class Solution(object):
    def containsDuplicate(self, nums):
        # utilise a set which contains only unique values, if the len of this set is different then the len of nums, nums had inunique values, thus false, else tr
        return len(set(nums)) != len(nums)