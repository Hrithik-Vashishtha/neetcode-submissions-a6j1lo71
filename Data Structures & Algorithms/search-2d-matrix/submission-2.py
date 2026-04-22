class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for r in range(len(matrix)):
            if matrix[r][-1] >= target:
                i = 0
                j = len(matrix[i])-1

                while i <= j:
                    mid = (i + j) // 2
                    if matrix[r][mid] == target:
                        return True

                    elif matrix[r][mid] > target:
                        j = mid-1

                    else:
                        i = mid+1

        return False