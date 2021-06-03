"""
Given two binary search trees root1 and root2.

Return a list containing all the integers from both trees sorted in ascending order.
leetcode
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

        



class Solution:
    def traversal(self,root,inlist):
        inlist.append(root.val)
        if root.left:
            inlist=self.traversal(root.left,inlist)
        if root.right:
            inlist=self.traversal(root.right,inlist)
        return inlist
    

    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        inlist=[]
        if root1 is not None:
            self.traversal(root1,inlist)
        if root2 is not None:
            self.traversal(root2,inlist)
        return sorted(inlist)
        
"""
Example 1:


Input: root1 = [2,1,4], root2 = [1,0,3]
Output: [0,1,1,2,3,4]
"""
