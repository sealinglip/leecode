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

    def __str__(self):
        return f'ListNode({self.val})'
    
    def __repr__(self):
        return self.__str__()

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


def printList(node: ListNode, sep=',', end='\n'):
    print('[', end='')
    visited = set()
    while node:
        if node in visited:
            break
        print(node.val, end=(sep if node.next else ''))
        visited.add(node)
        node = node.next
    print(']', end=end)
