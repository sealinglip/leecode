#
# @lc app=leetcode.cn id=558 lang=python3
#
# [558] 四叉树交集
#
# 给你两个四叉树，quadTree1 和 quadTree2。其中 quadTree1 表示一个 n * n 二进制矩阵，而 quadTree2 表示另一个 n * n 二进制矩阵。

# 请你返回一个表示 n * n 二进制矩阵的四叉树，它是 quadTree1 和 quadTree2 所表示的两个二进制矩阵进行 按位逻辑或运算 的结果。

# 注意，当 isLeaf 为 False 时，你可以把 True 或者 False 赋值给节点，两种值都会被判题机制 接受 。

# 四叉树数据结构中，每个内部节点只有四个子节点。此外，每个节点都有两个属性：

# val：储存叶子结点所代表的区域的值。1 对应 True，0 对应 False；
# isLeaf: 当这个节点是一个叶子结点时为 True，如果它有 4 个子节点则为 False 。
# class Node {
#     public boolean val;
#     public boolean isLeaf;
#     public Node topLeft;
#     public Node topRight;
#     public Node bottomLeft;
#     public Node bottomRight;
# }
# 我们可以按以下步骤为二维区域构建四叉树：

# 如果当前网格的值相同（即，全为 0 或者全为 1），将 isLeaf 设为 True ，将 val 设为网格相应的值，并将四个子节点都设为 Null 然后停止。
# 如果当前网格的值不同，将 isLeaf 设为 False， 将 val 设为任意值，然后如下图所示，将当前网格划分为四个子网格。
# 使用适当的子网格递归每个子节点。


# 如果你想了解更多关于四叉树的内容，可以参考 wiki 。

# 四叉树格式：

# 输出为使用层序遍历后四叉树的序列化形式，其中 null 表示路径终止符，其下面不存在节点。

# 它与二叉树的序列化非常相似。唯一的区别是节点以列表形式表示 [isLeaf, val] 。

# 如果 isLeaf 或者 val 的值为 True ，则表示它在列表 [isLeaf, val] 中的值为 1 ；如果 isLeaf 或者 val 的值为 False ，则表示值为 0 。


# 示例 1：
# 输入：quadTree1 = [[0,1],[1,1],[1,1],[1,0],[1,0]]
# , quadTree2 = [[0,1],[1,1],[0,1],[1,1],[1,0],null,null,null,null,[1,0],[1,0],[1,1],[1,1]]
# 输出：[[0,0],[1,1],[1,1],[1,1],[1,0]]
# 解释：quadTree1 和 quadTree2 如上所示。由四叉树所表示的二进制矩阵也已经给出。
# 如果我们对这两个矩阵进行按位逻辑或运算，则可以得到下面的二进制矩阵，由一个作为结果的四叉树表示。
# 注意，我们展示的二进制矩阵仅仅是为了更好地说明题意，你无需构造二进制矩阵来获得结果四叉树。

# 示例 2：
# 输入：quadTree1 = [[1,0]]
# , quadTree2 = [[1,0]]
# 输出：[[1,0]]
# 解释：两个数所表示的矩阵大小都为 1*1，值全为 0
# 结果矩阵大小为 1*1，值全为 0 。

# 示例 3：
# 输入：quadTree1 = [[0,0],[1,0],[1,0],[1,1],[1,1]]
# , quadTree2 = [[0,0],[1,1],[1,1],[1,0],[1,1]]
# 输出：[[1,1]]

# 示例 4：
# 输入：quadTree1 = [[0,0],[1,1],[1,0],[1,1],[1,1]]
# , quadTree2 = [[0,0],[1,1],[0,1],[1,1],[1,1],null,null,null,null,[1,1],[1,0],[1,0],[1,1]]
# 输出：[[0,0],[1,1],[0,1],[1,1],[1,1],null,null,null,null,[1,1],[1,0],[1,0],[1,1]]

# 示例 5：
# 输入：quadTree1 = [[0,1],[1,0],[0,1],[1,1],[1,0],null,null,null,null,[1,0],[1,0],[1,1],[1,1]]
# , quadTree2 = [[0,1],[0,1],[1,0],[1,1],[1,0],[1,0],[1,0],[1,1],[1,1]]
# 输出：[[0,0],[0,1],[0,1],[1,1],[1,0],[1,0],[1,0],[1,1],[1,1],[1,0],[1,0],[1,1],[1,1]]


# 提示：
# quadTree1 和 quadTree2 都是符合题目要求的四叉树，每个都代表一个 n * n 的矩阵。
# n == 2^x ，其中 0 <= x <= 9.

from typing import List


class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


def buildQuadTree(data: List[List[int]]) -> Node:
    if not data:
        return None
    nodeList = [Node(d[1], d[0], None, None, None, None) if d else None
                for d in data]

    # 按层构建
    depth = [nodeList[0]]
    i = 1
    l = len(nodeList)
    while depth and i < l:
        newDepth = []
        for node in depth:
            if node.isLeaf:
                i += 4  # 跳过
            else:
                topLeft = nodeList[i]
                if topLeft:
                    node.topLeft = topLeft
                    newDepth.append(topLeft)
                i += 1
                if i >= l:
                    break

                topRight = nodeList[i]
                if topRight:
                    node.topRight = topRight
                    newDepth.append(topRight)
                i += 1
                if i >= l:
                    break

                bottomLeft = nodeList[i]
                if bottomLeft:
                    node.bottomLeft = bottomLeft
                    newDepth.append(bottomLeft)
                i += 1
                if i >= l:
                    break

                bottomRight = nodeList[i]
                if bottomRight:
                    node.bottomRight = bottomRight
                    newDepth.append(bottomRight)
                i += 1

            if i >= l:
                break

        depth = newDepth

    return nodeList[0]


def printQuadTree(node: 'Node') -> None:
    nodeList = []
    if node:
        depth = [node]
        while depth:
            newDepth = []
            lastNotLeaf = max([i for i, n in enumerate(
                depth) if n and (not n.isLeaf)], default=-1)
            for i, n in enumerate(depth):
                if n is None:
                    nodeList.append(None)
                    continue

                nodeList.append([n.isLeaf, n.val])
                if n.isLeaf:
                    if i < lastNotLeaf:
                        newDepth.append(None)
                        newDepth.append(None)
                        newDepth.append(None)
                        newDepth.append(None)
                else:
                    newDepth.append(n.topLeft)
                    newDepth.append(n.topRight)
                    newDepth.append(n.bottomLeft)
                    newDepth.append(n.bottomRight)

            depth = newDepth

    print(nodeList)


# @lc code=start
"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""


class Solution:
    def intersect(self, quadTree1: 'Node', quadTree2: 'Node') -> 'Node':
        if quadTree1 is None or quadTree2 is None:
            return quadTree1 or quadTree2

        if quadTree1.isLeaf and quadTree2.isLeaf:
            # 都是叶子节点
            return Node(quadTree1.val | quadTree2.val, 1, None, None, None, None)
        if not quadTree1.isLeaf and not quadTree2.isLeaf:
            # 都是非叶子节点
            topLeft = self.intersect(quadTree1.topLeft, quadTree2.topLeft)
            topRight = self.intersect(quadTree1.topRight, quadTree2.topRight)
            bottomLeft = self.intersect(
                quadTree1.bottomLeft, quadTree2.bottomLeft)
            bottomRight = self.intersect(
                quadTree1.bottomRight, quadTree2.bottomRight)
            if topLeft.isLeaf and topRight.isLeaf and bottomLeft.isLeaf and bottomRight.isLeaf and topLeft.val == topRight.val and topLeft.val == bottomLeft.val and topLeft.val == bottomRight.val:
                # 四个分区可以合并的情况
                return topLeft
            else:
                return Node(1, 0, topLeft, topRight, bottomLeft, bottomRight)
        # 有一个是叶子节点
        if quadTree2.isLeaf:
            # 把叶子节点放前面
            quadTree1, quadTree2 = quadTree2, quadTree1
        return quadTree1 if quadTree1.val else quadTree2

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    printQuadTree(solution.intersect(buildQuadTree(
        [[0, 1], [1, 1], [1, 1], [1, 0], [1, 0]]), buildQuadTree([[0, 1], [1, 1], [0, 1], [1, 1], [1, 0], None, None, None, None, [1, 0], [1, 0], [1, 1], [1, 1]])))  # [[0, 1], [1, 1], [1, 1], [1, 1], [1, 0]]
    printQuadTree(solution.intersect(buildQuadTree(
        [[1, 0]]), buildQuadTree([[1, 0]])))  # [[1, 0]]
    printQuadTree(solution.intersect(buildQuadTree(
        [[0, 0], [1, 0], [1, 0], [1, 1], [1, 1]]), buildQuadTree([[0, 0], [1, 1], [1, 1], [1, 0], [1, 1]])))  # [[1, 1]]
    printQuadTree(solution.intersect(buildQuadTree(
        [[0, 0], [1, 1], [1, 0], [1, 1], [1, 1]]), buildQuadTree([[0, 0], [1, 1], [0, 1], [1, 1], [1, 1], None, None, None, None, [1, 1], [1, 0], [1, 0], [1, 1]])))  # [[0, 1], [1, 1], [0, 1], [1, 1], [1, 1], None, None, None, None, [1, 1], [1, 0], [1, 0], [1, 1]]
    printQuadTree(solution.intersect(buildQuadTree(
        [[0, 1], [1, 0], [0, 1], [1, 1], [1, 0], None, None, None, None, [1, 0], [1, 0], [1, 1], [1, 1]]), buildQuadTree([[0, 1], [0, 1], [1, 0], [1, 1], [1, 0], [1, 0], [1, 0], [1, 1], [1, 1]])))  # [[0, 1], [0, 1], [0, 1], [1, 1], [1, 0], [1, 0], [1, 0], [1, 1], [1, 1], [1, 0], [1, 0], [1, 1], [1, 1]]
