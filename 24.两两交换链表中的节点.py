#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@Description: file content
@Author: Thomas Young
@Date: 2020-06-15 05:52:03
LastEditors: Thomas Young
LastEditTime: 2020-10-13 09:43:10
'''
#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#
# 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

# 示例:
# 给定 1 -> 2 -> 3 -> 4, 你应该返回 2 -> 1 -> 4 -> 3.

from listnode import ListNode, printList
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        dummyNode = ListNode(-1)
        dummyNode.next = head
        first, second = dummyNode, dummyNode.next.next  # second 和 first 间隔一个节点

        while second:
            # 交换节点
            tmp = first.next
            first.next = second
            tmp.next = second.next
            second.next = tmp
            second = tmp.next.next if tmp.next else None
            first = tmp

        return dummyNode.next

# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    list = ListNode.convert_list([1, 2, 3, 4, 5])
    list = solution.swapPairs(list)
    printList(list)
