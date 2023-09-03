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
# 将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。


# 示例 1：
# 输入：l1 = [1, 2, 4], l2 = [1, 3, 4]
# 输出：[1, 1, 2, 3, 4, 4]

# 示例 2：
# 输入：l1 = [], l2 = []
# 输出：[]

# 示例 3：
# 输入：l1 = [], l2 = [0]
# 输出：[0]


# 提示：
# 两个链表的节点数目范围是[0, 50]
# -100 <= Node.val <= 100
# l1 和 l2 均按 非递减顺序 排列

from typing import List
from listnode import ListNode, printList
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

        dummy = ListNode(-1)
        node = dummy
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

        return dummy.next


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    printList(solution.mergeTwoLists(ListNode.convert_list(
        [1, 2, 4]), ListNode.convert_list([1, 3, 4])))  # [1,1,2,3,4,4]
    printList(solution.mergeTwoLists(ListNode.convert_list(
        []), ListNode.convert_list([])))  # []
    printList(solution.mergeTwoLists(ListNode.convert_list(
        []), ListNode.convert_list([0])))  # [0]
