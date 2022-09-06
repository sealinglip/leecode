#
# @lc app=leetcode.cn id=654 lang=python3
#
# [654] 最大二叉树
#
# 给定一个不重复的整数数组 nums 。 最大二叉树 可以用下面的算法从 nums 递归地构建:

# 创建一个根节点，其值为 nums 中的最大值。
# 递归地在最大值 左边 的 子数组前缀上 构建左子树。
# 递归地在最大值 右边 的 子数组后缀上 构建右子树。
# 返回 nums 构建的 最大二叉树 。


# 示例 1：


# 输入：nums = [3, 2, 1, 6, 0, 5]
# 输出：[6, 3, 5, None, 2, 0, None, None, 1]
# 解释：递归调用如下所示：
# - [3, 2, 1, 6, 0, 5] 中的最大值是 6 ，左边部分是[3, 2, 1] ，右边部分是[0, 5] 。
#  - [3, 2, 1] 中的最大值是 3 ，左边部分是[] ，右边部分是[2, 1] 。
#   - 空数组，无子节点。
#    - [2, 1] 中的最大值是 2 ，左边部分是[] ，右边部分是[1] 。
#       - 空数组，无子节点。
#        - 只有一个元素，所以子节点是一个值为 1 的节点。
#     - [0, 5] 中的最大值是 5 ，左边部分是[0] ，右边部分是[] 。
#     - 只有一个元素，所以子节点是一个值为 0 的节点。
#     - 空数组，无子节点。
# 示例 2：


# 输入：nums = [3, 2, 1]
# 输出：[3, None, 2, None, 1]


# 提示：
# 1 <= nums.length <= 1000
# 0 <= nums[i] <= 1000
# nums 中的所有整数 互不相同

from treenode import TreeNode
from typing import List, Optional

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def buildTree(arr: List[int], start: int, end: int) -> Optional[TreeNode]:
            if start == end:
                return None
            # locate max ele
            maxEle = nums[start]
            maxIdx = start
            for i in range(start + 1, end):
                if nums[i] > maxEle:
                    maxEle = nums[i]
                    maxIdx = i

            node = TreeNode(maxEle)
            node.left = buildTree(arr, start, maxIdx)
            node.right = buildTree(arr, maxIdx + 1, end)
            return node

        return buildTree(nums, 0, len(nums))
        # @lc code=end
