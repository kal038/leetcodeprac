class Solution:
    def removeDuplicates(self, s: str) -> str:
        '''
        Use a stack to keep track and to produce the final results of the problem
        For example: "abbaca"
        Start the stack with stack = [a]
        iterate through starting from second index:
        see if the current letter is on top of stack using peek(), if it is, pop from stack
        if it is not, append the current letter to the stack
        This will leave a stack that has elements that represent the resulting string in the end and all we need
        to do is "".join
        '''
        stack = []
        stack.append(s[0])
        for i in range(1,len(s)):
            if len(stack) != 0 and s[i] == stack[-1]:
                stack.pop()
            else:
                stack.append(s[i])
        return "".join(stack)
        