class Solution:
    def getRow(self, row: int) -> List[int]:
        '''
        recursion solution
        2 base cases: row = 0 return [1]
        row = 1 return [1,1]
        '''
        if row == 0:
            return [1]
        if row == 1:
            return [1,1]
        prev_r = self.getRow(row - 1)
        new_r = [1 for _ in range(len(prev_r)+1)]
        for i in range(len(prev_r) - 1):
            new_r[i + 1] = prev_r[i] + prev_r[i+1]
        return new_r