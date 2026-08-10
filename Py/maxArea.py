# LeetCode 11 - Container With Most Water (Medium)
#
# You are given an array height of n non-negative integers, where each value is
# the height of a vertical line drawn at that index.
#
# Pick two of those lines so that, together with the x-axis, they form a container
# that holds the most water, and return that maximum area.
#
# The area is the horizontal distance between the two lines multiplied by the
# height of the shorter one - water spills over the lower side, and the container
# cannot be tilted.
#
# Example: [1,8,6,2,5,4,8,3,7]  ->  49

def maxArea(heights: List[int]) -> int:
    area = 0
    f = 0
    r = len(heights) - 1
    while f < r: 
        temp = (r - f) * min(heights[f], heights[r])
        print(f"Front: {heights[f]}cm @ {f} - Rear: {heights[r]}cm @ {r} - Area: {temp}")
        if temp > area: 
            area = temp
        if heights[f] < heights[r]:
            f += 1
        else : 
            r -= 1
    return area


print(maxArea([1,7,2,5,12,3,500,500,7,8,4,7,3,6]))