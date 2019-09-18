### 实际上就是排序字符串的问题，这里就是排序数字

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        li=list(range(1,n+1))
        li.sort(key=str)
        return li