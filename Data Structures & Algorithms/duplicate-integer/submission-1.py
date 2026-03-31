class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dic = {}
        for num in nums:
            if dic.get(num, 0) == 1:
                return True
            dic[num] = 1
        return False