from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        r = [len(set(c)) == 1 for c in zip(*strs)] + [0]
        return strs[0][:r.index(0)] if strs else ''


a = Solution()
print(a.longestCommonPrefix(['ffaa','ffab','ffbb']))

# 若不+[0]，当字符串数组完全一样时，报错 ValueError: 0 is not in list
# 第一行具体步骤为：
# for c in zip(*strs):
#     if len(set(c)) == 1:
#         r = []
#         r.append(c)
#         r.append(0)
# 第二行具体步骤为：
# if strs != []:
#     s = r.index(0)
#     return strs[0][0:s]
# else:
#     return ''



# 作者：QQqun902025048
# 链接：https://leetcode-cn.com/problems/longest-common-prefix/solution/2-xing-python-by-knifezhu-2/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。