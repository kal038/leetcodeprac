class Solution:
    def numTeams(self, rating: List[int]) -> int:
        '''
        brute force my way through this shit
        '''
        # res = 0
        # for i in range(len(rating)):
        #     for j in range(i, len(rating)):
        #         for k in range(j, len(rating)):
        #             if  (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k]):
        #                 res += 1
        # return res
        '''
        well brute force did NOT work out too well for me
        An ingenious method is to iterate through the array using each element as the middle soldier
        Then, count the number of bigger_left and smaller_left and bigger_right and smaller_right soldiers from every j position
        Increment the result by (smaller_left * bigger_right + smaller_right * bigger_left) each j
        '''
        res = 0
        for j in range(len(rating)):
            smaller_left, bigger_left = 0, 0
            smaller_right, bigger_right = 0, 0
            for i in range(j-1, -1, -1):
                if rating[i] < rating[j]:
                    smaller_left += 1
                elif rating[i] > rating[j]:
                    bigger_left += 1
            
            for k in range(j+1, len(rating)):
                if rating[k] > rating[j]:
                    bigger_right += 1
                elif rating[k] < rating[j]:
                    smaller_right += 1
                    
            res += smaller_left * bigger_right + smaller_right * bigger_left
            
        return res
            
        
        
        
        
        
        return res
        
        