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

# def trap(height):
#     l = 0
#     r = l + 2
#     volume = 0
#     while r < len(height):
#         print(f"vol = {volume}")
#         i = l + 1
        
#         print(f"l = {height[l]} @ {l}, i = {height[i]} @ {i}, r = {height[r]} @ {r}")

        
#         if height[i] >= height[l]:
#             print(f"shifting")
#             l = i
#             continue
#         else:
#             while r < len(height) - 1 and height[r] <= height[i]:
#                 print(f"scanning for second boundary")
#                 r += 1
#             while i < r and height[r] > height[i]:
#                 print(f"scanning rain volume")
#                 volume += min(height[l], height[r]) - height[i]
#                 i += 1

#             l = r
#             r = l + 2
#     return volume

# print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))

def trap(height):
    if not height: return 0

    l, r = 0, len(height) - 1
    leftMax, rightMax = height[l], height[r]

    volume = 0

    while l < r:
        if leftMax < rightMax:
            l += 1
            leftMax = max(leftMax, height[l])
            volume += leftMax - height[l] 
        else:
            r -= 1
            rightMax = max(rightMax, height[r])
            volume += rightMax - height[r]

    return volume


print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))