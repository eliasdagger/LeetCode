# LeetCode 1046 - Last Stone Weight (Easy)
#
# You have an array stones where stones[i] is the weight of the i-th stone. On
# each turn, take the two heaviest stones and smash them together:
#
#   if they weigh the same, both stones are destroyed
#   if they differ, the lighter one is destroyed and the heavier one is left
#   weighing the difference between them
#
# Repeat until at most one stone remains, and return the weight of that stone -
# or 0 if none are left.
#
# Because you always need the two largest values, a max-heap is the natural fit.
#
# Example: [2,7,4,1,8,1]  ->  1


import heapq


def lastStoneWeight(stones) -> int:
    stones = [-s for s in stones]
    heapq.heapify(stones)
    # [2, 3, 3, 4, 4]
    while len(stones) > 1:
        print(stones)
      
        x = heapq.heappop(stones)
        y = heapq.heappop(stones)

        if x != y:
            z = -1 * abs(x - y)
            heapq.heappush(stones, z)
            
    return -1 * sum(stones)



print(lastStoneWeight([4, 4, 3, 3, 2]))

        