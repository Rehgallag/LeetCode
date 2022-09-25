class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # from collections import Counter #1

        # return sorted(Counter(s).items()) == sorted(Counter(t).items())

        # return sorted(s) == sorted(t) #2
        # 3
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT


if __name__ == "__main__":
    sol = Solution()
    s = "anagram"; t = "nagaram"
    print(sol.isAnagram(s,t))