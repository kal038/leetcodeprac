class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        '''
        iterative method works 
        idea:
            loop through each row starting from [[1]] and build the next row by appending [0] on both sides of curr_r
        '''
        res = [[1]]
        for i in range(numRows - 1):
            temp = [0] + res[-1] + [0]
            row = []
            for j in range(len(res[-1]) + 1):
                row.append(temp[j] + temp[j+1])
            res.append(row)
        return res
        