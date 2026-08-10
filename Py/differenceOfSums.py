# LeetCode 2894 - Divisible and Non-Divisible Sums Difference (Easy)
#
# You are given two positive integers n and m. Look at every integer from 1 to n
# and split them into two groups:
#
#   num1 - the integers in that range NOT divisible by m
#   num2 - the integers in that range that ARE divisible by m
#
# Return the sum of num1 minus the sum of num2.
#
# Example: n = 10, m = 3
#          num1 = 1+2+4+5+7+8+10 = 37, num2 = 3+6+9 = 18, answer = 19

class Solution(object):
    def differenceOfSums(self, n, m):
        # straight forward no explanation needed
        num1, num2 = 0, 0
        
        for i in range(1,n+1):
            if i % m == 0:
                num2 += i
            else:
                num1 += i
        
        
        return num1 - num2