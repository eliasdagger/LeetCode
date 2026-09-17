class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        # create a hash table, iterate through the list keeping track of occurences of each int val, if count > floor div length of list then return that val as the majority element
        cnt = {}
        for num in nums:
            cnt[num] = cnt.get(num, 0) + 1
            if cnt[num] > len(nums) // 2:
                return num

        return []