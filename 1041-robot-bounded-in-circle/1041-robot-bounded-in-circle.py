class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        '''
        Draw a cartesian grid to reason through it
        One pass solution only "simulate" a direction once
        In the end check if you have come back to origin (that's a 0 cycle) or
        chec if you changed direction (that's either a 2 cycle or a 4 cycle)
        n-cycle means that the robot comes back to original position in n moves, except
        for the 0 cycle which means 1 move
        '''
        dirX, dirY = 0 , 1
        x, y = 0, 0
        
        for d in instructions:
            #if it's a Go
            if d == "G":
                x, y = x + dirX, y + dirY
                
            #if it's a L
            elif d == "L":
                dirX, dirY = -1*dirY, dirX #visualize this on the Cartesian Plane
            
            #if it's a R
            else:
                dirX, dirY = dirY, -1*dirX #also visualize this on the Cartesian PLane
                
        return (x,y) == (0,0) or (dirX, dirY) != (0,1)
        