# Rearrange a string so all copies of one character come first
#
# Given a string s and two characters x and y, return a rearrangement of s in
# which every occurrence of y is moved to the front, ahead of any x, with all of
# the other characters left in their original relative order.
#
# Example: s = 'axbyc' with y = 'b'  ->  'baxyc'
#
# The LeetCode number for this one was not recorded in the file, so the exact
# original wording is worth double-checking.

class Solution:
    def rearrangeString(self, s: str, x: str, y: str) -> str:
        # in order to ensure that all instances of y occur before x in our result, for count of y, add to string first, then add the rest of the chars in string skipping the y's
        res = ""
        c = collections.Counter(s)
        
        for ss in range(c[y]):
            res += y
            
        for ch in s:
            if ch == y:
                continue
            else:
                res += ch

        return res