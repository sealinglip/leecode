#
# @lc app=leetcode.cn id=138 lang=python3
#
# [138] 复制带随机指针的链表
#
# 给定一个链表，每个节点包含一个额外增加的随机指针，该指针可以指向链表中的任何节点或空节点。
# 要求返回这个链表的 深拷贝。 
# 我们用一个由 n 个节点组成的链表来表示输入/输出中的链表。每个节点用一个 [val, random_index] 表示：

# val：一个表示 Node.val 的整数。
# random_index：随机指针指向的节点索引（范围从 0 到 n-1）；如果不指向任何节点，则为  null 。
 

# 示例 1：
# 输入：head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
# 输出：[[7,null],[13,0],[11,4],[10,2],[1,0]]

# 示例 2：
# 输入：head = [[1,1],[2,1]]
# 输出：[[1,1],[2,1]]

# 示例 3：
# 输入：head = [[3,null],[3,0],[3,null]]
# 输出：[[3,null],[3,0],[3,null]]

# 示例 4：
# 输入：head = []
# 输出：[]
# 解释：给定的链表为空（空指针），因此返回 null。
 
# 提示：
# -10000 <= Node.val <= 10000
# Node.random 为空（null）或指向链表中的节点。
# 节点数目不超过 1000 。

from typing import List
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return head

        cloneDict = {}
        def getCloneNode(node: 'Node') -> 'Node':
            if node is None:
                return None
            elif node in cloneDict:
                return cloneDict[node]
            else:
                cloneNode = Node(node.val)
                cloneDict[node] = cloneNode
                cloneNode.next = getCloneNode(node.next)
                cloneNode.random = getCloneNode(node.random)
                return cloneNode

        return getCloneNode(head)
        
# @lc code=end

def constructNode(arr: List[List[int]]) -> Node:
    if not arr:
        return None
    
    nodeArr = [Node(a[0]) for a in arr]
    for i, a in enumerate(arr):
        nodeArr[i].next = None if i == len(arr) - 1 else nodeArr[i + 1]
        nodeArr[i].random = None if a[1] is None else nodeArr[a[1]]

    return nodeArr[0]

def printNode(head: None):
    if not head:
        print("None")
    else:
        i = 0
        node = head
        arr = []
        nodeDict = {}
        while node:
            arr.append([node.val, node])
            nodeDict[node] = i
            i += 1
            node = node.next

        for a in arr:
            node = a[1]
            if node.random:
                a[1] = nodeDict[node.random]
            else:
                a[1] = None
        
        print(arr)


if __name__ == "__main__":
    solution = Solution()
    head = constructNode([[3, None], [3, 0], [3, None]])
    printNode(solution.copyRandomList(head))

