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