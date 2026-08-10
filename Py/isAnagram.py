# LeetCode 242 - Valid Anagram (Easy)
#
# Given two strings s and t, return true if t is an anagram of s - that is, if t
# uses exactly the same characters as s with the same counts, just arranged
# differently.
#
# Strings of different lengths can never be anagrams of each other.
#
# Example: s = 'anagram', t = 'nagaram'  ->  true
#          s = 'rat', t = 'car'          ->  false

class Solution(object):
    def isAnagram(self, s, t):
        # simply, if one string is an anagram of another, they must contained the same chars, if the sorted versions are identical, then they contain all the same chars.
        return sorted(s) == sorted(t)