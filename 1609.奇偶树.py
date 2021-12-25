#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2021-12-25 23:01:46
LastEditors: Thomas Young
LastEditTime: 2021-12-25 23:38:57
'''
#
# @lc app=leetcode.cn id=1609 lang=python3
#
# [1609] 奇偶树
#
# 如果一棵二叉树满足下述几个条件，则可以称为 奇偶树 ：

# 二叉树根节点所在层下标为 0 ，根的子节点所在层下标为 1 ，根的孙节点所在层下标为 2 ，依此类推。
# 偶数下标 层上的所有节点的值都是 奇 整数，从左到右按顺序 严格递增
# 奇数下标 层上的所有节点的值都是 偶 整数，从左到右按顺序 严格递减
# 给你二叉树的根节点，如果二叉树为 奇偶树 ，则返回 true ，否则返回 false 。


# 示例 1：
# 输入：root = [1, 10, 4, 3, None, 7, 9, 12, 8, 6, None, None, 2]
# 输出：true
# 解释：每一层的节点值分别是：
# 0 层：[1]
# 1 层：[10, 4]
# 2 层：[3, 7, 9]
# 3 层：[12, 8, 6, 2]
# 由于 0 层和 2 层上的节点值都是奇数且严格递增，而 1 层和 3 层上的节点值都是偶数且严格递减，因此这是一棵奇偶树。

# 示例 2：
# 输入：root = [5, 4, 2, 3, 3, 7]
# 输出：false
# 解释：每一层的节点值分别是：
# 0 层：[5]
# 1 层：[4, 2]
# 2 层：[3, 3, 7]
# 2 层上的节点值不满足严格递增的条件，所以这不是一棵奇偶树。

# 示例 3：
# 输入：root = [5, 9, 1, 3, 5, 7]
# 输出：false
# 解释：1 层上的节点值应为偶数。

# 示例 4：
# 输入：root = [1]
# 输出：true

# 示例 5：
# 输入：root = [11, 8, 6, 1, 3, 9, 11, 30, 20, 18, 16, 12, 10, 4, 2, 17]
# 输出：true


# 提示：
# 树中节点数在范围[1, 10^5] 内
# 1 <= Node.val <= 10^6


from treenode import TreeNode
from typing import Optional, List
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        def valid(nodes: List[TreeNode], level: int, next: List[TreeNode]) -> bool:
            oddAndAsc = (level & 1) == 0
            prev = None
            for n in nodes:
                if oddAndAsc ^ (n.val & 1) == 1:
                    # 违反奇偶性要求
                    return False
                if prev:
                    if n.val == prev.val or (oddAndAsc ^ (n.val > prev.val)):
                        # 违反单调性要求
                        return False

                if n.left:
                    next.append(n.left)
                if n.right:
                    next.append(n.right)
                prev = n
            return True

        siblings = [root]
        level = 0
        while siblings:
            next = []
            v = valid(siblings, level, next)
            if not v:
                return False
            level += 1
            siblings = next
        
        return True

# @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.isEvenOddTree(TreeNode.createBFSTree(
        [13, 34, 32, 23, 25, 27, 29, 44, 40, 36, 34, 30, 30, 28, 26, 3, 7, 9, 11, 15, 17, 21, 25, None, None, 27, 31, 35, None, 37, None, 30, None, 26, None, None, None, 24, None, 20, 16, 12, 10, None, None, 8, None, None, None, None, None, 6, None, None, None, None, None, 15, 19, None, None, None, None, 23, None, 27, 29, 33, 37, None, None, None, None, None, None, 48, None, None, None, 46, None, None, None, 42, 38, 34, 32, None, None, None, None, 19])))  # False
    print(solution.isEvenOddTree(TreeNode.createBFSTree(
        [5, 9, 1, 3, 5, 7])))  # False
    print(solution.isEvenOddTree(TreeNode.createBFSTree(
        [1, 10, 4, 3, None, 7, 9, 12, 8, 6, None, None, 2]))) # True
    print(solution.isEvenOddTree(TreeNode.createBFSTree(
        [5, 4, 2, 3, 3, 7])))  # False
    print(solution.isEvenOddTree(TreeNode.createBFSTree(
        [1]))) # True
    print(solution.isEvenOddTree(TreeNode.createBFSTree(
        [11, 8, 6, 1, 3, 9, 11, 30, 20, 18, 16, 12, 10, 4, 2, 17])))  # True
