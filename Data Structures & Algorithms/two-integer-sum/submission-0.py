class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        l = len(nums)
        for i in range(l):
            if target - nums[i] in dic:
                return [dic[target - nums[i]], i]
            dic[nums[i]] = i
