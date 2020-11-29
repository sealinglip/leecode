#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2020-06-10 22:36:18
LastEditors: Thomas Young
LastEditTime: 2020-10-04 07:14:36
'''
#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#
# 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

# 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

# 您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

# 示例：

# 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807

from listnode import ListNode, printList
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from typing import Tuple
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 or not l2:
            return l2 if l2 else l1

        def addNode(l1: ListNode, l2: ListNode, carry: int) -> Tuple:
            node = None
            sum = l1.val + l2.val + carry
            if sum >= 10:
                sum -= 10
                carry = 1
            else:
                carry = 0

            node = ListNode(sum)
            return node, carry

        dummy = ListNode(-1)
        carry = 0
        node = dummy
        while l1 and l2:
            n, carry = addNode(l1, l2, carry)
            node.next = n
            node = n
            l1, l2 = l1.next, l2.next
            
        l = l1 or l2
        while l:
            sum = carry + l.val
            if sum >= 10:
                sum -= 10
                carry = 1
            else:
                carry = 0
            n = ListNode(sum)
            node.next = n
            node = n
            l = l.next

        if carry:
            n = ListNode(carry)
            node.next = n

        return dummy.next

# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    printList(solution.addTwoNumbers(ListNode.convert_list([2, 4, 3]),\
        ListNode.convert_list([5, 6, 4])))
