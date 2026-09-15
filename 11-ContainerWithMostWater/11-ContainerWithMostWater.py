# Last updated: 15/9/2026, 11:38:32 pm
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r = 0,len(height)-1
        maxl,maxr = height[l],height[r]
        largest = max(height)
        ans = 0
        # print(ans)

        while (r-l)*largest>ans:
            if height[l]==maxl or height[r]==maxr:
                ans = max(ans,min(maxr,maxl)*(r-l))
            if maxl<=maxr:
                l += 1
                if height[l]>maxl:
                    maxl = height[l]
            else:
                r -= 1
                if height[r]>maxr:
                    maxr = height[r]
        
        return ans