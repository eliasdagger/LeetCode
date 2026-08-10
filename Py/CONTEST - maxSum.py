# Weekly contest problem - problem statement not recorded
#
# The original statement was not saved in this file. Reading the code, the task
# appears to be: given an array nums, a count k, and a starting multiplier mul,
# pick k values to maximize the total, where each pick may be taken either as-is
# or multiplied by the current multiplier, and the multiplier drops by 1 after
# each pick.
#
# Sample call in the file: maxSum([6,1,2,9], 3, 2)
#
# Treat this one as a scratch attempt - the exact rules should be confirmed
# against the original contest problem.


def maxSum(nums, k, mul):
    s = 0
    nums.sort()

    for i in range(-1, -(k+1), -1): 
        s += max(nums[i], nums[i] * mul)
        mul -= 1
    return s
print(maxSum([6,1,2,9], 3, 2))