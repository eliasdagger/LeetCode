# LeetCode 567 - Permutation in String (Medium)
#
# Given two strings s1 and s2, return true if s2 contains a permutation of s1 as a
# substring - that is, if some contiguous window of s2 is made of exactly the same
# letters as s1, with the same counts, in any order.
#
# Example: s1 = 'ab', s2 = 'eidbaooo'  ->  true (the window 'ba')
#          s1 = 'ab', s2 = 'eidboaoo'  ->  false


def checkInclusion(s1: str, s2: str) -> bool:
    # if the sorted version of s1 is in our sorted window, return true, continue until window is the entire length of s2, then return false if no permutation is found. 
    l, r = 0, len(s1)
    while r <= len(s2):
        if "".join(sorted(s1)) in "".join(sorted(s2[l:r])):
            return True
        else:
            r += 1
            l += 1
    return False

