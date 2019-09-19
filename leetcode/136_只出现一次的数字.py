# 异或解法
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if not nums: return
        res=0
        for i in nums:
            res^=i
        return res

# 常规辣鸡解法
# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         if not nums: return
#         res=[]
#         for i in range(len(nums)):
#             if nums[i] in res: res.remove(nums[i])
#             else: res.append(nums[i])
#         return res[0]