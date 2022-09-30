import heapq
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            largest = heapq.heappop(stones)
            second = heapq.heappop(stones)

            if second > largest:
                heapq.heappush(stones, largest - second)
        stones.append(0)
        return abs(stones[0])


# if __name__ == "__main__":
#     sol = Solution()   