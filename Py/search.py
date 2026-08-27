# LeetCode 704 - Binary Search (Easy)
#
# Given an array nums of distinct integers sorted in ascending order, and an
# integer target, return the index of target inside nums, or -1 if it is not
# there.
#
# The solution has to run in O(log n) time, which rules out a linear scan.
#
# Example: nums = [-1,0,3,5,9,12], target = 9  ->  4
#          nums = [-1,0,3,5,9,12], target = 2  ->  -1


def search(nums: List[int], target: int) -> int:
    # Set pointers to either end of our sorted array, if l <= r create our midpoint to be the window from l->r // 2 which will be half the length of our current range 
    # then + l, to make the mid point of the list be l + half the len(window). we want to move bounds to close our window and narrow down to a solution, 
    # so, if mid val is < target meaning target is on the right of mid, change the bounds where l = mid, then add 1 since we know mid != target. Similarily for r pointer
    # if mid index == target return mid (index).  
    l, r = 0, len(nums) - 1
    while l <= r:
        m = l + ((r - l) // 2)
        print(f"m = {m}")

        if nums[m] < target:
            l = m + 1
        elif nums[m] > target: 
            r = m - 1
        else:
            return m
    return -1

print(search([-1,0,2,4,6,8], 3))