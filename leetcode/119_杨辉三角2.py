# 解法1同前一题把三角做出来return最后一个
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res,counter=[],rowIndex+1
        while counter:
            tmp=[1]
            if not res: res.append(tmp)
            else:
                n=len(res[-1])
                for i in range(1,n):
                    tmp.append(res[-1][i-1]+res[-1][i])
                tmp.append(1)
                res.append(tmp)
            counter-=1
        return res[-1]

# 解法2直接按行求
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res,tmp=[],[1]
        while rowIndex+1:
            arr=[1]
            if not res: res=tmp
            else:
                n=len(res)
                for i in range(1,n):
                    arr.append(res[i-1]+res[i])
                arr.append(1)
                res=arr
            rowIndex-=1
        return res