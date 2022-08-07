#
# @lc app=leetcode.cn id=1161 lang=python3
#
# [1161] 最大层内元素和
#
# 给你一个二叉树的根节点 root。设根节点位于二叉树的第 1 层，而根节点的子节点位于第 2 层，依此类推。

# 请返回层内元素之和 最大 的那几层（可能只有一层）的层号，并返回其中 最小 的那个。


# 示例 1：
# 输入：root = [1, 7, 0, 7, -8, null, null]
# 输出：2
# 解释：
# 第 1 层各元素之和为 1，
# 第 2 层各元素之和为 7 + 0 = 7，
# 第 3 层各元素之和为 7 + -8 = -1，
# 所以我们返回第 2 层的层号，它的层内元素之和最大。

# 示例 2：
# 输入：root = [989, null, 10250, 98693, -89388, null, null, null, -32127]
# 输出：2


# 提示：
# 树中的节点数在[1, 10^4]范围内
# -10^5 <= Node.val <= 10^5


from cmath import inf
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
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return -1
        nodes = [root]
        lvl = 1
        maxLevelSum = -inf
        res = -1
        while nodes:
            levelSum = sum([n.val for n in nodes])
            if levelSum > maxLevelSum:
                maxLevelSum = levelSum
                res = lvl
            newNodes = []
            for n in nodes:
                if n.left:
                    newNodes.append(n.left)
                if n.right:
                    newNodes.append(n.right)
            nodes = newNodes
            lvl += 1

        return res

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.maxLevelSum(
        TreeNode.createBFSTree([-100, -200, -300, -20, -5, -10])))  # 3
    print(solution.maxLevelSum(
        TreeNode.createBFSTree([1, 7, 0, 7, -8])))  # 2
    print(solution.maxLevelSum(
        TreeNode.createBFSTree([989, None, 10250, 98693, -89388, None, None, None, -32127])))  # 2
