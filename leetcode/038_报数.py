class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        else:
            li, i, j = [], 1, 0
            li.append("1")
            li.append("11")
            # li[0]=="1"。求li[n-1]
            # 循环从li[1]开始，到li[n-1]结束，即循环定义li[i+1]
            while i < n - 1:
                # li[i]即为字符串，对字符串的每个字符处理
                # 若前a个都是z则li[i+1]就对应的有"az"
                count, s, j = 1, "", 0
                # 记住循环下个循环要重置j
                while j < len(li[i]):
                    j += 1
                    # 当内部循环下标达到最后一个元素时，将这个字符串添加到列表li
                    if len(li[i]) == j:
                        s += str(count) + li[i][j - 1]
                        li.append(s)
                        break
                    if li[i][j] == li[i][j - 1]:
                        count += 1
                    elif li[i][j] != li[i][j - 1]:
                        s += str(count) + li[i][j - 1]
                        # 重置计数器count
                        count = 1
                i += 1
            return li[n - 1]

    # 从后往前推，整了半天没整明白怎么弄，已知后一个报的是前一个
    # 比如“1211”是“一个2一个1”即前一个“21”
    def countAndSay(self, n: int) -> str:
        if n == 1: return "1"
        return self.report()

    def report(self, n)
        if n == 1:
            s = "1"
        else:
            nex, pre = "", ""
            while x < n and x > 0:
                a, b = "", ""
                for i, elm in enumerate(li[n - 1]):
                    if i % 2 == 0:
                        # i为0，2，4，6...是几个几的前面那个几
                        a += li[n - 1][i]
                    if i % 2 == 1:
                        # i为0，2，4，6...是几个几的后面那个几
                        b += li[n - 1][i]
                j = 0
                while j < len(a):
                    li[n - 2] += int(a[i]) * b[j]
                    j += 1

        # s=countAndSay(self,n-1)
        return li[n - 1]


    #从后往前推