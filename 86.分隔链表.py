#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2020-10-03 22:40:37
LastEditors: Thomas Young
LastEditTime: 2020-10-03 22:55:13
'''
#
# @lc app=leetcode.cn id=86 lang=python3
#
# [86] 分隔链表
#
# 给定一个链表和一个特定值 x，对链表进行分隔，使得所有小于 x 的节点都在大于或等于 x 的节点之前。
# 你应当保留两个分区中每个节点的初始相对位置。

# 示例:
# 输入: head = 1 -> 4 -> 3 -> 2 -> 5 -> 2, x = 3
# 输出: 1 -> 2 -> 2 -> 4 -> 3 -> 5

from listnode import ListNode, printList
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if head and head.next:
            dummy = ListNode(-1)
            dummyX = ListNode(x)

            node, tail, tailX = head, dummy, dummyX
            while node:
                if node.val >= x:
                    tailX.next = node
                    tailX = node
                else:
                    tail.next = node
                    tail = node
                node = node.next

            tail.next = dummyX.next
            tailX.next = None
            head = dummy.next
            
        return head
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    printList(solution.partition(ListNode.convert_list([1]), 0))
    printList(solution.partition(ListNode.convert_list([1, 4, 3, 2, 5, 2]), 3))
