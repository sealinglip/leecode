#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@Description: file content
@Author: Thomas Young
@Date: 2020-06-14 21:26:46
LastEditors: Thomas Young
LastEditTime: 2020-10-18 08:00:02
'''
#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第N个节点
#
# 给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

# 示例：
# 给定一个链表: 1 -> 2 -> 3 -> 4 -> 5, 和 n = 2.
# 当删除了倒数第二个节点后，链表变为 1 -> 2 -> 3 -> 5.

# 说明：
# 给定的 n 保证是有效的。

# 进阶：
# 你能尝试使用一趟扫描实现吗？

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # 我想不出来一趟扫描实现的方法
        # 看了官方的解法，我也不认为是一趟，一个循环，两个指针在跑，还是两趟
        dummy = ListNode(-1) #加一个哑节点，这样如果要删除的就是head，也能正常处理
        dummy.next = head
        first, secode = dummy, dummy

        # first先走n + 1 步
        for i in range(n+1):
            first = first.next

        while first:
            first = first.next
            secode = secode.next

        secode.next = secode.next.next # 删除节点
        return dummy.next

# @lc code=end

