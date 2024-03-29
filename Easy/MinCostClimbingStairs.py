from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2])

        return min(cost[0], cost[1])    

if __name__ == "__main__":
    sol = Solution()   
    input = [10,15,20]
    print(sol.minCostClimbingStairs(input))