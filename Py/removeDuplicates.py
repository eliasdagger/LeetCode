# LeetCode 26 - Remove Duplicates from Sorted Array (Easy)
#
# Given an integer array nums sorted in non-decreasing order, remove the
# duplicates in place so that each unique value appears only once, keeping the
# original relative order.
#
# Return k, the number of unique elements. The first k slots of nums have to hold
# those unique values; whatever sits beyond index k does not matter.
#
# The work must be done in place with O(1) extra memory - you cannot build a new
# array and return it.
#
# Example: nums = [0,0,1,1,1,2,2,3,3,4]  ->  k = 5, nums starts with [0,1,2,3,4]


def removeDuplicates(nums):
    i = 0
    for j in range(1, len(nums)):
        print(f"i = {i}, j = {j}")
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    return i + 1


print(removeDuplicates([1,1,2,2,3,4,5,6,6,6]))