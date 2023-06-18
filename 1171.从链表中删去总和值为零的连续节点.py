#
# @lc app=leetcode.cn id=1171 lang=python3
#
# [1171] 从链表中删去总和值为零的连续节点
#
# 给你一个链表的头节点 head，请你编写代码，反复删去链表中由 总和 值为 0 的连续节点组成的序列，直到不存在这样的序列为止。
# 删除完毕后，请你返回最终结果链表的头节点。


# 你可以返回任何满足题目要求的答案。
# （注意，下面示例中的所有序列，都是对 ListNode 对象序列化的表示。）

# 示例 1：
# 输入：head = [1, 2, -3, 3, 1]
# 输出：[3, 1]
# 提示：答案[1, 2, 1] 也是正确的。

# 示例 2：
# 输入：head = [1, 2, 3, -3, 4]
# 输出：[1, 2, 4]

# 示例 3：
# 输入：head = [1, 2, 3, -3, -2]
# 输出：[1]


# 提示：
# 给你的链表中可能有 1 到 1000 个节点。
# 对于链表中的每个节点，节点的值：- 1000 <= node.val <= 1000.

from collections import defaultdict
from typing import Optional
from listnode import ListNode, printList
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodeMap = defaultdict(list)
        dummy = ListNode(0, head)
        nodeMap[0].append(dummy)
        accum = 0

        def removeNode(fromNode: ListNode, toNode: ListNode, total: int) -> None:
            '''
            fromNode(不含)：删除的起点
            toNode(含)：删除的终点
            total：累积
            '''
            node = fromNode.next
            while node != toNode:
                total += node.val
                nodeMap[total].remove(node)
                node = node.next

            fromNode.next = toNode.next

        node = head
        while node:
            accum += node.val
            if nodeMap[accum]:
                prev = nodeMap[accum][-1]
                removeNode(prev, node, accum)
            else:
                nodeMap[accum].append(node)
            node = node.next

        return dummy.next
# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    printList(solution.removeZeroSumSublists(
        ListNode.convert_list([1, 2, -3, 3, 1])))  # [3,1]
    printList(solution.removeZeroSumSublists(
        ListNode.convert_list([1, 2, 3, -3, 4])))  # [1,2,4]
    printList(solution.removeZeroSumSublists(
        ListNode.convert_list([1, 2, 3, -3, -2])))  # [1]
