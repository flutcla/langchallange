#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def helper(l, r) -> bool:
            if l == None or r == None:
                return l == r == None
            return l.val == r.val and helper(l.left, r.right) and helper(l.right, r.left)
        return helper(root.left, root.right)
# @lc code=end

