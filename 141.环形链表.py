#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2020-10-03 22:57:17
LastEditors: Thomas Young
LastEditTime: 2020-10-03 23:01:01
'''
#
# @lc app=leetcode.cn id=141 lang=python3
#
# [141] 环形链表
#
# 给定一个链表，判断链表中是否有环。

# 如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。
# 为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。
# 如果 pos 是 - 1，则在该链表中没有环。注意：pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。
# 如果链表中存在环，则返回 true 。 否则，返回 false 。

# 进阶：
# 你能用 O(1)（即，常量）内存解决此问题吗？

from listnode import ListNode
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head:
            slow, fast = head, head
            while slow and fast:
                slow = slow.next  # 一次走一步
                fast = fast.next
                if fast:
                    fast = fast.next  # 一次走两步
                else:
                    return False
                if fast == slow:
                    return True

        return False

# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    head = ListNode.convert_list([3, 2, 0, -4])
    head.next.next.next.next = head.next
    print(solution.hasCycle(head))

    head = ListNode.convert_list([1, 2])
    head.next.next = head
    print(solution.hasCycle(head))
