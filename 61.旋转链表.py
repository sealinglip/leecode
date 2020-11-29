#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2020-09-08 22:20:06
LastEditors: Thomas Young
LastEditTime: 2020-09-08 22:47:01
'''
#
# @lc app=leetcode.cn id=61 lang=python3
#
# [61] 旋转链表
#
# 给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。

# 示例 1:
# 输入: 1 -> 2 -> 3 -> 4 -> 5 -> NULL, k = 2
# 输出: 4 -> 5 -> 1 -> 2 -> 3 -> NULL
# 解释:
# 向右旋转 1 步: 5 -> 1 -> 2 -> 3 -> 4 -> NULL
# 向右旋转 2 步: 4 -> 5 -> 1 -> 2 -> 3 -> NULL

# 示例 2:
# 输入: 0 -> 1 -> 2 -> NULL, k = 4
# 输出: 2 -> 0 -> 1 -> NULL
# 解释:
# 向右旋转 1 步: 2 -> 0 -> 1 -> NULL
# 向右旋转 2 步: 1 -> 2 -> 0 -> NULL
# 向右旋转 3 步: 0 -> 1 -> 2 -> NULL
# 向右旋转 4 步: 2 -> 0 -> 1 -> NULL

from listnode import ListNode, printList
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head

        listSize = 1
        mark = head
        p1 = head
        p2 = head
        # p2 先走k步
        while p2.next:
            if listSize == k + 1:
                break
            p2 = p2.next
            listSize += 1
        else: # listSize < k: 走完了整个链表也不够k这个数量
            k = k % listSize # 取余数
            p2 = head
            for _ in range(k):
                p2 = p2.next
        
        while p2.next:
            p2 = p2.next
            p1 = p1.next
        
        p2.next = head
        head = p1.next
        p1.next = None
        return head

# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    printList(solution.rotateRight(
        ListNode.convert_list([i for i in range(1, 6)]), 2))
    printList(solution.rotateRight(
        ListNode.convert_list([i for i in range(3)]), 4))
    printList(solution.rotateRight(
        ListNode.convert_list([i for i in range(3)]), 7))
