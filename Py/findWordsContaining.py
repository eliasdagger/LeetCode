# LeetCode 2942 - Find Words Containing Character (Easy)
#
# Given an array of strings words and a character x, return an array of the
# indices of every word that contains x.
#
# The indices may be returned in any order.
#
# Example: words = ['leet','code'], x = 'e'  ->  [0,1]
#          words = ['abc','bcd','aaaa','cbc'], x = 'a'  ->  [0,2]

class Solution(object):
    def findWordsContaining(self, words, x):
        # if char in word append list index
        res = []
        for idx, s in enumerate(words):
            if x in s:
                res.append(idx)
        return res
        