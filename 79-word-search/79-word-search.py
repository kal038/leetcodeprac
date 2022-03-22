class Solution(object):
    def exist(self, board, word):
        """
        backtracking algorithm
        for each cell in the matrix, we run a backtrack() function to check if there could be a solution starting 
        from this cell
        rows = len(board)
        cols = len(board[0])
        
        
        backtrack(row, col, curr_word):
            check if we hit the target word (len of suffix is 0). Since we are slicing off 1 starting letter each match
            example "dog" and we are on letter "d", then we run backtrack recursively on "og"... until we get ""
            check  if the current state is invalid, 
                1. either row or col is out of bounds
                2. the current word does not match up with the target word
            if valid: then start backtracking recursively 
                1. mark the current cell as visited (use a number)
                2. define north, west, east , south directions
                3. upon return up the call stack, prune to original state
        """
        
        rows = len(board)
        cols = len(board[0])
        path = set()
        
        def backtrack(row, col, i):
            if i == len(word):
                return True
            if row < 0 or row >= rows or col < 0 or col >= cols or board[row][col] != word[i] or (row,col) in path:
                return False
            
            path.add((row,col))
            res = (backtrack(row+1, col, i+1) or
                   backtrack(row-1, col, i+1) or
                   backtrack(row, col + 1, i + 1 ) or
                   backtrack (row, col -1, i + 1))
            path.remove((row,col))
            return res
            
        
        for r in range(rows):
            for c in range(cols):
                if backtrack(r,c,0):
                    return True
                
        return False
        