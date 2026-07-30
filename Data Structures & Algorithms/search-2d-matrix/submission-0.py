class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1
        length = len(matrix[0]) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if target <= matrix[mid][length] and target >= matrix[mid][0]:
                left1 = 0
                right1 = len(matrix[0]) - 1
                while left1 <= right1:
                    mid1 = left1 + (right1 - left1) // 2
                    if matrix[mid][mid1] == target:
                        return True
                    elif matrix[mid][mid1] < target:
                        left1 = mid1 + 1
                    else:
                        right1 = mid1 - 1
                return False
            elif target < matrix[mid][0]:
                right = mid - 1
            else:
                left = mid + 1
        return False