#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@Description: file content
@Author: Thomas Young
@Date: 2020-06-20 14:25:26
@LastEditors: Thomas Young
@LastEditTime: 2020-07-02 17:20:05
'''
#
# @lc app=leetcode.cn id=25 lang=python3
#
# [25] K 个一组翻转链表
#
from typing import List
from listnode import ListNode

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head or k == 1:
            return head

        dummy = ListNode(-1)
        dummy.next = head
        l, r = dummy, dummy
        step = 0
        while r:
            r = r.next
            if r:
                step += 1
            if step == k:
                step = 0
                # 翻转 l 和r 之间的所有节点
                tmp = l.next
                prev = r.next
                while True:
                    next = tmp.next
                    tmp.next = prev
                    prev = tmp
                    if tmp == r:
                        break
                    tmp = next
                tmp = l.next
                l.next = r
                l, r = tmp, tmp

        return dummy.next

# @lc code=end
def print_node(node: ListNode):
    list = []
    while node:
        list.append(node.val)
        node = node.next
    print(list)

if __name__ == "__main__":
    solution = Solution()
    print_node(solution.reverseKGroup(ListNode.convert_list([1, 2, 3, 4, 5]), 2))
    
