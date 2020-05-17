#
# @lc app=leetcode.cn id=367 lang=python3
#
# [367] 有效的完全平方数
#
# https://leetcode-cn.com/problems/valid-perfect-square/description/
#
# algorithms
# Easy (43.29%)
# Likes:    120
# Dislikes: 0
# Total Accepted:    31.8K
# Total Submissions: 73.3K
# Testcase Example:  '16'
#
# 给定一个正整数 num，编写一个函数，如果 num 是一个完全平方数，则返回 True，否则返回 False。
#
# 说明：不要使用任何内置的库函数，如  sqrt。
#
# 示例 1：
#
# 输入：16
# 输出：True
#
# 示例 2：
#
# 输入：14
# 输出：False
#
#
#


# @lc code=start
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        low, high = 1, num
        while low <= high:
            mid = (low + high) >> 1
            if mid * mid > num:
                high = mid - 1
            elif mid * mid < num:
                low = mid + 1
            else:
                return True
        return False


# @lc code=end
