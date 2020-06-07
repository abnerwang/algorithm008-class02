#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#
# https://leetcode-cn.com/problems/generate-parentheses/description/
#
# algorithms
# Medium (73.74%)
# Likes:    1005
# Dislikes: 0
# Total Accepted:    124.2K
# Total Submissions: 164.9K
# Testcase Example:  '3'
#
# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
#
#
#
# 示例：
#
# 输入：n = 3
# 输出：[
# ⁠      "((()))",
# ⁠      "(()())",
# ⁠      "(())()",
# ⁠      "()(())",
# ⁠      "()()()"
# ⁠    ]
#
#
#


# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        all_valid_parentheses = []

        def dfsParentheses(cur_parenthesis: str, left: int, right: int):
            if len(cur_parenthesis) == 2 * n:
                all_valid_parentheses.append(cur_parenthesis)
                return

            if left < n:
                dfsParentheses(cur_parenthesis + '(', left + 1, right)
            if right < left:
                dfsParentheses(cur_parenthesis + ')', left, right + 1)

        dfsParentheses('', 0, 0)

        return all_valid_parentheses


# @lc code=end
