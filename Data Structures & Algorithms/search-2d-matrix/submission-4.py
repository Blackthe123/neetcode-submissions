class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lo = 0
        hi = len(matrix) - 1
        row = -1
        n = len(matrix[0]) - 1
        while lo <= hi:
            mid = (hi + lo) //2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] > target:
                hi = mid - 1
            else:
                if matrix[mid][n] >= target:
                    row = mid
                    break
                else:
                    lo = mid + 1
        if row == -1:
            if lo >= len(matrix):
                row = hi
            else:
                row = lo
        print(row)
        lo = 0
        hi = n
        while lo <= hi:
            mid = (hi + lo) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                hi = mid - 1
            else:
                lo = mid + 1
        return False