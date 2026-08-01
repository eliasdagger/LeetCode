class Solution(object):
    def firstPalindrome(self, words):
        # if string is same reversed, return string as that is the first normal left to right iteration.
        for idx, s in enumerate(words):
            if s[::] == s[::-1]:
                return s[::]
        # if no string exists return empty quotes
        return ""
