#
# @lc app=leetcode.cn id=863 lang=python3
#
# [863] 二叉树中所有距离为 K 的结点
#
# 给定一个二叉树（具有根结点 root）， 一个目标结点 target ，和一个整数值 K 。
# 返回到目标结点 target 距离为 K 的所有结点的值的列表。 答案可以以任何顺序返回。

# 示例 1：
# 输入：root = [3, 5, 1, 6, 2, 0, 8, null, null, 7, 4], target = 5, K = 2
# 输出：[7, 4, 1]
# 解释：
# 所求结点为与目标结点（值为 5）距离为 2 的结点，
# 值分别为 7，4，以及 1

# 注意，输入的 "root" 和 "target" 实际上是树上的结点。
# 上面的输入仅仅是对这些对象进行了序列化描述。

# 提示：
# 给定的树是非空的。
# 树上的每个结点都具有唯一的值 0 <= node.val <= 500 。
# 目标结点 target 是树上的结点。
# 0 <= K <= 1000.

from typing import List
from treenode import TreeNode
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        cache = {}  # 记录节点的父

        def recordParent(node: TreeNode):
            if node.left:
                cache[node.left.val] = node
                recordParent(node.left)
            if node.right:
                cache[node.right.val] = node
                recordParent(node.right)
        recordParent(root)

        res = []

        def findNode(node: TreeNode, fromNode: TreeNode, step: int):
            if node is None:
                return
            if step == k:
                res.append(node.val)
                return

            if node.left and node.left != fromNode:
                findNode(node.left, node, step + 1)
            if node.right and node.right != fromNode:
                findNode(node.right, node, step + 1)
            if node.val in cache and cache[node.val] != fromNode:
                findNode(cache[node.val], node, step + 1)

        findNode(target, None, 0)
        return res

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    root = TreeNode.createBFSTree(
        [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    target = root.left
    print(solution.distanceK(root, target, 2))
