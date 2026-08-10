# LeetCode 2798 - Number of Employees Who Met the Target (Easy)
#
# There are n employees, and hours[i] is the number of hours employee i worked.
#
# Given the array hours and an integer target, return how many employees worked at
# least target hours - meeting the target exactly still counts.
#
# Example: hours = [0,1,2,3,4], target = 2  ->  3
#          hours = [5,1,4,2,2], target = 6  ->  0

class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        # sum (1 will be added, for x in nums such that IF x >= target) the sum will sum all true employees that are above the target
        res = sum(1 for x in hours if x >= target)
        return res
        