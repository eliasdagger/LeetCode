# LeetCode 977 - Squares of a Sorted Array (Easy)
#
# Given an integer array nums sorted in non-decreasing order - which may include
# negative numbers - return an array of the squares of each number, also sorted in
# non-decreasing order.
#
# Squaring and then sorting is the easy way. The follow-up asks for an O(n)
# solution, which is possible because the largest squares always live at the two
# ends of the array.
#
# Example: [-4,-1,0,3,10]  ->  [0,1,9,16,100]
#          [-7,-3,2,3,11]  ->  [4,9,9,49,121]

class Solution(object):
    def sortedSquares(self, nums):
        # square entries then sort
        return sorted([x**2 for x in nums])
        