#
# @lc app=leetcode.cn id=817 lang=python3
#
# [817] 链表组件
#
# 给定链表头结点 head，该链表上的每个结点都有一个 唯一的整型值 。同时给定列表 nums，该列表是上述链表中整型值的一个子集。

# 返回列表 nums 中组件的个数，这里对组件的定义为：链表中一段最长连续结点的值（该值必须在列表 nums 中）构成的集合。


# 示例 1：
# 输入: head = [0, 1, 2, 3], nums = [0, 1, 3]
# 输出: 2
# 解释: 链表中, 0 和 1 是相连接的，且 nums 中不包含 2，所以[0, 1] 是 nums 的一个组件，同理[3] 也是一个组件，故返回 2。

# 示例 2：
# 输入: head = [0, 1, 2, 3, 4], nums = [0, 3, 1, 4]
# 输出: 2
# 解释: 链表中，0 和 1 是相连接的，3 和 4 是相连接的，所以[0, 1] 和[3, 4] 是两个组件，故返回 2。


# 提示：
# 链表中节点数为n
# 1 <= n <= 10^4
# 0 <= Node.val < n
# Node.val 中所有值 不同
# 1 <= nums.length <= n
# 0 <= nums[i] < n
# nums 中所有值 不同


from typing import List, Optional
from listnode import ListNode

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        numsSet = set(nums)
        cnt = 0
        node = head
        state = False
        while node:
            if node.val in numsSet:
                if not state:
                    cnt += 1
                    state = True
            else:
                state = False
            node = node.next

        return cnt


        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.numComponents(
        ListNode.convert_list([0, 1, 2, 3]), [0, 1, 3]))  # 2
    print(solution.numComponents(
        ListNode.convert_list([0, 1, 2, 3, 4]), [0, 3, 1, 4]))  # 2
