#
# @lc app=leetcode.cn id=872 lang=python3
#
# [872] 叶子相似的树
#
# 请考虑一棵二叉树上所有的叶子，这些叶子的值按从左到右的顺序排列形成一个 叶值序列 。
# 举个例子，如上图所示，给定一棵叶值序列为(6, 7, 4, 9, 8) 的树。
# 如果有两棵二叉树的叶值序列是相同，那么我们就认为它们是 叶相似 的。
# 如果给定的两个根结点分别为 root1 和 root2 的树是叶相似的，则返回 true；否则返回 false 。

# 示例 1：
# 输入：root1 = [3, 5, 1, 6, 2, 9, 8, null, null, 7, 4], root2 = [3, 5, 1, 6, 7, 4, 2, null, null, null, null, null, null, 9, 8]
# 输出：true

# 示例 2：
# 输入：root1 = [1], root2 = [1]
# 输出：true

# 示例 3：
# 输入：root1 = [1], root2 = [2]
# 输出：false

# 示例 4：
# 输入：root1 = [1, 2], root2 = [2, 2]
# 输出：true

# 示例 5：
# 输入：root1 = [1, 2, 3], root2 = [1, 3, 2]
# 输出：false

# 提示：
# 给定的两棵树可能会有 1 到 200 个结点。
# 给定的两棵树上的值介于 0 到 200 之间。

from typing import List
from treenode import TreeNode
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def leaf(r: TreeNode) -> List:
            l = []
            q = [r]
            while q:
                n = q.pop()
                if n.left is None and n.right is None:
                    l.append(n.val)
                else:
                    if n.right:
                        q.append(n.right)
                    if n.left:
                        q.append(n.left)

            return l

        leaf1 = leaf(root1)
        leaf2 = leaf(root2)
        return leaf1 == leaf2


        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.leafSimilar(TreeNode.createBFSTree(
        [3, 5, 1, 6, 7, 4, 2, None, None, None, None, None, None, 9, 11, None, None, 8, 10]), TreeNode.createBFSTree([3, 5, 1, 6, 2, 9, 8, None, None, 7, 4])))
    print(solution.leafSimilar(TreeNode.createBFSTree(
        [3, 5, 1, 6, 2, 9, 8, None, None, 7, 4]), TreeNode.createBFSTree([3, 5, 1, 6, 7, 4, 2, None, None, None, None, None, None, 9, 8])))
    print(solution.leafSimilar(TreeNode.createBFSTree(
        [1]), TreeNode.createBFSTree([1])))
    print(solution.leafSimilar(TreeNode.createBFSTree(
        [1]), TreeNode.createBFSTree([2])))
    print(solution.leafSimilar(TreeNode.createBFSTree(
        [1, 2]), TreeNode.createBFSTree([2, 2])))
    print(solution.leafSimilar(TreeNode.createBFSTree(
        [1, 2, 3]), TreeNode.createBFSTree([1, 3, 2])))
