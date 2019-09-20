# 暴力遍历在这题无法通过测试用例，尝试别的方法

# 方法一， nums.index()
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        # nums.index(target-nums[i])
        while i < len(nums):
            if (target - nums[i]) in nums:
                j = nums.index(target - nums[i])
                if j == i:
                    i += 1
                    continue
                else:
                    return [i, j]
            i += 1

# 方法二， 字典模拟hash，更优解法
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        for idx,num in enumerate(nums):
            hashmap[num]=idx
        for i,num in enumerate(nums):
            j=hashmap.get(target-num)
            # 字典存在None导致条件不符合，需要加入not None
            if i!=j and j is not None: return[i,j]
            else: continue