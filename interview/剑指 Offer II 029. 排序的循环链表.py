# 剑指 Offer II 029 排序的循环链表

# 给定循环单调非递减列表中的一个点，写一个函数向这个列表中插入一个新元素 insertVal ，使这个列表仍然是循环升序的。

# 给定的可以是这个列表中任意一个顶点的指针，并不一定是这个列表中最小元素的指针。

# 如果有多个满足条件的插入位置，可以选择任意一个位置插入新的值，插入后整个列表仍然保持有序。

# 如果列表为空（给定的节点是 null），需要创建一个循环有序列表并返回这个节点。否则。请返回原先给定的节点。

#  

# 示例 1：
# 输入：head = [3, 4, 1], insertVal = 2
# 输出：[3, 4, 1, 2]
# 解释：在上图中，有一个包含三个元素的循环有序列表，你获得值为 3 的节点的指针，我们需要向表中插入元素 2 。新插入的节点应该在 1 和 3 之间，插入之后，整个列表如上图所示，最后返回节点 3 。


# 示例 2：
# 输入：head = [], insertVal = 1
# 输出：[1]
# 解释：列表为空（给定的节点是 null），创建一个循环有序列表并返回这个节点。

# 示例 3：
# 输入：head = [1], insertVal = 0
# 输出：[1, 0]
#  

# 提示：
# 0 <= Number of Nodes <= 5 * 10 ^ 4
# -10 ^ 6 <= Node.val <= 10 ^ 6
# -10 ^ 6 <= insertVal <= 10 ^ 6

from typing import List
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""


class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        if head is None:
            node = Node(insertVal)
            node.next = node
            return node
        # 待插入值有三种情况：比最小值小，比最大值大，其他
        prev, node = head, head.next
        while node != head:
            if (prev.val <= insertVal <= node.val) or ((prev.val > node.val or prev == node) and (insertVal >= prev.val or insertVal <= node.val)):
                insertNode = Node(insertVal, node)
                prev.next = insertNode
                break
            prev, node = node, node.next
        else:
            insertNode = Node(insertVal, node)
            prev.next = insertNode

        return head


def generateList(nums: List[int]) -> 'Node':
    if not nums:
        return None
    head = Node(-1)
    tail = head
    for num in nums:
        node = Node(num)
        tail.next = node
        tail = node
    tail.next = head.next
    return head.next


def printList(node: 'Node', end='\n'):
    print('[', end='')
    head = node
    while node:
        print(node.val, end=' ')
        node = node.next
        if node == head:
            break
    print(']', end=end)


if __name__ == "__main__":
    solution = Solution()
    printList(solution.insert(None, 1))

    head = generateList([1])
    printList(solution.insert(head, 0))

    head = generateList([3, 3, 3])
    printList(solution.insert(head, 0))
