
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        every tuple in prerequisites defines an edge in the graph V and prerequisites is E. numCourses dictates how many vertices the graph has numbering
        from 0 to numCourses - 1
        
        Example: num Courses = 2, prereq = [(1,0)] means (0)<------(1)
        
        The problem then becomes detecting if there is a cycle if the DG (Directed Graph). If there is a cycle return False else True
        
        Algorithm:
        Assume we have an adjacency list 
        """
        
        courseDict = {i: [] for i in range(numCourses)}
        
        # for _ in prerequisites:
        #     source, dest = _[1], _[0]
        #     courseDict[source].append(dest)
            
        #create an adjacency list
        for crs, pre in prerequisites:
            courseDict[crs].append(pre)
        # dfs function
        seen = set()
        
        def dfs(crs):
            #base cases
            if crs in seen:
                return False
            if len(courseDict[crs]) == 0:
                return True
            seen.add(crs)
            for pre in courseDict[crs]:
                if not dfs(pre): return False
            seen.remove(crs)
            courseDict[crs] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True
            
        