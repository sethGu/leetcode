class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums)==0: return 0
        p=0
        while p<len(nums):
            if nums[p]==val:
                nums.pop(p)
                p-=1
            p+=1
        return len(nums)