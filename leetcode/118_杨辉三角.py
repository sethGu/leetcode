# 蠢逼想法，递归里面有循环，只为计算具体值，而每次求结果还要一个一个求
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res=[]
        for i in range(numRows): res.append([])
        def helper(lvl,k):
            if lvl==1:
                return 1
            else:
                tmp=0
                i=0
                while i<k:
                    if i==0 or i==lvl-1: tmp=1
                    else: tmp=helper(lvl-1,k-1)+helper(lvl-1,k)
                    i+=1
                return tmp
        for i in range(numRows):
            for j in range(i+1):
                res[i].append(helper(i+1,j+1))
        return res

# 直白做法，去掉头尾后食用，吃完一层丢一层
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        while numRows:
            tmp = [1]
            if not res:
                res.append(tmp)
            else:
                n = len(res[-1])
                for i in range(1, n):
                    tmp.append(res[-1][i - 1] + res[-1][i])
                tmp.append(1)
                res.append(tmp)
            numRows -= 1
        return res
