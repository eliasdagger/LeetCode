# LeetCode 58 - Length of Last Word (Easy)
#
# Given a string s made of words separated by spaces, return the length of the
# last word, where a word is a maximal run of non-space characters.
#
# The string may have trailing spaces, so you cannot just split on spaces and grab
# the final piece without dealing with them first.
#
# Example: 'Hello World'                ->  5
#          '   fly me   to   the moon  ' ->  4

class Solution(object):
    def lengthOfLastWord(self, s):
        # start at the right most index since we are trying to find the length of the last word. init count to 0
        r = len(s) - 1
        c = 0
        # condition is to scan the entiry of the string, thus >= 0
        while r >= 0:
            # if the character is not alphanumeric, decrement r until it finds the last word
            if not s[r].isalnum():
                r -= 1
            # found the last word, now find the len, make a while loop to iterate each char of the word and increment count then return 
            elif s[r].isalnum():
                while r >= 0 and s[r].isalnum():
                    c += 1
                    r -= 1
                return c