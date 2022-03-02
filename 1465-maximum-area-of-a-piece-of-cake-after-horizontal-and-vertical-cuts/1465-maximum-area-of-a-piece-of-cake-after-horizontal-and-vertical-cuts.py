class Solution:
    def maxArea(self, h: int, w: int, hc: List[int], vc: List[int]) -> int:
        hc.append(0)
        hc.append(h)
        hc.sort()
        vc.append(0)
        vc.append(w)
        vc.sort()
        ans1=0
        for i in range(1,len(hc)):
            ans1=max(ans1,hc[i]-hc[i-1])
        ans2=0
        for j in range(1,len(vc)):
            ans2=max(ans2,vc[j]-vc[j-1])
        return ans1*ans2%1000000007
        