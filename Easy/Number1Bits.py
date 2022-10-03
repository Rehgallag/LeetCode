class Solution:
    def hammingWeight(self, n: int) -> int:
        output = 0

        while n:
            n &= (n - 1)
            output += 1

        return output

if __name__ == "__main__":
    sol = Solution()   
    n = 1011
    print(sol.hammingWeight(n))