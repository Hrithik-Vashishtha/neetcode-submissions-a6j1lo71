class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        pre = [1 for i in range(l)]
        post = [1 for i in range(l)]

        for i in range(1, l):
            pre[i] = pre[i-1] * nums[i-1] 

        for i in range(l-2, -1, -1):
            post[i] = post[i+1] * nums[i+1]

        output = [1 for i in range(l)]
        for i in range(l):
            output[i] = pre[i] * post[i]

        return output