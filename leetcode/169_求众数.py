class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d={}
        for i in nums:
            if i not in d: d[i]=1
            else: d[i]+=1
        m=i
        for j in d:
            if d[j]>d[m]: m=j
        return m