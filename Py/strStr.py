# LeetCode 28 - Find the Index of the First Occurrence in a String (Easy)
#
# Given two strings haystack and needle, return the index of the first occurrence
# of needle inside haystack, or -1 if needle is not part of haystack.
#
# Example: haystack = 'sadbutsad', needle = 'sad'    ->  0
#          haystack = 'leetcode',  needle = 'leeto'  ->  -1

class Solution(object):
    def strStr(self, haystack, needle):
        # starting pointer
        l = 0
        # utilise a sliding window approach, window should include l as a starting point, then +length of needle, final value exclusive
        # <= since the window is l + len exclusive final elementthus, no index out of bounds error
        while l + len(needle) <= len(haystack):
            # if this window is the needle, l will return as the starting index of the needle, else we will shift the window.
            if haystack[l:l+len(needle)] == needle:
                return l
            else:
                l += 1
                    
        return -1
        