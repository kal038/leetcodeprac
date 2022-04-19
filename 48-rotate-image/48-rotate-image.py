class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def transpose(m):
            for i in range(len(m)):
                for j in range(i+1, len(m)):
                    m[j][i] , m[i][j] = m[i][j], m[j][i]
        def reverse(m):
            for i in range(len(m)):
                m[i].reverse()
                
        transpose(matrix)
        reverse(matrix)
        
        
        
                