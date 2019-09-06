# 内置函数解法
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack: return -1
        return haystack.index(needle)

    # 取haystack里和needle相同长度的一部分进行比较，若相同则break返回
    # +1是因为如果输入的两个字符串是""和""时应当返回0而不是-1
    def strStr(self, haystack: str, needle: str) -> int:
        c = -1
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i: i + len(needle)] == needle:
                c = i
                break
        return c

# 作者：blaoke
# 链接：https: // leetcode - cn.com / problems / implement - strstr / solution / ji - bai - 999
# de - pythonfang - fa - by - blaoke /
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
