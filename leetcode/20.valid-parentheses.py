#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in ['(', '{', '[']:
                stack.append(char)
            else:
                if stack == []:
                    return False
                top = stack.pop()
                if any([char == ')' and top == '(',
                        char == '}' and top == '{',
                        char == ']' and top == '[']):
                    continue
                else:
                    return False
        return stack == []
# @lc code=end

