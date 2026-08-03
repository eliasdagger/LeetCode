
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

