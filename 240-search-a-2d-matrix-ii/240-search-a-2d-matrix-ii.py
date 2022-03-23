class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        
        h = len(matrix)
        w = len(matrix[0])
        
        row = h - 1
        col = 0
        
        while col < w and row >= 0:
            if matrix[row][col] > target:
                row -=1
            elif matrix[row][col] < target:
                col += 1
            else:
                # matrix[row][col] == target
                return True
        return False # went out of bounds
        