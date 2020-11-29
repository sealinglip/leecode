#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2020-11-20 09:52:35
LastEditors: Thomas Young
LastEditTime: 2020-11-20 10:05:24
'''
#
# @lc app=leetcode.cn id=147 lang=python3
#
# [147] 对链表进行插入排序
#
# 对链表进行插入排序。

# 插入排序的动画演示如上。从第一个元素开始，该链表可以被认为已经部分排序（用黑色表示）。
# 每次迭代时，从输入数据中移除一个元素（用红色表示），并原地将其插入到已排好序的链表中。

# 插入排序算法：
# 插入排序是迭代的，每次只移动一个元素，直到所有元素可以形成一个有序的输出列表。
# 每次迭代中，插入排序只从输入数据中移除一个待排序的元素，找到它在序列中适当的位置，并将其插入。
# 重复直到所有输入数据插入完为止。

# 示例 1：
# 输入: 4 -> 2 -> 1 -> 3
# 输出: 1 -> 2 -> 3 -> 4

# 示例 2：
# 输入: -1 -> 5 -> 3 -> 4 -> 0
# 输出: -1 -> 0 -> 3 -> 4 -> 5

from listnode import ListNode, printList
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        
        dummy = ListNode(-1)
        dummy.next = head
        last = head # 最后一个排好序的节点
        cur = head.next # 待插入的节点

        while cur:
            if last.val <= cur.val:
                last = cur
            else:
                prev = dummy
                while prev.next.val <= cur.val:
                    prev = prev.next
                last.next = cur.next
                cur.next = prev.next
                prev.next = cur 
            cur = last.next
            
        return dummy.next
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    listNode = solution.insertionSortList(ListNode.convert_list([4, 2, 1, 3]))
    printList(listNode)
    listNode = solution.insertionSortList(ListNode.convert_list([-1, 5, 3, 4, 0]))
    printList(listNode)