# 基本解法。两个指针，若两个相同就删一个
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p1,p2=0,1
        while p2<len(nums):
            if nums[p1]==nums[p2]:
                nums.pop(p2)
            else:
                p1+=1
                p2+=1


a=Solution()
print(a.removeDuplicates([1,2,3]))