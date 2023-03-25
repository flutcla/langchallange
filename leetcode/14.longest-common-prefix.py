#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for i in range(min([len(s) for s in strs])):
            if len({s[i] for s in strs}) == 1:
                res = strs[0][0:i+1]
            else:
                break
        return res
# @lc code=end

