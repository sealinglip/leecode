#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@Description: file content
@Author: Thomas Young
@Date: 2020-06-14 14:32:08
@LastEditors: Thomas Young
@LastEditTime: 2020-06-14 14:46:25
'''
#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l2:
            return l1
        elif not l1:
            return l2
        
        fakeHead = ListNode(-1)
        node = fakeHead
        while l1 and l2:
            if l1.val < l2.val:
                node.next = l1
                node = l1
                l1 = l1.next
            else:
                node.next = l2
                node = l2
                l2 = l2.next
        
        node.next = l1 if l1 else l2

        return fakeHead.next

        
# @lc code=end

