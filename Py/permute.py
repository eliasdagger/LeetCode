# LeetCode 46 - Permutations (Medium)
#
# Given an array nums of distinct integers, return every possible ordering of
# its elements. The permutations can be returned in any order.
#
# All values are distinct, so there are exactly n! permutations and nothing to
# deduplicate. nums has between 1 and 6 elements. This is the classic
# introduction to backtracking.
#
# Example: [1,2,3]  ->  [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
#          [0,1]    ->  [[0,1],[1,0]]

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1: return [nums[:]]

        res = []

        for _ in range(len(nums)):
            curr = nums.pop(0)
            perms = self.permute(nums)

            for p in perms:
                p.append(curr)

            res.extend(perms)
            nums.append(curr)
        return res
            

        