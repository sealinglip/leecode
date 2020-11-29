#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@Description: file content
@Author: Thomas Young
@Date: 2020-06-13 10:15:38
@LastEditors: Thomas Young
@LastEditTime: 2020-07-02 21:42:20
'''
#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并K个排序链表
#
from typing import List
from listnode import ListNode, printList

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from queue import PriorityQueue

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None

        # 删掉空节点
        lists = [a for a in lists if a]
        if not lists:
            return None

        head = ListNode(-1)
        tail = head
        priority_queue = PriorityQueue()
        for index, node in enumerate(lists):
            priority_queue.put((node.val, index, node))

        while not priority_queue.empty():
            val, index, node = priority_queue.get()

            tail.next = node
            tail = node
            if node.next:
                node = node.next
                priority_queue.put((node.val, index, node))

        return head.next
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    arr = [[1, 4, 5], [1, 3, 4], [2, 6]]
    lists = [ListNode.convert_list(a) for a in arr]
    printList(solution.mergeKLists(lists))
