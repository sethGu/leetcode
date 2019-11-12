class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        n=bin(n)
        s=str(n)
        res=0
        for i in s:
            if i=='1': res+=1
        return res