# LeetCode 35 - Search Insert Position (Easy)
#
# Given a sorted array of distinct integers nums and a target value, return the
# index of the target. If the target is not in the array, return the index where
# it would need to be inserted to keep the array sorted.
#
# The solution has to run in O(log n) time, so this is binary search with a bit of
# care about where the pointers end up when the target is missing.
#
# Example: nums = [1,3,5,6], target = 5  ->  2
#          nums = [1,3,5,6], target = 2  ->  1
#          nums = [1,3,5,6], target = 7  ->  4


def searchInsert(nums, target):
    # Set up two pointers for the binary search
    l, r = 0, len(nums) - 1

    while l <= r:
        # Find middle index, l is set to the left boundary then add half the distance to the second boundary r, to find the middle index in a dynamic manner to complement the while loop
        mid = l + ((r - l) // 2)
        print(mid)
        if target > nums[mid]:
            # change l to mid + 1 since we know that mid is not == target, else this would create an infinite loop
            l = mid + 1
        elif target < nums[mid]:
            r = mid - 1
        else:
            return mid
    # Binary searches index will finish after the index if right boundary is changed and vice versa  
    return mid + 1 if target > nums[mid] else mid
    
print(searchInsert([1, 3, 5, 6], 2))