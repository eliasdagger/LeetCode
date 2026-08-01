class Solution(object):
    def maximumWealth(self, accounts):
        # res = 0, for each accounts, if sum is greater than current max bank account overwrite for each account
        res = 0

        for i in accounts:
            res = max(res, sum(i))

        return res