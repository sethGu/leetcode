# 转list解法
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        if x == 0: return True
        # 左列表是 按x的顺序int->str->list
        # 右列表是 把x反顺序int->str->list
        le, ri = [], []
        xstr = str(x)
        for i in xstr: le.append(i)
        while x>0:
            temp = str(x%10)
            ri.append(temp)
            x //= 10
        if le == ri: return True
        else: return False


# 转字符串解法，一行代码，[::-1]即为反转字符串
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]


# 也是转list解法，比第一种好不到哪里去
class Solution:
    def isPalindrome(self, x: int) -> bool:
        r = list(map(lambda i: int(10**-i * x % 10), range(int(math.log10(x)), -1, -1))) if x > 0 else [0, x]
        return r == r[::-1]

