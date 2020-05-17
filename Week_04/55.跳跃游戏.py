#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#
# https://leetcode-cn.com/problems/jump-game/description/
#
# algorithms
# Medium (38.56%)
# Likes:    656
# Dislikes: 0
# Total Accepted:    110.4K
# Total Submissions: 277.2K
# Testcase Example:  '[2,3,1,1,4]'
#
# 给定一个非负整数数组，你最初位于数组的第一个位置。
#
# 数组中的每个元素代表你在该位置可以跳跃的最大长度。
#
# 判断你是否能够到达最后一个位置。
#
# 示例 1:
#
# 输入: [2,3,1,1,4]
# 输出: true
# 解释: 我们可以先跳 1 步，从位置 0 到达 位置 1, 然后再从位置 1 跳 3 步到达最后一个位置。
#
#
# 示例 2:
#
# 输入: [3,2,1,0,4]
# 输出: false
# 解释: 无论怎样，你总会到达索引为 3 的位置。但该位置的最大跳跃长度是 0 ， 所以你永远不可能到达最后一个位置。
#
#
#

# @lc code=start
# Solution 1: The 74th case TLE
# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
#         if not nums:
#             return False
#         len_of_nums = len(nums)
#         can_reach = [False] * len_of_nums
#         can_reach[0] = True
#         for i in range(len_of_nums - 1):
#             if can_reach[i]:
#                 for j in range(nums[i]):
#                     if i + j + 1 < len_of_nums:
#                         can_reach[i + j + 1] = True
#
#         return can_reach[-1]


# Solution 2: greedy
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return False
        len_of_nums = len(nums)
        back_idx, end_reachable = len_of_nums - 1, len_of_nums - 1
        while back_idx >= 0:
            if nums[back_idx] + back_idx >= end_reachable:
                end_reachable = back_idx
            back_idx -= 1

        return end_reachable == 0


# @lc code=end
