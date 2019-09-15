class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        b,a,l,o,n,res=0,0,0,0,0,0
        for i in text:
            if i=="b": b+=2
            if i=="a": a+=2
            if i=="l": l+=1
            if i=="o": o+=1
            if i=="n": n+=2
        res=int(min(b,a,l,o,n)/2)
        return res