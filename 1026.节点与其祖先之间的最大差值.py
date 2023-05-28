#
# @lc app=leetcode.cn id=1026 lang=python3
#
# [1026] 节点与其祖先之间的最大差值
#
# 给定二叉树的根节点 root，找出存在于 不同 节点 A 和 B 之间的最大值 V，其中 V = |A.val - B.val |，且 A 是 B 的祖先。
# （如果 A 的任何子节点之一为 B，或者 A 的任何子节点是 B 的祖先，那么我们认为 A 是 B 的祖先）


# 示例 1：
# 输入：root = [8, 3, 10, 1, 6, null, 14, null, null, 4, 7, 13]
# 输出：7
# 解释：
# 我们有大量的节点与其祖先的差值，其中一些如下：
# |8 - 3 | = 5
# |3 - 7 | = 4
# |8 - 1 | = 7
# |10 - 13 | = 3
# 在所有可能的差值中，最大值 7 由 | 8 - 1 | = 7 得出。

# 示例 2：
# 输入：root = [1, null, 2, null, 0, 3]
# 输出：3


# 提示：
# 树中的节点数在 2 到 5000 之间。
# 0 <= Node.val <= 10^5

from math import inf
from typing import Optional, Tuple
from treenode import TreeNode
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        res = 0

        def traverse(node: TreeNode) -> Tuple[int]:
            '''
            遍历节点，返回最值
            '''
            if not node:
                return None
            mi, ma = inf, -inf
            lm = traverse(node.left)
            if lm:
                mi = min(mi, lm[0])
                ma = max(ma, lm[1])
            rm = traverse(node.right)
            if rm:
                mi = min(mi, rm[0])
                ma = max(ma, rm[1])

            nonlocal res
            if mi != inf:
                res = max(res, abs(node.val - mi))
            if ma != -inf:
                res = max(res, abs(node.val - ma))
            return min(mi, node.val), max(ma, node.val)

        traverse(root)
        return res


        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.maxAncestorDiff(TreeNode.createBFSTree(
        [8, 3, 10, 1, 6, None, 14, None, None, 4, 7, 13])))  # 7
    print(solution.maxAncestorDiff(TreeNode.createBFSTree(
        [1, None, 2, None, 0, 3])))  # 3
