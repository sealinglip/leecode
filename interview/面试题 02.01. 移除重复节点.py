#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@Description: file content
@Author: Thomas Young
@Date: 2020-06-26 10:01:12
@LastEditors: Thomas Young
@LastEditTime: 2020-07-02 21:50:10
'''
from typing import List
import os
import sys
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
from listnode import ListNode, printList
# Definition for singly-linked list.

class Solution:
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        cache = set()
        dummy = ListNode(-1)
        dummy.next = head
        prev, node = dummy, head
        while node:
            if node.val in cache:
                node = node.next
                prev.next = node
            else:
                cache.add(node.val)
                prev = node
                node = node.next
        return dummy.next

if __name__ == "__main__":
    solution = Solution()
    printList(solution.removeDuplicateNodes(
        ListNode.convert_list([1, 2, 3, 3, 2, 1])))
    printList(solution.removeDuplicateNodes(
        ListNode.convert_list([1, 1, 1, 1, 2])))

