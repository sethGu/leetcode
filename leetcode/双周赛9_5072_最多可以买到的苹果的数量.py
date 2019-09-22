class Solution:
    def maxNumberOfApples(self, arr: List[int]) -> int:
        arr.sort()
        s,k=0,0
        for i in arr:
            if s+i<5000:
                s+=i
                k+=1
            else: break
        return k