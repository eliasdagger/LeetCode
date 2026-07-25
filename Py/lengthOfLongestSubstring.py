class Solution(object):
    def lengthOfLongestSubstring(self, s):
        l, r = 0,0
        res = 0
        while r < len(s):
            if len(set(s[l:r+1])) > len(set(s[l:r])):
                r += 1
                
            else:
                l += 1
            res = max(res, r - l)

        return res

# O(n) solution which uses a hash set to dictate l and r's position like an accordian, r will continue to extend at an increment of 1, updating count (c) if a new longest unique substring is found, if we find a duplicate, l will clear the hash set one by one removing the element of its index, this will continue until 
# duplicate is out of the hashset, then r will continue its path. This is done because we count the lenght of a substring, then when we encounter a duplicate we know that the substring from l - r is counted we can reframe until we remove the duplicate
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        l, c = 0, 0

        for r in range(len(s)):
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1

            char_set.add(s[r])
            c = max(c, r - l + 1)
        
        return c