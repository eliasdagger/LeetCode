class Solution(object):
    def arraySign(self, nums):
        # the sign of a prod is:
        # 1) 0, if there is a single 0 anywhere in the list
        # 2) negative, if there are an odd number of negative numbers in the list, and condition 1 is not met
        # 3) positive, if there are an even number of negative numbers in the list, and condition 1 is not met
        if 0 in nums:
            return 0
        elif sum(x < 0 for x in nums) % 2 != 0:
            return -1
        else:
            return 1
