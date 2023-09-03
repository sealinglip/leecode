#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2020-10-10 08:45:53
LastEditors: Thomas Young
LastEditTime: 2020-10-10 09:06:55
'''
#
# @lc app=leetcode.cn id=142 lang=python3
#
# [142] 环形链表 II
#
# 给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
# 为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置
# （索引从 0 开始）。 如果 pos 是 - 1，则在该链表中没有环。
# 说明：不允许修改给定的链表。

# 示例 1：
# 输入：head = [3, 2, 0, -4], pos = 1
# 输出：tail connects to node index 1
# 解释：链表中有一个环，其尾部连接到第二个节点。

# 示例 2：
# 输入：head = [1, 2], pos = 0
# 输出：tail connects to node index 0
# 解释：链表中有一个环，其尾部连接到第一个节点。

# 示例 3：
# 输入：head = [1], pos = -1
# 输出：no cycle
# 解释：链表中没有环。

# 进阶：
# 你是否可以不用额外空间解决此题？

from listnode import ListNode, printList
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head:
            return None

        slow, fast = head, head
        while fast:
            slow = slow.next
            fast = fast.next
            if not fast:
                return None
            fast = fast.next
            if slow == fast:  # 快指针追上了慢指针
                ptr = head
                while slow != ptr:
                    slow = slow.next
                    ptr = ptr.next
                return ptr
        return None

# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    head = ListNode.convert_list([3, 2, 0, -4])
    head.next.next.next.next = head.next
    printList(solution.detectCycle(head))

    head = ListNode.convert_list([1, 2])
    head.next.next = head
    printList(solution.detectCycle(head))
