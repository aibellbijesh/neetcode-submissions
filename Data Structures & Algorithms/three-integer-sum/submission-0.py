class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        num = sorted(nums)
        for i, a in enumerate(num):
            if i>0 and a == num[i-1] :
                continue;
            l,r = i+1, len(num)-1
            while l < r:
                total = a + num[l] + num[r]        
                if total>0:
                    r-= 1
                elif total<0:
                    l+=1
                else:
                    res.append([a, num[l], num[r]])
                    l += 1
                    while l < r and num[l] == num[l-1]:
                        l += 1
    
        return res
            