class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        r = 0 
        l = 0
        max_L = 0
        seen = set()
        while r < len(s):
            if s[r] not  in seen:
                seen.add(s[r])
                r += 1
                max_L = max(max_L, r-l)
            else:
                seen.remove(s[l])
                l += 1
        return max_L


