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



"""
Two Sum - C Implementation

int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    # when creating our result array, we need to store the memory in the heap opposed to the stack
    # then edit returnSize to be the size of the array we are returning. Perform the same algorithm to find the 2sum
    int* res = malloc(2 * sizeof(int));
    *returnSize = 2;

    for (int i = 0; i < numsSize; i++){
        for (int j = i + 1; j < numsSize; j++){
            if (nums[j] + nums[i] == target){
                res[0] = j;
                res[1] = i;
                return res;
            }
        }
    }

    # 
    *returnSize = 0;
    return res;
}


"""