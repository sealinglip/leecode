#
# @lc app=leetcode.cn id=429 lang=python3
#
# [429] N 叉树的层序遍历
#
# 给定一个 N 叉树，返回其节点值的层序遍历。（即从左到右，逐层遍历）。

# 树的序列化输入是用层序遍历，每组子节点都由 None 值分隔（参见示例）。


# 示例 1：
# 输入：root = [1,None,3,2,4,None,5,6]
# 输出：[[1],[3,2,4],[5,6]]

# 示例 2：
# 输入：root = [1,None,2,3,4,5,None,None,6,7,None,8,None,9,10,None,None,11,None,12,None,13,None,None,14]
# 输出：[[1],[2,3,4,5],[6,7,8,9,10],[11,12,13],[14]]


# 提示：
# 树的高度不会超过 1000
# 树的节点总数在 [0, 10^4] 之间

from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        level = [root]
        res = []
        while level:
            res.append([n.val for n in level])
            newLevel = []
            for n in level:
                if n.children:
                    newLevel.extend(n.children)
            level = newLevel

        return res

        # @lc code=end
