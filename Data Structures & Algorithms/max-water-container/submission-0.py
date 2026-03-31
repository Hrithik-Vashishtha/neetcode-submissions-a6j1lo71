class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_amount = float('-inf')
        i, j = 0, len(heights) - 1
        while i < j:
            curr_amount = (j-i) * min(heights[i], heights[j])
            max_amount = max(max_amount, curr_amount)
            if heights[i] <= heights[j]:
                i += 1
            else:
                j -= 1

        return max_amount