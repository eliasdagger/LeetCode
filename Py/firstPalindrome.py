# LeetCode 2108 - Find First Palindromic String in the Array (Easy)
#
# Given an array of strings words, return the first string in the array that is a
# palindrome - one that reads the same forwards and backwards.
#
# If none of the words is a palindrome, return an empty string.
#
# Example: ['abc','car','ada','racecar','cool']  ->  'ada'
#          ['def','ghi']                         ->  ''

class Solution(object):
    def firstPalindrome(self, words):
        # if string is same reversed, return string as that is the first normal left to right iteration.
        for idx, s in enumerate(words):
            if s[::] == s[::-1]:
                return s[::]
        # if no string exists return empty quotes
        return ""
