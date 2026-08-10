# LeetCode 1550 - Three Consecutive Odds (Easy)
#
# Given an integer array arr, return true if there are three consecutive odd
# numbers anywhere in the array, and false otherwise.
#
# "Consecutive" means adjacent by position, not consecutive in value.
#
# Example: [1,2,34,3,4,5,7,23,12]  ->  true (5, 7, 23 sit next to each other)
#          [2,6,4,1]               ->  false

class Solution(object):
    def threeConsecutiveOdds(self, arr):
        # use a sliding window technique to scan if there are three consecutive odd numbers
        for i in range(len(arr) - 2):
            if arr[i] % 2 != 0 and arr[i+1] % 2 != 0 and arr[i+2] % 2 != 0:
                return True

        return False