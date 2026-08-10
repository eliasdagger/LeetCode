# Digit frequency score
#
# Given an integer n, look at its decimal digits. For each distinct digit,
# multiply the digit by the number of times it appears in n, then return the sum
# of those products.
#
# Example: n = 1223  ->  (1 x 1) + (2 x 2) + (3 x 1) = 1 + 4 + 3 = 8
#
# The LeetCode number for this one was not recorded in the file.

class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        # convert n to string to iterate each digit, use collections counter to count each char conv into a key value pair {'char': frequency}. simple for loop .items() to handle key value pairs. then perform the arithmetic the problem requires
        s = str(n)
        res = 0
        c = collections.Counter(s)
        
        for key, value in c.items():
            res += int(key) * value

        return res

        