class Solution:
    def isHappy(self, n: int) -> bool:
        start = set()
        while(n not in start):
            start.add(n)
            
            n=self.squareSum(n)
            if(n==1):
                return True
        return False
    def squareSum(self, n:int):
        output=0
        while(n):
            digit=n%10
            output+=digit**2
            n=n//10
        return output