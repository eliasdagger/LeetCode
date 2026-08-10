# Weekly contest problem - unfinished attempt
#
# The original statement was not saved in this file. Based on the signature
# maxSubarraySum(nums, k) and the sample call, this looks like "Maximum Subarray
# Sum With Length Divisible by K":
#
#   Given an integer array nums and an integer k, return the largest possible sum
#   of a non-empty subarray (a contiguous block of nums) whose length is a
#   multiple of k.
#
# Example: nums = [1,-2,3,4,-5], k = 2  ->  7, from the subarray [3,4]
#
# Worth double-checking against the contest page - the code below is an incomplete
# sliding-window attempt and does not actually solve it.

# Did not complete
def maxSubarraySum(nums, k):
    total = 0
    l, r = 0, 0
    if max(nums) < 0:
            total += -(-max(nums) // k)
    else:
        while r < len(nums) - 1:   
            print(f"l = {l} r = {r}")  
            if nums[r + 1] >= 0:
                total = max(total, sum(nums[l:r]) * k)

                r += 1
                print(f"total = {total} ss = {nums[l:r]}")       
            else:
                l += 1
                r += 1
    return total

print(maxSubarraySum([1,-2,3,4,-5], 2))

