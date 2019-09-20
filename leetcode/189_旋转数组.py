# 取余
# 方法一：插入
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k%=len(nums)
        for i in range(k):
            nums.insert(0,nums.pop())
        return nums

# 方法二：观察发现规律，可以使用三次旋转，前中后，耗时两倍少于插入
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lens=len(nums)
        k%=lens
        nums[:]=nums[::-1]
        nums[:k]=nums[:k][::-1]
        nums[k:]=nums[k:][::-1]
        return nums



