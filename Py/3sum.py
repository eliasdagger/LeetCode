# LeetCode 15 - 3Sum (Medium)
#
# Given an integer array nums, return every unique triplet [nums[i], nums[j],
# nums[k]] where i, j and k are three different indices and the three values add
# up to 0.
#
# The answer must not contain duplicate triplets - [-1,0,1] and [0,1,-1] count as
# the same triplet - though the triplets themselves may be returned in any order.
# Handling those duplicates is the real difficulty of the problem.
#
# Example: nums = [-1,0,1,2,-1,-4]  ->  [[-1,-1,2],[-1,0,1]]

from typing import List

def threeSum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    res = []
    
    for i, a in enumerate(nums):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        target = -a
        front, rear = i + 1, len(nums) - 1

        while front < rear:
            current_sum = nums[front] + nums[rear]
            
            if current_sum == target:
                res.append([a, nums[front], nums[rear]])
                
                front += 1
                rear -= 1
                
                while front < rear and nums[front] == nums[front - 1]:
                    front += 1
                    
                while front < rear and nums[rear] == nums[rear + 1]:
                    rear -= 1

            elif current_sum > target:
                rear -= 1
            else:
                front += 1
                
    return res

print(threeSum([-3, 3, 4, -3, 1, 2]))
