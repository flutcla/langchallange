#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def helper(r: Optional[TreeNode]):
            if r == None : return
            helper(r.left)
            res.append(r.val)
            helper(r.right)
        helper(root)
        return res
# @lc code=end

