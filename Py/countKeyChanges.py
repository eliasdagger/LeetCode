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
