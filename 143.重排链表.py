#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2020-10-20 08:21:39
LastEditors: Thomas Young
LastEditTime: 2020-10-20 08:53:58
'''
#
# @lc app=leetcode.cn id=143 lang=python3
#
# [143] 重排链表
#
# 给定一个单链表 L：L0→L1→…→Ln-1→Ln ，
# 将其重新排列后变为： L0→Ln→L1→Ln-1→L2→Ln-2→…

# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

# 示例 1:
# 给定链表 1 -> 2 -> 3 -> 4, 重新排列为 1 -> 4 -> 2 -> 3.

# 示例 2:
# 给定链表 1 -> 2 -> 3 -> 4 -> 5, 重新排列为 1 -> 5 -> 2 -> 4 -> 3.

from listnode import ListNode, printList
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return

        # 先找到列表的中间节点和列表的长度
        fast = slow = head
        N = 0
        while fast:
            fast = fast.next
            N += 1
            if fast:
                fast = fast.next
                N += 1
                slow = slow.next
            
        if N > 1:
            # 此时fast指向None，slow指向中间节点，N为列表长度
            # 逆序（slow，fast）之间的列表
            head2 = slow.next
            slow.next = None
            prev = None
            while head2:
                next = head2.next
                head2.next = prev
                prev = head2
                if not next:
                    break
                head2 = next

            # 合并head 和head2 两个列表
            while head2:
                next2 = head2.next
                next = head.next
                head.next = head2
                head2.next = next
                head = next
                head2 = next2

# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    head = ListNode.convert_list([1, 2, 3, 4])
    solution.reorderList(head)
    printList(head)

    head = ListNode.convert_list([1, 2, 3, 4, 5])
    solution.reorderList(head)
    printList(head)

    head = ListNode.convert_list([1, 2, 3, 4, 5, 6, 7, 8])
    solution.reorderList(head)
    printList(head)
