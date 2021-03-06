#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#
# https://leetcode-cn.com/problems/merge-two-sorted-lists/description/
#
# algorithms
# Easy (60.78%)
# Likes:    960
# Dislikes: 0
# Total Accepted:    231.5K
# Total Submissions: 379.1K
# Testcase Example:  '[1,2,4]\n[1,3,4]'
#
# 将两个升序链表合并为一个新的升序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
#
# 示例：
#
# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4
#
#
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if l1.val <= l2.val:
            cur_node = l1
            l1 = l1.next
        else:
            cur_node = l2
            l2 = l2.next
        head = cur_node
        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                cur_node.next = l1
                cur_node = l1
                l1 = l1.next
            else:
                cur_node.next = l2
                cur_node = l2
                l2 = l2.next
        if l1 is None and l2 is not None:
            cur_node.next = l2
        if l2 is None and l1 is not None:
            cur_node.next = l1
        return head


# @lc code=end
