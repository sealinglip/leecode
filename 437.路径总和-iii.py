#
# @lc app=leetcode.cn id=437 lang=python3
#
# [437] 路径总和 III
#
# 给定一个二叉树的根节点 root ，和一个整数 targetSum ，求该二叉树里节点值之和等于 targetSum 的 路径 的数目。
# 路径 不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。


# 示例 1：
# 输入：root = [10, 5, -3, 3, 2, null, 11, 3, -2, null, 1], targetSum = 8
# 输出：3
# 解释：和等于 8 的路径有 3 条，如图所示。

# 示例 2：
# 输入：root = [5, 4, 8, 11, null, 13, 4, 7, 2, null, null, 5, 1], targetSum = 22
# 输出：3


# 提示:
# 二叉树的节点个数的范围是[0, 1000]
# -10^9 <= Node.val <= 10^9
# -1000 <= targetSum <= 1000

from treenode import TreeNode
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict


class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        prefixSumDict = defaultdict(int)  # 保存前缀和的字典
        prefixSumDict[0] = 1  # 前缀和为0有一种情况，就是路径为空（初始情况）

        def dfs(node: TreeNode, prefixSum: int) -> int:
            if node is None:
                return 0
            cnt = 0
            prefixSum += node.val
            cnt += prefixSumDict[prefixSum - targetSum]
            prefixSumDict[prefixSum] += 1
            if node.left:
                cnt += dfs(node.left, prefixSum)
            if node.right:
                cnt += dfs(node.right, prefixSum)

            prefixSumDict[prefixSum] -= 1
            return cnt

        return dfs(root, 0)
# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    print(solution.pathSum(TreeNode.createBFSTree(
        [10, 5, -3, 3, 2, None, 11, 3, -2, None, 1]), 8))  # 3
    print(solution.pathSum(TreeNode.createBFSTree(
        [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]), 22))  # 3
