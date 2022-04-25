class Solution:
    def judgeCircle(self, moves: str) -> bool:
        '''
        create an array with 4 integer values dir = {"L": 0, "R":0, "U":0, "D":0} which keep tracks of how many moves in which direction
        after incrementing all the right values, return L == R and U == D
        '''
        if not moves or len(moves) == 0:
            return True
        dirs = {"L": 0, "R":0, "U":0, "D":0}
        for dir in moves:
            dirs[dir] += 1
        return ((dirs["L"] == dirs["R"]) and (dirs["U"] == dirs["D"]))
            

        