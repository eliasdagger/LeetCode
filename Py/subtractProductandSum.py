class Solution(object):
    def subtractProductAndSum(self, n):
        # base case
        if n == 0:
            return 0
        # 0 for sum, start prod at 1 as base
        s = 0
        p = 1
        n = str(n)
        for i in n:
            p = p * int(i)
            s += int(i)
        
        
        return p - s