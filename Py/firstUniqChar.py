# LeetCode 387 - First Unique Character in a String (Easy)
#
# Given a string s, find the first character that appears exactly once in the
# whole string and return its index. If every character repeats, return -1.
#
# Note that "first" means first by position in the string, not first one you
# happen to find while counting.
#
# Example: s = 'leetcode'     ->  0
#          s = 'loveleetcode' ->  2
#          s = 'aabb'         ->  -1

class Solution(object):
    def firstUniqChar(self, s):
        # create a hash map with key(char):value(frequency) --> {'a': 2, 'b': 1, ...}
        c = collections.Counter(s)
        # if frequency of char is one then first unique char so return index
        for idx, char in enumerate(s):
            if c[char] == 1:
                return idx
        return -1