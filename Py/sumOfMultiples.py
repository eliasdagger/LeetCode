# LeetCode 2652 - Sum Multiples (Easy)
#
# Given a positive integer n, return the sum of every integer in the range [1, n]
# that is divisible by 3, by 5, or by 7.
#
# A number divisible by more than one of them is still only counted once.
#
# Example: n = 7   ->  3 + 5 + 6 + 7 = 21
#          n = 10  ->  3 + 5 + 6 + 7 + 9 + 10 = 40

class Solution(object):
    def sumOfMultiples(self, n):
        c = 0
        # mod to ensure divisible, increment c by i 
        for i in range(1, n + 1):
            if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
                c += i
                
        return c