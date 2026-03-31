class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        l = len(height)
        pre = [0] * l
        post = [0] * l

        pre[0] = height[0]
        post[-1] = height[-1]

        for i in range(1, l):
            pre[i] = max(height[i], pre[i-1])
        
        for i in range(l-2, -1, -1):
            post[i] = max(height[i], post[i+1])

        water = 0
        for i in range(l):
            water += min(pre[i], post[i]) - height[i]

        return water