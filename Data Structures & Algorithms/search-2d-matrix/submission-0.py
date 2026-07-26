class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        low, high = 0, (rows * cols) - 1

        while low <= high:
            mid = (low + high) // 2
            mr, mc = mid // cols, mid % cols
            if matrix[mr][mc] == target:
                return True
            elif matrix[mr][mc] > target:
                high = mid - 1
            else:
                low = mid + 1
        
        return False

        