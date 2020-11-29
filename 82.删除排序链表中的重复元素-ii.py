#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2020-10-02 09:15:22
LastEditors: Thomas Young
LastEditTime: 2020-10-02 10:16:36
'''
#
# @lc app=leetcode.cn id=82 lang=python3
#
# [82] 删除排序链表中的重复元素 II
#
# 给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。

# 示例 1:

# 输入: 1 -> 2 -> 3 -> 3 -> 4 -> 4 -> 5
# 输出: 1 -> 2 -> 5
# 示例 2:

# 输入: 1 -> 1 -> 1 -> 2 -> 3
# 输出: 2 -> 3

from listnode import ListNode, printList
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head and head.next:
            # 方法1
            # prevPrev = None
            # prev = None
            # node = head
            # markFirst = False
            # duplicate = False
            # while node:
            #     if prev and node.val == prev.val:
            #         duplicate = True
            #         if prevPrev:
            #             prevPrev.next = node.next
            #     else:
            #         if prev and not duplicate:
            #             prevPrev = prev
            #             if not markFirst:
            #                 markFirst = True
            #                 head = prevPrev
            #         prev = node
            #         duplicate = False
            #     node = node.next
            # if not markFirst:
            #     head = prev if not duplicate else None

            # 方法2
            dummy = ListNode(-1)
            tail = dummy
            l, r = head, head
            while l:
                while r and r.val == l.val:
                    r = r.next
                if l.next == r: # 没有重复元素
                    tail.next = l
                    tail = l
                    tail.next = None # 清掉尾巴可能带的未经校验的元素
                l = r
            head = dummy.next
        return head
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    printList(solution.deleteDuplicates(
        ListNode.convert_list([1, 1, 2])))
    printList(solution.deleteDuplicates(
        ListNode.convert_list([1])))
    printList(solution.deleteDuplicates(
        ListNode.convert_list([1, 2])))
    printList(solution.deleteDuplicates(
        ListNode.convert_list([1, 1])))
    printList(solution.deleteDuplicates(
        ListNode.convert_list([1, 2, 3, 3, 4, 4, 5])))
    printList(solution.deleteDuplicates(
        ListNode.convert_list([1, 1, 1, 2, 3])))
