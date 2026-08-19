class Solution:
    def trap(self, height: List[int]) -> int:
        total_w = 0
        left_max = 0
        right_max = 0 
        l,r = 0, len(height)-1
        while l<r:
            if height[l] < height[r]:
                left_max = max(left_max, height[l])
                total_w+= left_max-height[l]
                l+=1
            else:
                right_max = max(right_max, height[r])
                total_w+= right_max-height[r]
                r-=1
        return total_w
            
        

