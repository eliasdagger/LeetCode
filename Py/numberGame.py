# LeetCode 2974 - Minimum Number Game (Easy)
#
# Alice and Bob play with an array nums of even length. While the array is not
# empty they repeat these steps:
#
#   Alice removes the smallest remaining number, then Bob removes the smallest of
#   what is left. Bob then appends his number to the result array, and Alice
#   appends hers after it.
#
# Return the resulting array. The net effect is that the numbers come out in
# sorted order but with each adjacent pair swapped.
#
# Example: nums = [5,4,2,3]  ->  [3,2,5,4]
#          nums = [2,5]      ->  [5,2]

class Solution(object):
    def numberGame(self, nums):
        arr = []
        # sort nums in reverse in order to access lowest val via pop() method
        nums.sort(reverse=True)
        
        # continue the rules of the game
        while len(nums) != 0:
            alice = nums.pop()
            bob = nums.pop()
            
            arr.appenSd(bob)
            arr.append(alice)
        return arr