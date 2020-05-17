#
# @lc app=leetcode.cn id=515 lang=python3
#
# [515] 在每个树行中找最大值
#
# https://leetcode-cn.com/problems/find-largest-value-in-each-tree-row/description/
#
# algorithms
# Medium (58.77%)
# Likes:    62
# Dislikes: 0
# Total Accepted:    11.2K
# Total Submissions: 18.6K
# Testcase Example:  '[1,3,2,5,3,null,9]'
#
# 您需要在二叉树的每一行中找到最大的值。
#
# 示例：
#
#
# 输入:
#
# ⁠         1
# ⁠        / \
# ⁠       3   2
# ⁠      / \   \
# ⁠     5   3   9
#
# 输出: [1, 3, 9]
#
#
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        max_vals_each_level = []
        level = [root]

        while root and level:
            max_vals_each_level.append(max([node.val for node in level]))
            level = [
                child for node in level for child in (node.left, node.right)
                if child
            ]

        return max_vals_each_level


# @lc code=end
