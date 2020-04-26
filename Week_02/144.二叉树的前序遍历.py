#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] 二叉树的前序遍历
#
# https://leetcode-cn.com/problems/binary-tree-preorder-traversal/description/
#
# algorithms
# Medium (64.96%)
# Likes:    245
# Dislikes: 0
# Total Accepted:    95.9K
# Total Submissions: 147K
# Testcase Example:  '[1,null,2,3]'
#
# 给定一个二叉树，返回它的 前序 遍历。
#
# 示例:
#
# 输入: [1,null,2,3]
# ⁠  1
# ⁠   \
# ⁠    2
# ⁠   /
# ⁠  3
#
# 输出: [1,2,3]
#
#
# 进阶: 递归算法很简单，你可以通过迭代算法完成吗？
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
    # Solution 1
    # def preorderTraversal(self, root: TreeNode) -> List[int]:
    #     WHITE, GRAY = 0, 1
    #     res = []
    #     stack = [(WHITE, root)]
    #     while stack:
    #         color, node = stack.pop()
    #         if node is None: continue
    #         if color == WHITE:
    #             stack.append((WHITE, node.right))
    #             stack.append((WHITE, node.left))
    #             stack.append((GRAY, node))
    #         else:
    #             res.append(node.val)
    #     return res

    # Solution 2
    def __init__(self):
        self._res = []

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root:
            self._res.append(root.val)
            self.preorderTraversal(root.left)
            self.preorderTraversal(root.right)
        return self._res


# @lc code=end
