#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#
# https://leetcode-cn.com/problems/plus-one/description/
#
# algorithms
# Easy (43.71%)
# Likes:    457
# Dislikes: 0
# Total Accepted:    141.3K
# Total Submissions: 322.4K
# Testcase Example:  '[1,2,3]'
#
# 给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。
# 
# 最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
# 
# 你可以假设除了整数 0 之外，这个整数不会以零开头。
# 
# 示例 1:
# 
# 输入: [1,2,3]
# 输出: [1,2,4]
# 解释: 输入数组表示数字 123。
# 
# 
# 示例 2:
# 
# 输入: [4,3,2,1]
# 输出: [4,3,2,2]
# 解释: 输入数组表示数字 4321。
# 
# 
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if not digits:
            return [1]
        len_of_digits = len(digits)
        tail = len_of_digits - 1
        while tail >= 0:
            if digits[tail] == 9:
                digits[tail] = 0
                tail -= 1
            else:
                digits[tail] += 1
                return digits
        return [1] + [0] * len_of_digits
# @lc code=end

