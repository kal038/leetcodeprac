class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        '''
        O(n) solution with O(26) space
        Have an array [0] * 26 to represent 26 letters in alphabet, unicode of letter a is 61
        '''
        return len(set(sentence)) == 26