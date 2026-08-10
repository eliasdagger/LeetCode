# LeetCode 3019 - Number of Changing Keys (Easy)
#
# You are given a string s of what a user typed. Return the number of times they
# had to change the key they were pressing.
#
# Shifting between the upper and lower case of the same letter does not count as a
# key change - only moving to a different letter does. So 'ab' is one change but
# 'aA' is none.
#
# Example: s = 'aAbBcC'  ->  2 (a to b, then b to c)
#          s = 'AaAaAaaA' ->  0

class Solution(object):
    def countKeyChanges(self, s):
        # init count, all keys lower to check for char changes not capitalization changes, set curr to first char, each time it changes increment count and set curr to new char
        c = 0
        s = s.lower()
        curr = s[0]
        for i in range(len(s)):
            if s[i] != curr:
                c += 1
                curr = s[i]
        return c
