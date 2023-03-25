#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # do binary search
        def helper(subnums: List[int], pos: int):
            if len(subnums) == 0:
                return pos
            mid = len(subnums) // 2
            if subnums[mid] == target:
                return pos+mid
            elif subnums[mid] < target:
                return helper(subnums[mid+1:], pos+mid+1)
            else:
                return helper(subnums[:mid], pos)
        return helper(nums, 0)
# @lc code=end

