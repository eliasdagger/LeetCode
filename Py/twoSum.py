# LeetCode 1 - Two Sum (Easy)
#
# Given an array of integers nums and an integer target, return the indices of the
# two numbers that add up to target.
#
# Each input has exactly one solution, and you may not use the same element twice.
# The two indices can be returned in any order.
#
# The brute-force double loop is O(n^2); the follow-up asks for an O(n) solution,
# which means remembering the values you have already seen in a hash map.
#
# Example: nums = [2,7,11,15], target = 9  ->  [0,1]
#          nums = [3,2,4], target = 6      ->  [1,2]

class Solution(object):
    def twoSum(self, nums, target):
        # nested loop strategy allows us to skip index to ensure indices are not duplicates
        for i in range(len(nums)):
            for j in range(len(nums)):
                if j == i:
                    continue
                if nums[j] + nums[i] == target:
                    return [j,i]
        # if loop breaks without appending values, there is no solution thus we will return empty res
        return []