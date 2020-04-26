#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#
# https://leetcode-cn.com/problems/binary-tree-inorder-traversal/description/
#
# algorithms
# Medium (70.84%)
# Likes:    477
# Dislikes: 0
# Total Accepted:    145.7K
# Total Submissions: 204.8K
# Testcase Example:  '[1,null,2,3]'
#
# 给定一个二叉树，返回它的中序 遍历。
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
# 输出: [1,3,2]
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
    # def inorderTraversal(self, root: TreeNode) -> List[int]:
    #     WHITE, GRAY = 0, 1
    #     res = []
    #     stack = [(WHITE, root)]
    #     while stack:
    #         color, node = stack.pop()
    #         if node is None: continue
    #         if color == WHITE:
    #             stack.append((WHITE, node.right))
    #             stack.append((GRAY, node))
    #             stack.append((WHITE, node.left))
    #         else:
    #             res.append(node.val)
    #     return res

    # Solution 2
    def __init__(self):
        self._res = []

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root:
            self.inorderTraversal(root.left)
            self._res.append(root.val)
            self.inorderTraversal(root.right)
        return self._res


# @lc code=end
