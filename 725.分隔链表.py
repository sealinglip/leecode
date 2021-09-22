#
# @lc app=leetcode.cn id=725 lang=python3
#
# [725] 分隔链表
#
# 给你一个头结点为 head 的单链表和一个整数 k ，请你设计一个算法将链表分隔为 k 个连续的部分。
# 每部分的长度应该尽可能的相等：任意两部分的长度差距不能超过 1 。这可能会导致有些部分为 null 。
# 这 k 个部分应该按照在链表中出现的顺序排列，并且排在前面的部分的长度应该大于或等于排在后面的长度。
# 返回一个由上述 k 部分组成的数组。


# 示例 1：
# 输入：head = [1, 2, 3], k = 5
# 输出：[[1], [2], [3], [], []]
# 解释：
# 第一个元素 output[0] 为 output[0].val = 1 ，output[0].next = null 。
# 最后一个元素 output[4] 为 null ，但它作为 ListNode 的字符串表示是[] 。

# 示例 2：
# 输入：head = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k = 3
# 输出：[[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]
# 解释：
# 输入被分成了几个连续的部分，并且每部分的长度相差不超过 1 。前面部分的长度大于等于后面部分的长度。


# 提示：
# 链表中节点的数目在范围[0, 1000]
# 0 <= Node.val <= 1000
# 1 <= k <= 50

from typing import List
from listnode import ListNode, printList
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def splitListToParts(self, head: ListNode, k: int) -> List[ListNode]:
        # 方法1：
        # dummy = ListNode(-1, head)
        # res = [dummy] * (k + 1)
        # while True:
        #     # 先移某尾，看能移多少次
        #     lastStep = k
        #     node = res[k]
        #     while node and lastStep > 0:
        #         node = node.next
        #         lastStep -= 1
        #     res[k] = node
        #     if node is None:
        #         lastStep += 1
        #     for i in range(1, k):
        #         # 按i走步数
        #         node = res[i]
        #         step = min(i, k - lastStep)
        #         while node and step > 0:
        #             node = node.next
        #             step -= 1
        #         res[i] = node
        #     if res[-1] is None:
        #         break

        # for i in range(k):
        #     node = res[i]
        #     if node:
        #         res[i] = node.next
        #         node.next = None

        # return res[:k]

        # 方法2：
        # 先求链表长度
        node = head
        length = 0
        while node:
            length += 1
            node = node.next

        avgSize = length // k
        remainder = length % k
        # 前remainder个子链表的长度是avgSize + 1，其他是avgSize
        res = [None] * k
        node = head
        for i in range(k):
            res[i] = node
            subSize = avgSize + (1 if i < remainder else 0)
            if subSize == 0:
                break
            for _ in range(subSize - 1):
                node = node.next
            n = node.next
            node.next = None
            node = n
        return res

        # @lc code=end


def printResult(res: List[ListNode]) -> None:
    print('[', end='')
    for i, ln in enumerate(res):
        if i > 0:
            print(", ", end='')
        printList(ln, end='')
    print(']')


if __name__ == "__main__":
    solution = Solution()
    # [[1], [2], [3], [], []]
    printResult(solution.splitListToParts(ListNode.convert_list([1, 2, 3]), 5))
    # [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]
    printResult(solution.splitListToParts(
        ListNode.convert_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 3))
    # [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11]]
    printResult(solution.splitListToParts(
        ListNode.convert_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]), 3))
    # [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    printResult(solution.splitListToParts(
        ListNode.convert_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]), 3))
