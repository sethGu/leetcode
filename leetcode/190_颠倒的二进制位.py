class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        n=bin(n)
        s=str(n)
        s=s[::-1]
        length=len(s)
        if length<34:
            sup_len=33-length
            s=s.replace('b','0'*sup_len)
        else:
            s=s.strip('b0')
        return int(s,2)