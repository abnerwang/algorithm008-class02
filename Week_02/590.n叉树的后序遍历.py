#
# @lc app=leetcode.cn id=590 lang=python3
#
# [590] N叉树的后序遍历
#
# https://leetcode-cn.com/problems/n-ary-tree-postorder-traversal/description/
#
# algorithms
# Easy (72.79%)
# Likes:    61
# Dislikes: 0
# Total Accepted:    20.9K
# Total Submissions: 28.6K
# Testcase Example:  '[1,null,3,2,4,null,5,6]'
#
# 给定一个 N 叉树，返回其节点值的后序遍历。
#
# 例如，给定一个 3叉树 :
#
#
#
#
#
#
#
# 返回其后序遍历: [5,6,3,2,4,1].
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

    # def postorder(self, root: 'Node') -> List[int]:
    #     if root:
    #         for child in root.children:
    #             self.postorder(child)
    #         self._res.append(root.val)
    #     return self._res

    # Solution 2
    def postorder(self, root: 'Node') -> List[int]:
        res = []
        if root is None:
            return res
        stack = [root]
        while stack:
            root = stack.pop()
            res.append(root.val)
            len_of_children = len(root.children)
            idx = 0
            while idx < len_of_children:
                stack.append(root.children[idx])
                idx += 1
        return res[::-1]


# @lc code=end
