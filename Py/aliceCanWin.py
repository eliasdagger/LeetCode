# LeetCode 3232 - Find if Digit Game Can Be Won (Easy)
#
# Alice and Bob play a game with an array nums of positive integers, each of which
# is either a single-digit number (1-9) or a double-digit number (10-99).
#
# Alice chooses one of two options: take all of the single-digit numbers, or take
# all of the double-digit numbers. Bob gets everything she did not take. Alice
# wins if her total is strictly greater than Bob's.
#
# Return true if Alice can win by picking one of those two groups, false if not.
# She only loses when the two group totals are exactly equal, since otherwise she
# just picks whichever group is bigger.
#
# Example: nums = [1,2,3,4,10]  ->  true

class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        # alice can pick all single or double digit numbers, she can win if the sum of her numbers are greater than bobs. only possibility she doesnt win is if sd == dd 
        sd, dd = 0,0

        for i in nums:
            if i >= 10:
                dd += i
            elif i < 10:
                sd += i

        return not sd == dd