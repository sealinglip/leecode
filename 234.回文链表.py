#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2020-10-23 13:43:30
LastEditors: Thomas Young
LastEditTime: 2020-10-23 14:17:46
'''
#
# @lc app=leetcode.cn id=234 lang=python3
#
# [234] 回文链表
#
# 请判断一个链表是否为回文链表。

# 示例 1:
# 输入: 1 -> 2
# 输出: false

# 示例 2:
# 输入: 1 -> 2 -> 2 -> 1
# 输出: true
# 进阶：
# 你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？

from listnode import ListNode, printList
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        
        slow = fast = head
        while fast:
            fast = fast.next
            if fast:
                fast = fast.next
                slow = slow.next

        def reverseList(node: ListNode) -> ListNode:
            h, prev = node, None
            while node:
                h = node
                next = node.next
                node.next = prev
                prev = h
                node = next
            return h

        # 此时slow指向了链表的中间
        # 翻转slow后面的链表
        head2 = reverseList(slow)

        # 判断head和head2是否一致
        match = head2 is not None
        p, p2 = head, head2
        while match and p2:
            if p.val == p2.val:
                p = p.next
                p2 = p2.next
            else:
                match = False

        # 翻转
        reverseList(head2)

        return match
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.isPalindrome(ListNode.convert_list([1, 2])))
    print(solution.isPalindrome(ListNode.convert_list([1, 2, 2, 1])))
    print(solution.isPalindrome(ListNode.convert_list([1, 2, 3, 2, 1])))
    print(solution.isPalindrome(ListNode.convert_list([1, 2, 3, 4, 2, 1])))
