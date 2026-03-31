class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, l = 0, len(numbers)
        j = l - 1
        while i < j:
            sum_ = numbers[i] + numbers[j]
            if sum_ == target:
                return[i+1, j+1]
            elif sum_ > target:
                j -= 1
            else:
                i += 1