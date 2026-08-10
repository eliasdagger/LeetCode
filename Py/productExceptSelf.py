# LeetCode 238 - Product of Array Except Self (Medium)
#
# Given an integer array nums, return an array answer where answer[i] is the
# product of every element of nums except nums[i].
#
# Every one of those products is guaranteed to fit in a 32-bit integer, and the
# problem asks for an O(n) solution that does not use the division operator - the
# intended answer builds prefix and suffix products instead.
#
# Zeros are the interesting case if you do divide: a single zero makes every other
# entry 0 and only the zero's own slot gets the product of the rest, while two or
# more zeros make the entire answer zeros.
#
# Example: [1,2,3,4]  ->  [24,12,8,6]

# Initial Attempt which breached time limit
class Solution(object):
    def productExceptSelf(self, nums):
        res = []
        for i in range(len(nums)):
            prod = 1
            for j in range(len(nums)):
                if j == i:
                    continue
                prod = prod * nums[j]
            
            res.append(prod)
        return res
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
# Second attempt
# Example: [1,2,4,6]
class Solution(object):
    def productExceptSelf(self, nums):
        prod, zeros = 1, 0

        # First multiply every num in nums. 
        # ex. prod = 48
        for num in nums:
            # if non zero
            if num:
                prod *= num
            else:
                zeros +=  1
        if zeros > 1: return [0] * len(nums)

        res = [0] * len(nums)
        for i, c in enumerate(nums):
            if zeros: res[i] = 0 if c else prod
            else: res[i] = prod // c
        return res
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        