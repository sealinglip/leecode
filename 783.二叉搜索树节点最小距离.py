#
# @lc app=leetcode.cn id=783 lang=python3
#
# [783] 二叉搜索树节点最小距离
#
# 给你一个二叉搜索树的根节点 root ，返回 树中任意两不同节点值之间的最小差值 。
# 注意：本题与 530：https: // leetcode-cn.com/problems/minimum-absolute-difference-in-bst / 相同

# 示例 1：
# 输入：root = [4, 2, 6, 1, 3]
# 输出：1

# 示例 2：
# 输入：root = [1, 0, 48, null, null, 12, 49]
# 输出：1

# 提示：
# 树中节点数目在范围[2, 100] 内
# 0 <= Node.val <= 10^5

from typing import Tuple
from treenode import TreeNode
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        if not root:
            return 0

        def innerDiff(node: TreeNode) -> Tuple:
            if not node:
                return None
            minDiff = 100000
            lb = rb = node.val
            if node.left:
                res = innerDiff(node.left)
                minDiff = min(minDiff, res[0], abs(res[2] - node.val))
                lb = res[1]
            if node.right:
                res = innerDiff(node.right)
                minDiff = min(minDiff, res[0], abs(res[1] - node.val))
                rb = res[2]
            return (minDiff, lb, rb)

        return innerDiff(root)[0]
# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    print(solution.minDiffInBST(TreeNode.createBFSTree(
        [71, 62, 84, 14, None, None, 88])))
    # print(solution.minDiffInBST(TreeNode.createBFSTree([4, 2, 6, 1, 3])))
    # print(solution.minDiffInBST(
    #     TreeNode.createBFSTree([1, 0, 48, None, None, 12, 49])))
