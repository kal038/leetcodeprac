import collections
class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        '''
        backtracking algorithm
        
        allPathsSourceTarget(graph)
        
        result = []
        target = last numbered node
        
        backtrack(node, curr_path):
            base case if node == target:
                append curr_path to result
            loop through the array of neighbors
                add the current choice to path
                explore recursively
                remove the choice from path
                
        backtrack(0, [0])
        return results
        
        complexity O(2^n*n) for both time and space
                
        '''
        
        target = len(graph) - 1
        results = []
        
        def backtrack(node, curr_path):
            if node == target:
                results.append(list(curr_path))
                return
            for neigh in graph[node]:
                curr_path.append(neigh)
                backtrack(neigh, curr_path)
                curr_path.pop()
                
        path  = collections.deque([0])
        backtrack(0, path)
        
        return results
