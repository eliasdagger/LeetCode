# LeetCode 125 - Valid Palindrome (Easy)
#
# A phrase counts as a palindrome if, after lowercasing every letter and throwing
# away everything that is not a letter or a digit, it reads the same forwards and
# backwards.
#
# Given a string s, return true if it is a palindrome and false otherwise. An
# empty string counts as a palindrome.
#
# Example: 'A man, a plan, a canal: Panama'  ->  true
#          'race a car'                      ->  false

class Solution(object):
    def isPalindrome(self, s):
        # utilise a two pointer method which can check for symmetry by comparing either end
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            r -= 1
            l += 1
        return True