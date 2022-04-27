class Solution:
    
    def asteroidCollision(self, ast: List[int]) -> List[int]:
        '''
        use the stack data structure to evaluate collision
        '''
        stack = []
        for a in ast:
            while stack and a < 0 and stack[-1] > 0:
                diff = a + stack[-1]
                if diff < 0:
                    #pop and append
                    stack.pop()
                    
                elif diff > 0:
                    a = 0
                else:
                    a = 0
                    stack.pop()
            if a != 0:
                stack.append(a)
        return stack
        