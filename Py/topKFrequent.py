# LeetCode 347 - Top K Frequent Elements (Medium)
#
# Given an integer array nums and an integer k, return the k most frequently
# occurring elements.
#
# The answer may be returned in any order, and the problem guarantees it is
# unique - there are never ties that would make the choice ambiguous.
#
# The follow-up asks for better than O(n log n), so fully sorting the frequency
# counts is not the intended solution; a heap or bucket sort is.
#
# Example: nums = [1,1,1,2,2,3], k = 2  ->  [1,2]
#          nums = [1], k = 1            ->  [1]

class Solution(object):
    def topKFrequent(self, nums, k):
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num,0)

        heap = []
        for num in count.keys():
            heapq.heappush(heap, (count[num], num))
            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """