# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        # node=TreeNode(nums[int(len(nums)/2)])
        # node.left,node.right=TreeNode(nums[int(len(nums)/3)]),TreeNode(nums[int(len(nums)/1.5)])
        if not nums: return
        mid_i=(len(nums)-1)//2
        node=TreeNode(nums[mid_i])
        node.left=self.sortedArrayToBST(nums[:mid_i])
        node.right=self.sortedArrayToBST(nums[mid_i+1:])
        return node