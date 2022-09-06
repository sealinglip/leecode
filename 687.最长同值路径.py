#
# @lc app=leetcode.cn id=687 lang=python3
#
# [687] 最长同值路径
#
# 给定一个二叉树的 root ，返回 最长的路径的长度 ，这个路径中的 每个节点具有相同值 。 这条路径可以经过也可以不经过根节点。

# 两个节点之间的路径长度 由它们之间的边数表示。


# 示例 1:
# 输入：root = [5, 4, 5, 1, 1, 5]
# 输出：2

# 示例 2:
# 输入：root = [1, 4, 5, 4, 4, 5]
# 输出：2


# 提示:
# 树的节点数的范围是[0, 10^4]
# -1000 <= Node.val <= 1000
# 树的深度将不超过 1000

from typing import Optional
from treenode import TreeNode
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        res = 0
        if root is None:
            return res

        # 没仔细看，理解错题意了
        # stack = [(root, 0)]
        # while stack:
        #     node, edges = stack.pop()
        #     res = max(res, edges)
        #     if node.left:
        #         stack.append(
        #             (node.left, edges + 1 if node.left.val == node.val else 0))
        #     if node.right:
        #         stack.append(
        #             (node.right, edges + 1 if node.right.val == node.val else 0))

        # return res
        def traverse(node: TreeNode) -> int:
            nonlocal res
            edges = paths = 0
            if node.left:
                left = traverse(node.left)
                if node.left.val == node.val:
                    edges = left + 1
                    paths += left + 1
            if node.right:
                right = traverse(node.right)
                if node.right.val == node.val:
                    paths += right + 1
                    edges = max(edges, right + 1)
            res = max(res, paths)
            return edges

        traverse(root)

        return res

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.longestUnivaluePath(
        TreeNode.createBFSTree([5, 4, 5, 1, 1, 5])))
    print(solution.longestUnivaluePath(
        TreeNode.createBFSTree([1, 4, 5, 4, 4, None, 5])))
