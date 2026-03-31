class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        result = 0
        visited = set()
        for num in nums:
            count = 1
            visited.add(num)
            while num+1 in nums:
                visited.add(num+1)
                num = num + 1
                count += 1
            
            result = max(result, count)

        return result