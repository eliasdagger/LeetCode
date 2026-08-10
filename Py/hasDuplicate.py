# Duplicate Integer (NeetCode) - the same problem as LeetCode 217, Contains Duplicate
#
# Given an integer array nums, return true if any value appears more than once,
# and false if every element is distinct.
#
# Example: [1,2,3,3]  ->  true
#          [1,2,3,4]  ->  false

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        lst = []
        for i in nums:
            if i in lst:
                return True
            lst.append(i)
        return False
            
