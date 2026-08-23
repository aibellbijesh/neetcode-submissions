class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L, R = 0, 0
        count = {}
        max_len = 0
        while R < len(s):
            count[s[R]] = count.get(s[R], 0) + 1
            most_freq = max(count.values())
            win_len = R - L + 1    
            rplcmt = win_len - most_freq
            if rplcmt > k :
                count[s[L]] -= 1
                L += 1
            else:
                max_len = max(max_len, win_len)
            R += 1
        return max_len
