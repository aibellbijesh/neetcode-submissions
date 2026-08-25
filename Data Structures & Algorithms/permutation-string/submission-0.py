class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = {}
        count2 = {}
        for char in s1:
            count1[char] = count1.get(char, 0) + 1
        L,R = 0, 0
        while R < len(s2):
            count2[s2[R]] = count2.get(s2[R], 0) + 1
            if R-L + 1 > len(s1):
                count2[s2[L]] -= 1 
                if count2[s2[L]] == 0:
                    del count2[s2[L]]
                L += 1
            if count1 == count2:
                return True  
            R += 1
        return False