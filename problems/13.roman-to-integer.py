#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        table = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        res = 0
        for i in range(len(s)):
            if i == 0:
                res += table[s[0]]
            else:
                here = table[s[i]]
                left = table[s[i-1]]
                # if increasing, subtract
                if here > left:
                    res -= 2 * left
                res += here
        return res
# @lc code=end

