# LeetCode 2520 - Count the Digits That Divide a Number (Easy)
#
# Given an integer num, count how many of its own digits divide num evenly.
#
# A digit is counted every time it appears, so a repeated digit that divides num
# contributes more than once. num is guaranteed not to contain the digit 0.
#
# Example: num = 121  ->  2 (both 1s divide 121, but 2 does not)
#          num = 1248 ->  4 (every digit divides 1248)

class Solution(object):
    def countDigits(self, num):
        # create a string rep of the number to gain the ability to iterate through the int 
        div = str(num)
        c = 0

        # for each index of div, if num is divisible increment count
        for i in range(len(div)):
            if num % int(div[i]) == 0:
                c += 1
        return c
