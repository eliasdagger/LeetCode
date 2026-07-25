class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        # sum (1 will be added, for x in nums such that IF x >= target) the sum will sum all true employees that are above the target
        res = sum(1 for x in hours if x >= target)
        return res
        