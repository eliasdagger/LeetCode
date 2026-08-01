class Solution(object):
    def threeConsecutiveOdds(self, arr):
        # use a sliding window technique to scan if there are three consecutive odd numbers
        for i in range(len(arr) - 2):
            if arr[i] % 2 != 0 and arr[i+1] % 2 != 0 and arr[i+2] % 2 != 0:
                return True

        return False