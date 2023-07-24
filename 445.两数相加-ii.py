#
# @lc app=leetcode.cn id=445 lang=python3
#
# [445] 两数相加 II
#
# 给你两个 非空 链表来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储一位数字。将这两数相加会返回一个新的链表。

# 你可以假设除了数字 0 之外，这两个数字都不会以零开头。


# 示例1：
# 输入：l1 = [7, 2, 4, 3], l2 = [5, 6, 4]
# 输出：[7, 8, 0, 7]

# 示例2：
# 输入：l1 = [2, 4, 3], l2 = [5, 6, 4]
# 输出：[8, 0, 7]

# 示例3：
# 输入：l1 = [0], l2 = [0]
# 输出：[0]


# 提示：
# 链表的长度范围为[1, 100]
# 0 <= node.val <= 9
# 输入数据保证链表代表的数字无前导 0


# 进阶：如果输入链表不能翻转该如何解决？
from listnode import ListNode, printList
from typing import Optional

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def revertList(l: ListNode):
            prev = None
            node = l
            while node:
                tmp = node.next
                node.next = prev
                node, prev = tmp, node
            return prev

        l1 = revertList(l1)
        l2 = revertList(l2)
        res = ListNode(0)  # dummy head
        carry = 0
        node = res
        while l1 and l2:
            s = l1.val + l2.val + carry
            carry, s = divmod(s, 10)
            newNode = ListNode(s)
            node.next = newNode
            node = newNode
            l1 = l1.next
            l2 = l2.next

        rest = l1 or l2
        if rest:
            while rest:
                s = carry + rest.val
                carry, s = divmod(s, 10)
                newNode = ListNode(s)
                node.next = newNode
                node = newNode
                rest = rest.next

        if carry:
            newNode = ListNode(carry)
            node.next = newNode

        return revertList(res.next)


# @lc code=end
if __name__ == "__main__":
    solution = Solution()
    printList(solution.addTwoNumbers(ListNode.convert_list(
        [5]), ListNode.convert_list([9, 9, 9, 5])))  # [1,0,0,0,0]
    printList(solution.addTwoNumbers(ListNode.convert_list(
        [5]), ListNode.convert_list([5])))  # [1, 0]
    printList(solution.addTwoNumbers(ListNode.convert_list(
        [7, 2, 4, 3]), ListNode.convert_list([5, 6, 4])))  # [7,8,0,7]
    printList(solution.addTwoNumbers(ListNode.convert_list(
        [2, 4, 3]), ListNode.convert_list([5, 6, 4])))  # [8,0,7]
    printList(solution.addTwoNumbers(ListNode.convert_list(
        [0]), ListNode.convert_list([0])))  # [0]
