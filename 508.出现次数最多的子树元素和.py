#
# @lc app=leetcode.cn id=508 lang=python3
#
# [508] 出现次数最多的子树元素和
#
# 给你一个二叉树的根结点 root ，请返回出现次数最多的子树元素和。如果有多个元素出现的次数相同，返回所有出现次数最多的子树元素和（不限顺序）。

# 一个结点的 「子树元素和」 定义为以该结点为根的二叉树上所有结点的元素之和（包括结点本身）。


# 示例 1：
# 输入: root = [5, 2, -3]
# 输出: [2, -3, 4]

# 示例 2：
# 输入: root = [5, 2, -5]
# 输出: [2]


# 提示:
# 节点数在[1, 10^4] 范围内
# -10^5 <= Node.val <= 10^5


from treenode import TreeNode
from typing import List
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict


class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        stat = defaultdict(int)

        def treeSum(node: TreeNode):
            sum = node.val
            if node.left:
                sum += treeSum(node.left)
            if node.right:
                sum += treeSum(node.right)
            stat[sum] += 1
            return sum

        treeSum(root)
        maxSum = max(stat.values())
        stat.items()
        return [k for k, v in stat.items() if v == maxSum]


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.findFrequentTreeSum(
        TreeNode.createBFSTree([5, 2, -3])))  # [2, -3, 4]
    print(solution.findFrequentTreeSum(
        TreeNode.createBFSTree([5, 2, -5])))  # [2]
