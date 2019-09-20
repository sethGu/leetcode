class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if not numbers: return
        s,l=0,len(numbers)-1
        while s!=l:
            if numbers[s]+numbers[l]<target: s+=1
            elif numbers[s]+numbers[l]>target: l-=1
            else: return [s+1,l+1]