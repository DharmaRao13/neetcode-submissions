class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        l = len(heights)
        area = 0
        
        while i < l:
            j = i + 1
            while j < l:
                minNum = min(heights[i], heights[j])
                dist = j - i
                area = max(area, minNum * dist)
                j += 1
            i += 1
        return area
