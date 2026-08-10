class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        left = 0
        prod = 1
        result = 0
        for right in range (len(nums)):
            prod *= nums[right]
            if prod >= k:
                while prod >= k:
                    prod //= nums[left]
                    left += 1
            result += (right - left + 1)
        return result