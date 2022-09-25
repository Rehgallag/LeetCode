

import math
import os
import random
import re
import sys


def main():
    s = "()"
    print(isValid(s))



def isValid(self, s:str) -> bool:
    parentheses= {'}':'{', ']':'[', ')':'('}
    if len(s)%2 or s[0] in parentheses: 
        return False
    charStack = []
    for i in s:
        if i in parentheses:
            if not(charStack and charStack[-1] == parentheses[i]):
                    return False
            else:
                charStack.pop()
        else:
            charStack.append(i)
    return len(charStack) == 0    



