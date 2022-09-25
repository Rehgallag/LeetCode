from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) -1

        while left <= right:
            mid = (right + left) // 2

            # if x greater, ignore left
            if nums[mid] < target:
                left = mid + 1
            # if x less than, ignore right 
            elif nums[mid] > target:
                right = mid - 1
            # x in the middle
            else:
                return mid
        return -1

if __name__ == "__main__":
    sol = Solution()
    nums, target = [-1,0,3,5,9,12], 9
    print(sol.search(nums,target))