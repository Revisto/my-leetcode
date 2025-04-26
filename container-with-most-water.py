class Solution:
    def maxArea(self, height) -> int:
        p1 = 0
        p2 = len(height) - 1
        max_water = 0
        
        while (p1 < p2):
            current_water = (p2 - p1) * min(height[p1], height[p2])
            max_water = max(max_water, current_water)
            
            if height[p1] == height[p2]:
                p1 += 1
                p2 -= 1
            elif height[p1] > height[p2]:
                p2 -= 1
            else:
                p1 += 1
        return max_water
    
print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))