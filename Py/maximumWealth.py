# LeetCode 1672 - Richest Customer Wealth (Easy)
#
# You are given an m x n grid accounts, where accounts[i][j] is how much money the
# i-th customer has in the j-th bank. A customer's wealth is the total across all
# of their accounts.
#
# Return the wealth of the richest customer - the single largest row total.
#
# Example: [[1,2,3],[3,2,1]]        ->  6
#          [[1,5],[7,3],[3,5]]      ->  10

class Solution(object):
    def maximumWealth(self, accounts):
        # res = 0, for each accounts, if sum is greater than current max bank account overwrite for each account
        res = 0

        for i in accounts:
            res = max(res, sum(i))

        return res