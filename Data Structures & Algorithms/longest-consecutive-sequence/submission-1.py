class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        longest = 0 
        for num  in seen:
            if num-1 not in seen:
                length = 1
                current  = num
                while current+1 in seen :
                    current +=1
                    length += 1
                longest = max(length,longest)
        return longest
