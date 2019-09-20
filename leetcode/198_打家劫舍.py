# 动态规划，从n=1,n=2,n=3总结出到n的规律，发现最大值为max( f(x-2)+i, f(x-1))
# 这其中f(x-2)可表示为上上次迭代后的结果pre，而f(x-1)可表示为上一次迭代后的结果cur
class Solution:
    def rob(self, nums: List[int]) -> int:
        pre,cur=0,0
        for i in nums:
            tmp=cur
            cur=max(pre+i,cur)
            pre=tmp
        return cur