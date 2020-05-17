#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#
# https://leetcode-cn.com/problems/jump-game-ii/description/
#
# algorithms
# Hard (33.59%)
# Likes:    552
# Dislikes: 0
# Total Accepted:    60.1K
# Total Submissions: 165.7K
# Testcase Example:  '[2,3,1,1,4]'
#
# 给定一个非负整数数组，你最初位于数组的第一个位置。
#
# 数组中的每个元素代表你在该位置可以跳跃的最大长度。
#
# 你的目标是使用最少的跳跃次数到达数组的最后一个位置。
#
# 示例:
#
# 输入: [2,3,1,1,4]
# 输出: 2
# 解释: 跳到最后一个位置的最小跳跃数是 2。
# 从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
#
#
# 说明:
#
# 假设你总是可以到达数组的最后一个位置。
#
#

# @lc code=start
# Solution 1: dp, 超时
# class Solution:
#     def jump(self, nums: List[int]) -> int:
#         if not nums:
#             return 0
#         len_of_nums = len(nums)
#         dp = [0] * len_of_nums
#         i = len_of_nums - 2
#
#         while i >= 0:
#             min_jump_counts = float(inf)
#             for count in range(1, nums[i] + 1):
#                 if i + count < len_of_nums:
#                     if min_jump_counts > 1 + dp[i + count]:
#                         min_jump_counts = 1 + dp[i + count]
#                 else:
#                     break
#
#             dp[i] = min_jump_counts
#             i -= 1
#         return dp[0]


# Solution 2: 利用二叉树 BFS 思想
class Solution:
    def jump(self, nums: List[int]) -> int:
        len_of_nums = len(nums)
        if len_of_nums < 2: return 0
        old_farthest_idx, farthest_idx, min_jump_counts = 0, nums[0], 1

        while farthest_idx < len_of_nums - 1:
            min_jump_counts += 1
            next_farest_idx = max(
                i + nums[i] for i in range(old_farthest_idx, farthest_idx + 1))
            old_farthest_idx, farthest_idx = farthest_idx, next_farest_idx

        return min_jump_counts


# @lc code=end
