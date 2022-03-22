class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        
        Vertical scan idea
        flower
        flow
        flight
        ^
        """
        res = ""
        if len(strs) == 0:
            return res
        for i in range(len(min(strs))):
            c = strs[0][i]
            if all(a[i] == c for a in strs):
                res += c
            else:
                break
        return res
        