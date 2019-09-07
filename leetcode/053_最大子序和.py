class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n,tmp=len(nums),nums[0]
        mx=tmp
        for i in range(1,n):
            # 如果tmp加上元素大于该元素，而不是大于tmp
            if tmp+nums[i]>nums[i]: mx,tmp=max(mx,tmp+nums[i]),tmp+nums[i]
            # 记录最大值，重置tmp
            else: mx,tmp=max(mx,tmp,tmp+nums[i],nums[i]),nums[i]
        return mx
