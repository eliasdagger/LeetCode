# LeetCode 3976 - Maximum Subarray Sum After Multiplier (Medium)
#
# The original statement was not saved in this file. From the title and the
# signature maxSubarraySum(nums, k), the task is to find the largest subarray
# sum in nums when a multiplier k can be applied as part of the choice - the
# exact rule for how k is applied should be confirmed on the problem page.
#
# Sample call in the file: maxSubarraySum([1,-2,3,4,-5], 2)
#
# The code below is an unfinished attempt (it got Wrong Answer).

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

