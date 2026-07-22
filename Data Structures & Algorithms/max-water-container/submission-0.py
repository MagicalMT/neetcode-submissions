class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maximum = 0
        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                store = (j-i) * min(heights[i], heights[j])
                if store >= maximum:
                    maximum = store
        return maximum