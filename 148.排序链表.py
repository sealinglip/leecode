#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2020-11-21 09:12:35
LastEditors: Thomas Young
LastEditTime: 2020-11-21 22:42:03
'''
#
# @lc app=leetcode.cn id=148 lang=python3
#
# [148] 排序链表
#
# 给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表。

# 进阶：
# 你可以在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序吗？

# 示例 1：
# 输入：head = [4, 2, 1, 3]
# 输出：[1, 2, 3, 4]

# 示例 2：
# 输入：head = [-1, 5, 3, 4, 0]
# 输出：[-1, 0, 3, 4, 5]

# 示例 3：
# 输入：head = []
# 输出：[]

# 提示：
# 链表中节点的数目在范围[0, 5 * 104] 内
# - 10^5 <= Node.val <= 10^5

from listnode import ListNode, printList
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        def merge(head1: ListNode, head2: ListNode) -> ListNode:
            """归并排序

            Args:
                head1 (ListNode): 列表1头结点
                head2 (ListNode): 列表2头结点

            Returns:
                ListNode: 合并后的列表
            """
            dummy = ListNode(-1)
            tmp, tmp1, tmp2 = dummy, head1, head2
            while tmp1 and tmp2:
                if tmp1.val <= tmp2.val:
                    tmp.next = tmp1
                    tmp1 = tmp1.next
                else:
                    tmp.next = tmp2
                    tmp2 = tmp2.next
                tmp = tmp.next
            if tmp1:
                tmp.next = tmp1
            elif tmp2:
                tmp.next = tmp2
            return dummy.next

        if not head:
            return head

        length = 0
        node = head
        while node:
            length += 1
            node = node.next
        
        dummy = ListNode(-1, head)
        subLength = 1
        while subLength < length:
            prev, curr = dummy, dummy.next
            while curr:
                head1 = curr
                for i in range(1, subLength):
                    if curr.next:
                        curr = curr.next
                    else:
                        break
                head2 = curr.next
                curr.next = None
                curr = head2
                for i in range(1, subLength):
                    if curr and curr.next:
                        curr = curr.next
                    else:
                        break
                
                succ = None # 记录后继结点
                if curr:
                    succ = curr.next
                    curr.next = None

                merged = merge(head1, head2)
                prev.next = merged
                # 将prev指向已经归并排序的最后
                while prev.next: 
                    prev = prev.next

                curr = succ
            subLength <<= 1

        return dummy.next

            
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    head = ListNode.convert_list([4, 2, 1, 3])
    head = solution.sortList(head)
    printList(head)

    head = ListNode.convert_list([-1, 5, 3, 4, 0])
    head = solution.sortList(head)
    printList(head)
