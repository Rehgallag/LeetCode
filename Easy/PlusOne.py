from typing import List

class PlusOne:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1,-1,-1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                # digits[-1] += 1
                digits[i] += 1
                return digits
            if i==0:
                digits.insert(0,1)
        return digits
    
p = PlusOne()
digits = [2,9]
print(p.plusOne(digits))