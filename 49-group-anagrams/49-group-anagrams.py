class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        mydict = {}
        
        for i in strs:
            if str(sorted(i)) in mydict:
                mydict[str(sorted(i))] += [i]
            else:
                mydict[str(sorted(i))] = [i]
        return mydict.values()