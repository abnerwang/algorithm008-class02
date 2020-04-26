#
# @lc app=leetcode.cn id=589 lang=python3
#
# [589] N叉树的前序遍历
#
# https://leetcode-cn.com/problems/n-ary-tree-preorder-traversal/description/
#
# algorithms
# Easy (72.73%)
# Likes:    75
# Dislikes: 0
# Total Accepted:    24.2K
# Total Submissions: 33.2K
# Testcase Example:  '[1,null,3,2,4,null,5,6]'
#
# 给定一个 N 叉树，返回其节点值的前序遍历。
#
# 例如，给定一个 3叉树 :
#
#
#
#
#
#
#
# 返回其前序遍历: [1,3,5,6,2,4]。
#
#
#
# 说明: 递归法很简单，你可以使用迭代法完成此题吗?
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    # Solution 1
    # def __init__(self):
    #     self._res = []

    # def preorder(self, root: 'Node') -> List[int]:
    #     if root:
    #         self._res.append(root.val)
    #         for child in root.children:
    #             self.preorder(child)
    #     return self._res

    # Solution 2
    def preorder(self, root: 'Node') -> List[int]:
        res = []
        if root is None:
            return res
        stack = [root]
        while stack:
            root = stack.pop()
            res.append(root.val)
            len_of_children = len(root.children)
            idx = len_of_children - 1
            while idx >= 0:
                stack.append(root.children[idx])
                idx -= 1
        return res


# @lc code=end
