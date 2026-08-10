# LeetCode 3024 - Type of Triangle (Easy)
#
# You are given a list nums of three positive numbers, the lengths of the sides of
# a possible triangle. Return a string describing it:
#
#   'none'         the three lengths cannot form a triangle at all
#   'equilateral'  all three sides are equal
#   'isosceles'    exactly two sides are equal
#   'scalene'      all three sides are different
#
# Three lengths can form a triangle only if the sum of any two of them is strictly
# greater than the third - the triangle inequality. Check that first, because
# [1,1,3] has two equal sides but is not a triangle at all.
#
# Example: [3,3,3]  ->  'equilateral'
#          [1,2,3]  ->  'none'

class Solution(object):
    def triangleType(self, nums):
        # sort nums to examine if it is a valid triangle via the inequality thereom.
        nums.sort()
        if not nums[0] + nums[1] > nums[2]:
            return "none"
        # create a set of nums, duplicates will be filtered thus we know which type of triangle it is depending on the number of unique side lengths
        uniqCh = len(set(nums))
        
        if uniqCh == 3:
            return "scalene"
        elif uniqCh == 2:
            return "isosceles"
        else:
            return "equilateral"
