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

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # create a two pointer technique from either side, at each iteration check the volume, change the boundaries depending on which is the lower wall. this will ensure we look for the largest volume
        l, r = 0, len(height) - 1

        max_volume = 0
        while l < r:
            curr_volume = (r - l) * min(height[l], height[r])
            max_volume = max(max_volume, curr_volume)

            if height[l] < height[r]:
                l += 1
            elif height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return max_volume 
            
        