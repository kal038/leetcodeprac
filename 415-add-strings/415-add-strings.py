class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        res  = []
        carry = 0
        p1, p2 = len(num1) - 1, len(num2) - 1
        while p1 >= 0 or p2 >= 0:
            x1 = int(num1[p1]) if p1 >= 0 else 0
            x2 = int(num2[p2]) if p2 >= 0 else 0
            val = (x1 + x2 +carry) % 10
            carry = (x1 +x2 +carry) // 10
            res.append(val)
            p1 -= 1
            p2 -= 1
            
        if carry:
            res.append(carry)
            
        return ''.join(str(x) for x in res[::-1])