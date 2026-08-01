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
        