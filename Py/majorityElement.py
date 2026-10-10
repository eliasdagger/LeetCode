# LeetCode 169 - Majority Element (Easy)
#
# Given an array nums of size n, return the majority element - the value that
# appears more than n / 2 times. The input is guaranteed to have one.
#
# The follow-up asks for O(n) time and O(1) extra space, which rules out
# counting every value in a hash map (that is what Boyer-Moore voting is for).
#
# Example: [3,2,3]          ->  3
#          [2,2,1,1,1,2,2]  ->  2

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        # create a hash table, iterate through the list keeping track of occurences of each int val, if count > floor div length of list then return that val as the majority element
        cnt = {}
        for num in nums:
            cnt[num] = cnt.get(num, 0) + 1
            if cnt[num] > len(nums) // 2:
                return num

        return []