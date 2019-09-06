class Solution:
    # 内置函数基本解法
    def searchInsert(self, nums: List[int], target: int) -> int:
        if  target not in nums:
            nums.append(target)
            nums.sort()
            return nums.index(target)
        else: return nums.index(target)

    # 二分法查找优化