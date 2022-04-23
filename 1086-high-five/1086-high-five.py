class Solution:
    import heapq
    import math
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        '''
        after working on a problem for a bit, one should realize it is a GET TOP K ELEMENTS PRBLEM -> HEAPPPPP!
        '''
        items = sorted(items, key = lambda x: x[0])
        prev_id = items[0][0]
        res = []
        curr_grades = []

        for entry in items:
            if prev_id == entry[0]:
                curr_grades.append(entry[1])
            else:
                avg = sum(heapq.nlargest(5,curr_grades))/5
                res.append([prev_id, math.floor(avg)])
                prev_id = entry[0]
                curr_grades = [entry[1]]
        avg = sum(heapq.nlargest(5,curr_grades))/5
        res.append([prev_id, math.floor(avg)])
        return res
                
               