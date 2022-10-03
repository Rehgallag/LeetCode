from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        output = 0

        for n in nums:
            output = n ^ output   

        return output

if __name__ == "__main__":
    sol = Solution()   
    nums = [4,1,2,1,2]
    print(sol.singleNumber(nums))