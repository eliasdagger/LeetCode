# LeetCode 167 - Two Sum II - Input Array Is Sorted (Medium)
#
# Given a 1-indexed array of integers numbers sorted in non-decreasing order, find
# the two numbers that add up to a specific target.
#
# Return their positions as [index1, index2] with index1 < index2, using 1-based
# indexing. There is exactly one solution, and you may not use the same element
# twice.
#
# The array being sorted is the whole point: you are required to solve it with
# only constant extra space, so a hash map is off the table and two pointers
# closing in from the ends is the intended approach.
#
# Example: numbers = [2,7,11,15], target = 9  ->  [1,2]

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Utilise a two pointer technique, since the list is sorted in ascending order, we can close move our pointers towards the two sum to target as we know if numbers @ l, r > target then we move r to the left since there is no possible sum of numbers that can equal target @ r, and vice versa
        l, r = 0, len(numbers) - 1

        while l < r:
            if numbers[l] + numbers[r] > target:
                r -= 1
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                return [l+1, r+1]

        return []
        