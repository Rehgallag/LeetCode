from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {} # val : index of target

        for i, n in enumerate(nums):
            diff = target - nums[i]
            if diff in map:
                return [map[diff], i]
            map[n] = i
        return

if __name__ == "__main__":
    sol = Solution()
    nums = [2,1,5,3]; target = 4
    print(sol.twoSum(nums, target))