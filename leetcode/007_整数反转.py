# 不用判断正负，直接搞

class Solution:
    def reverse(self, x: int) -> int:
        num, res = abs(x), 0
        std = 2**31-1 if x>0 else 2**31
        while num >0:
            res = num%10 + res*10
            if res > std: return 0
            num //= 10
        return res if x>0 else -res