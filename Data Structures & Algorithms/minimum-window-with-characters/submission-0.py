class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = {}
        window = {}
        have = 0    
        for char in t:
            need[char] = need.get(char, 0) + 1
        need_count = len(need)
        L, R = 0, 0
        min_length = float("inf")  
        Result = ''
        while R < len(s):
            window[s[R]] = window.get(s[R], 0) + 1
            if s[R] in  need and window[s[R]] == need[s[R]]:
                have += 1            
            while have == need_count:
                win_length = R  - L + 1                          
                if win_length < min_length:
                    min_length = win_length
                    Result = s[L: R+1]
                window[s[L]] -= 1
                if s[L] in need and window[s[L]] < need[s[L]]:
                    have -= 1
                if window[s[L]] == 0:
                    del window[s[L]]
                L += 1
            R += 1
        return Result
        




