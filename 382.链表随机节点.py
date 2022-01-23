#
# @lc app=leetcode.cn id=382 lang=python3
#
# [382] 链表随机节点
#

from random import choice
from listnode import ListNode
from typing import Optional
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.arr = []
        while head:
            self.arr.append(head.val)
            head = head.next

    def getRandom(self) -> int:
        return choice(self.arr)


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
# @lc code=end

if __name__ == "__main__":
    head = ListNode.convert_list([1, 2, 3])
    solution = Solution(head)
    print(solution.getRandom())
    print(solution.getRandom())
    print(solution.getRandom())
    print(solution.getRandom())
