#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2020-10-11 13:27:41
LastEditors: Thomas Young
LastEditTime: 2020-10-11 14:03:46
'''
#
# @lc app=leetcode.cn id=92 lang=python3
#
# [92] 反转链表 II
#
# 反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。

# 说明:
# 1 ≤ m ≤ n ≤ 链表长度。

# 示例:
# 输入: 1 -> 2 -> 3 -> 4 -> 5 -> NULL, m = 2, n = 4
# 输出: 1 -> 4 -> 3 -> 2 -> 5 -> NULL

from listnode import ListNode, printList
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head:
            return head
        dummy = ListNode(-1) # 哑节点
        dummy.next = head

        if m > n:
            m, n = n, m

        if n > m:
            p = dummy
            prePm = None
            for _ in range(m):
                prePm = p
                p = p.next

            pM = p
            pNext = p.next
            for _ in range(n - m):
                pPre = p
                p = pNext
                pNext = p.next
                p.next = pPre
            
            pM.next = pNext
            prePm.next = p
        return dummy.next
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    list = ListNode.convert_list([1, 2, 3, 4, 5])
    solution.reverseBetween(list, 2, 4)
    printList(list)
