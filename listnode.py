#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@Description: file content
@Author: Thomas Young
@Date: 2020-07-02 17:09:01
LastEditors: Thomas Young
LastEditTime: 2020-11-21 22:23:47
'''

from typing import List


class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

    @classmethod
    def convert_list(cls, nums: List[int]) -> 'ListNode':
        if not nums:
            return None
        head = cls(-1)
        tail = head
        for num in nums:
            node = cls(num)
            tail.next = node
            tail = node
        return head.next


def printList(node: ListNode, end='\n'):
    print('[', end='')
    while node:
        print(node.val, end=' ')
        node = node.next
    print(']', end=end)
