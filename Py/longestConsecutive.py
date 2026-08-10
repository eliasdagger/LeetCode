# LeetCode 128 - Longest Consecutive Sequence (Medium)
#
# Given an unsorted array of integers nums, return the length of the longest run
# of consecutive integers that appear in it.
#
# The numbers do not need to sit next to each other in the array - only their
# values matter. Duplicates do not extend a run.
#
# The real problem asks for an O(n) solution, so sorting the array first is a
# fallback rather than the intended answer.
#
# Example: [100,4,200,1,3,2]  ->  4 (the sequence 1, 2, 3, 4)

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # count start at 0 for empty set case
        c = 0
        # sort in order and remove duplicates
        n = sorted(set(nums))
        for i in range(len(n)):
            c2 = 1
            # start index + 1 from where we left off
            for j in range(i + 1, len(n)):
                # if n[j - 1] is greater than its previous then increment
                if n[j] == n[j - 1] + 1:
                    c2 +=1
                # not consecutive case, break immediately
                else:
                    break
            # if this iters count is greater than max count than rewrite it
            if c2 > c:
                c = c2
        return c