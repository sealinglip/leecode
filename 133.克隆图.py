#
# @lc app=leetcode.cn id=133 lang=python3
#
# [133] 克隆图
#
# 给你无向 连通 图中一个节点的引用，请你返回该图的 深拷贝（克隆）。

# 图中的每个节点都包含它的值 val（int） 和其邻居的列表（list[Node]）。

# class Node {
#     public int val;
#     public List<Node> neighbors;
# }

# 测试用例格式：
# 简单起见，每个节点的值都和它的索引相同。例如，第一个节点值为 1（val = 1），第二个节点值为 2（val = 2），以此类推。该图在测试用例中使用邻接列表表示。
# 邻接列表 是用于表示有限图的无序列表的集合。每个列表都描述了图中节点的邻居集。
# 给定节点将始终是图中的第一个节点（值为 1）。你必须将 给定节点的拷贝 作为对克隆图的引用返回。

# 提示：
# 节点数不超过 100 。
# 每个节点值 Node.val 都是唯一的，1 <= Node.val <= 100。
# 无向图是一个简单图，这意味着图中没有重复的边，也没有自环。
# 由于图是无向的，如果节点 p 是节点 q 的邻居，那么节点 q 也必须是节点 p 的邻居。
# 图是连通图，你可以从给定节点访问到所有节点。

from typing import List

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        
        cloneCache = dict()
        stack = deque([node])
        cloneNode = Node(node.val)
        cloneCache[node.val] = cloneNode
        while stack:
            n = stack.popleft()
            cp = cloneCache[n.val]
            if n.neighbors:
                cp.neighbors = []
                for nb in n.neighbors:
                    if nb.val not in cloneCache:
                        stack.append(nb)
                        cloneCache[nb.val] = Node(nb.val)
                    cp.neighbors.append(cloneCache[nb.val])

        return cloneNode
            

# @lc code=end

def constructNodeGraph(adjList: List[List[int]]) -> 'Node':
    if not adjList:
        return Node

    cache = dict()
    def getNode(val: int) -> 'Node':
        if val in cache:
            return cache[val]
        else:
            node = Node(val)
            cache[val] = node
            return node

    for idx, adj in enumerate(adjList):
        val = idx + 1
        node = getNode(val)
        if adj:
            node.neighbors = []
            for a in adj:
                n = getNode(a)
                node.neighbors.append(n)

    return getNode(1)

def printNodeGraph(node: 'Node'):
    stack = [node]
    printed = set()
    while stack:
        n = stack.pop()
        if n.val not in printed:
            if n.neighbors:
                for nb in n.neighbors:
                    stack.append(nb)
            printed.add(n.val)
            print("""Node: 
            \tval:%d
            \taj:%s""" % (n.val, "Empty" if not n.neighbors else ",".join([str(nb.val) for nb in n.neighbors])))

if __name__ == "__main__":
    solution = Solution()
    origin = constructNodeGraph([[2,4],[1,3],[2,4],[1,3]])
    print("****** Origin ******")
    printNodeGraph(origin)
    node = solution.cloneGraph(origin)
    print()
    print("****** Clone ******")
    printNodeGraph(node)
    

