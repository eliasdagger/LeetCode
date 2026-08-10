# LeetCode 1281 - Subtract the Product and Sum of Digits of an Integer (Easy)
#
# Given an integer n, compute the product of its digits and the sum of its digits,
# then return the product minus the sum.
#
# Example: n = 234  ->  product 2*3*4 = 24, sum 2+3+4 = 9, answer 15
#          n = 4421 ->  product 32, sum 11, answer 21

class Solution(object):
    def subtractProductAndSum(self, n):
        # base case
        if n == 0:
            return 0
        # 0 for sum, start prod at 1 as base
        s = 0
        p = 1
        n = str(n)
        for i in n:
            p = p * int(i)
            s += int(i)
        
        
        return p - s