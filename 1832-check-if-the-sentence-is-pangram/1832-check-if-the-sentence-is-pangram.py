class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        '''
        O(n) solution with O(26) space
        Have set of size O(26) = O(1) to check for every single letter of the alphabet
        '''
        return len(set(sentence)) == 26