class Solution(object):
    def letterCasePermutation(self, s):
        """
        784. Letter Case Permutation
        Idea: Recursive Algorithm
        
        
        
        """
  
        res = []
        n = len(s)
        
        def recurse(i = 0, curr = ""):
            if i == n:
                res.append(curr)
            elif s[i].isalpha():
                recurse(i+1, curr + s[i].upper())
                recurse(i+1, curr + s[i].lower())
            else:
                recurse(i+1, curr + s[i])
        
        recurse()
        
        return res