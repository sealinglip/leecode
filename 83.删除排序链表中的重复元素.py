#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2020-09-03 08:49:07
LastEditors: Thomas Young
LastEditTime: 2020-09-03 08:57:05
'''
#
# @lc app=leetcode.cn id=83 lang=python3
#
# [83] 删除排序链表中的重复元素
#
# 给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。

# 示例 1:
# 输入: 1 -> 1 -> 2
# 输出: 1 -> 2

# 示例 2:
# 输入: 1 -> 1 -> 2 -> 3 -> 3
# 输出: 1 -> 2 -> 3

from listnode import ListNode, printList
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
            
        prev, next = head, head.next
        while next:
            if next.val == prev.val: # 重复
                next = next.next
                prev.next = next
            else:
                prev = next
                next = next.next

        return head
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    node = ListNode.convert_list([1, 1, 2])
    solution.deleteDuplicates(node)
    printList(node)
    node = ListNode.convert_list([1, 1, 2, 3, 3])
    solution.deleteDuplicates(node)
    printList(node)
    
