import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        tmp=''.join(re.findall(r'[A-Za-z0-9]', s)).lower()
        l,r=tmp[0:len(tmp)//2],tmp[len(tmp)//2:len(tmp)]
        return l==r[::-1] or l==r[::-1][:-1]