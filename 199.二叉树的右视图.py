#
# @lc app=leetcode.cn id=199 lang=python3
#
# [199] 二叉树的右视图
#
# 给定一个二叉树的 根节点 root，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。

# 示例 1:
# 输入: [1,2,3,null,5,null,4]
# 输出: [1,3,4]

# 示例 2:
# 输入: [1,null,3]
# 输出: [1,3]

# 示例 3:
# 输入: []
# 输出: []
 
# 提示:
# 二叉树的节点个数的范围是 [0,100]
# -100 <= Node.val <= 100 

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
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        rightSide = []
        maxDepth = -1
        stack = [(root, 0)] if root else None

        while stack:
            node, depth = stack.pop()
            if depth > maxDepth:
                maxDepth = depth
                rightSide.append(node.val)

            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth + 1))

        return rightSide
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.rightSideView(TreeNode.createBFSTree([1,2,3,None,5,None,4]))) # [1,3,4]
    print(solution.rightSideView(TreeNode.createBFSTree([1,None,3]))) # [1,3]
    print(solution.rightSideView(TreeNode.createBFSTree([]))) # []