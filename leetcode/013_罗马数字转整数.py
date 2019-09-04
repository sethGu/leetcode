# 使用遍历字符串,naive地进行操作,要注意IV这种V也要判断的情况,for循环idx+1超出范围
class Solution:
    def romanToInt(self, s: str) -> int:
        p = 0
        for idx, i in enumerate(s):
            if i == "I":
                if idx + 1 < len(s):
                    if s[idx + 1] == "V" or s[idx + 1] == "X":
                        p -= 1
                    else:
                        p += 1
                else:
                    p += 1
            if i == "V": p += 5
            if i == "X":
                # print(idx,len(s))
                if idx + 1 < len(s):
                    if s[idx + 1] == "L" or s[idx + 1] == "C":
                        p -= 10
                    else:
                        p += 10
                else:
                    p += 10
            if i == "L": p += 50
            if i == "C":
                if idx + 1 < len(s):
                    if s[idx + 1] == "D" or s[idx + 1] == "M":
                        p -= 100
                    else:
                        p += 100
                else:
                    p += 100
            if i == "D": p += 500
            if i == "M": p += 1000

        return p


a = Solution()
print(a.romanToInt("III"))

# 使用字典，2行代码
# class Solution:
#     def romanToInt(self, s: str) -> int:
#         d = {'I':1, 'IV':3, 'V':5, 'IX':8, 'X':10, 'XL':30, 'L':50, 'XC':80, 'C':100, 'CD':300, 'D':500, 'CM':800, 'M':1000}
#         return sum(d.get(s[max(i-1, 0):i+1], d[n]) for i, n in enumerate(s))
