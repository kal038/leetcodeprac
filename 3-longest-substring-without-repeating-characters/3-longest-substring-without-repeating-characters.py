class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        chars = [0] * 128
        l = 0
        r = 0
        res = 0
        while l <= r and r < len(s):
            r_letter = s[r]
            chars[ord(r_letter)] += 1
            while(chars[ord(r_letter)] > 1):
                l_letter = s[l]
                chars[ord(l_letter)] -= 1
                l += 1
            res = max(res, r-l+1)
            r += 1
        return res
        
        