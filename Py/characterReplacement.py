# LeetCode 424 - Longest Repeating Character Replacement (Medium)
#
# You are given a string s of uppercase English letters and an integer k. You may
# choose any k characters in the string and change each one into any other
# uppercase letter.
#
# Return the length of the longest substring you can make consist of a single
# repeated character after performing at most k replacements.
#
# Example: s = 'AABABBA', k = 1  ->  4
#          (change the middle A to a B to get the substring 'BBBB')

from typing import Counter


def characterReplacement(s: str, k: int):
    count = {}
    res = 0 
    l = 0 

    for r in range(len(s)):
        count[s[r]] = 1 + count.get(s[r], 0)

        while (r - l + 1) - max(count.values()) > k:
            count[s[l]] -= 1
            l += 1

        res = max(res, r - l + 1)
    return res


    



print(characterReplacement("AAABBAACA", 2))

g = "AAABBAACA"
# print(g[0:1])