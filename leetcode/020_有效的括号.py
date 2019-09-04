class Solution:
    def isValid(self, s: str) -> bool:
        dic = {'{': '}',  '[': ']', '(': ')', '?': '?'}
        # if '{' in dic: print(True) => True
        # if '}' not in dic: print(False) => False
        # stack.pop() => '?'
        stack = ['?']
        for c in s:
            if c in dic: stack.append(c)
            elif dic[stack.pop()] != c: return False
            # 顺序 stack.pop()即元素c => dic[stack.pop()]即判断是否dic[c]!=c:
            # 若输入的是'}'则不进第一个if，若进入此elif则pop栈的最上方，
            # 若栈的最上方是'{'则为dic['{']即'}'满足'}'=='}'
        return len(stack) == 1

# 作者：jyd
# 链接：https://leetcode-cn.com/problems/valid-parentheses/solution/valid-parentheses-fu-zhu-zhan-fa-by-jin407891080/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

a = Solution()
print(a.isValid("{[]}"))