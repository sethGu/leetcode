class Solution:
    # python3，分两种情况
    # arr本身大于0就拿头尾，其余中间部分直接sum()，相加取模
    # arr小于0的话直接取前中后三个arr就够了，根据测试用例范围不需要取模
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        if sum(arr)>0:
            nums=arr*2
            for i in range(1, len(nums)):
                nums[i] = max(nums[i], nums[i] + nums[i-1])
            res1=max(nums)+(sum(arr))*(k-2)
            return res1%(pow(10,9)+7)
        else:
            for j in arr:
                if j<0:
                    nums=arr*3
                    break
            for i in range(1, len(nums)):
                # 当前索引i永远存储0~i的最大和
                nums[i] = max(nums[i], nums[i] + nums[i - 1])
            # 返回每个索引最大和的最大值
            res=max(0,max(nums))
            return res

