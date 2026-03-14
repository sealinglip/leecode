#
# @lc app=leetcode.cn id=1339 lang=python3
#
# [1339] 分裂二叉树的最大乘积
#
# https://leetcode.cn/problems/maximum-product-of-splitted-binary-tree/description/
#
# algorithms
# Medium (42.98%)
# Likes:    129
# Dislikes: 0
# Total Accepted:    21.2K
# Total Submissions: 47K
# Testcase Example:  '[1,2,3,4,5,6]'
#
# 给你一棵二叉树，它的根为 root 。请你删除 1 条边，使二叉树分裂成两棵子树，且它们子树和的乘积尽可能大。
# 由于答案可能会很大，请你将结果对 10^9 + 7 取模后再返回。
# 
# 
# 示例 1：
# 输入：root = [1,2,3,4,5,6]
# 输出：110
# 解释：删除红色的边，得到 2 棵子树，和分别为 11 和 10 。它们的乘积是 110 （11*10）
# 
# 示例 2：
# 输入：root = [1,null,2,3,4,null,null,5,6]
# 输出：90
# 解释：移除红色的边，得到 2 棵子树，和分别是 15 和 6 。它们的乘积为 90 （15*6）
# 
# 示例 3：
# 输入：root = [2,3,9,10,7,8,6,5,4,11,1]
# 输出：1025
# 
# 示例 4：
# 输入：root = [1,1]
# 输出：1
# 
# 
# 提示：
# 每棵树最多有 50000 个节点，且至少有 2 个节点。
# 每个节点的值在 [1, 10000] 之间。
# 
# 
#

from bisect import bisect_left
from treenode import TreeNode
from typing import Optional
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = 10 ** 9 + 7

        # 遍历得到每个节点（及其子节点）的值和，记录到sumList中
        sumList = []
        def calSum(node: TreeNode) -> int:
            if node is None:
                return 0
            res = node.val + calSum(node.left) + calSum(node.right)
            sumList.append(res)
            return res
        calSum(root)

        sumList.sort()
        total = sumList[-1]
        idx = bisect_left(sumList, total >> 1)
        if idx == len(sumList) - 1: # 如果没有哪个节点（非根）值和接近一半
            idx -= 1
        res = (total - sumList[idx]) * sumList[idx]
        if idx > 0:
            idx -= 1
            res = max(res, (total - sumList[idx]) * sumList[idx])
        
        return res % MOD
        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.maxProduct(TreeNode.createBFSTree([10,7,6,None,10,None,10]))) # 442
    print(solution.maxProduct(TreeNode.createBFSTree([1,2,3,4,5,6]))) # 110
    print(solution.maxProduct(TreeNode.createBFSTree([1,None,2,3,4,None,None,5,6]))) # 90
    print(solution.maxProduct(TreeNode.createBFSTree([2,3,9,10,7,8,6,5,4,11,1]))) # 1025
    print(solution.maxProduct(TreeNode.createBFSTree([1,1]))) # 1
