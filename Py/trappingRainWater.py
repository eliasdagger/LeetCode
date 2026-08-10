# LeetCode 42 - Trapping Rain Water (Hard)
#
# Given n non-negative integers height representing an elevation map where the
# width of each bar is 1, work out how much rainwater is trapped once it rains.
#
# Water settles on top of a bar up to the lower of two heights: the tallest bar
# anywhere to its left, and the tallest bar anywhere to its right. Anything above
# that level runs off the open side. Return the total units of water trapped.
#
# Example: [0,1,0,2,1,0,1,3,2,1,2,1]  ->  6
#
# The code below is an unfinished first attempt - the working two-pointer solution
# is in trap.py.

def trap(height: List[int]) -> int:
    l = 0
    r = 1
    res = 0
    while r < len(height):
        if l < r:
            l += 1
            r += 1
            continue
        if r
        
        for i in range(l, r):


    pass



print(trap([0,2,0,3,1,0,1,3,2,1]))