# LeetCode 258 - Add Digits (Easy)
#
# Given a non-negative integer num, repeatedly add all of its digits together
# until the result is a single digit, then return that digit.
#
# Example: num = 38  ->  3 + 8 = 11  ->  1 + 1 = 2, so the answer is 2
#
# The follow-up asks for an O(1) solution with no loop and no recursion. That is
# the digital root: for any num > 0 the answer is 1 + (num - 1) % 9.

class Solution(object):
    def addDigits(self, num):
        # base case
        if num == 0:
            return 0

        # 
        return 1 + (num - 1) % 9