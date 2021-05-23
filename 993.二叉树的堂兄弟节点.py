#
# @lc app=leetcode.cn id=993 lang=python3
#
# [993] 二叉树的堂兄弟节点
#
# 在二叉树中，根节点位于深度 0 处，每个深度为 k 的节点的子节点位于深度 k+1 处。
# 如果二叉树的两个节点深度相同，但 父节点不同 ，则它们是一对堂兄弟节点。
# 我们给出了具有唯一值的二叉树的根节点 root ，以及树中两个不同节点的值 x 和 y 。
# 只有与值 x 和 y 对应的节点是堂兄弟节点时，才返回 true 。否则，返回 false。

# 示例 1：
# 输入：root = [1, 2, 3, 4], x = 4, y = 3
# 输出：false

# 示例 2：
# 输入：root = [1, 2, 3, null, 4, null, 5], x = 5, y = 4
# 输出：true

# 示例 3：
# 输入：root = [1, 2, 3, null, 4], x = 2, y = 3
# 输出：false

# 提示：
# 二叉树的节点数介于 2 到 100 之间。
# 每个节点的值都是唯一的、范围为 1 到 100 的整数。

from treenode import TreeNode
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if x == y:
            return False

        stack = [(root, 0)]
        p1 = p2 = None
        while stack:
            node, level = stack.pop()
            if node.left:
                if node.left.val == x:
                    p1 = (node, level)
                elif node.left.val == y:
                    p2 = (node, level)
                stack.append((node.left, level + 1))
            if node.right:
                if node.right.val == x:
                    p1 = (node, level)
                elif node.right.val == y:
                    p2 = (node, level)
                stack.append((node.right, level + 1))
            if p1 and p2:
                break

        return (p1 is not None) and (p2 is not None) and p1[0] != p2[0] and p1[1] == p2[1]

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.isCousins(TreeNode.createBFSTree(
        [1, None, 2, 3, None, None, 4, None, 5]), 1, 3))
    print(solution.isCousins(TreeNode.createBFSTree([1, 2, 3, 4]), 4, 3))
    print(solution.isCousins(
        TreeNode.createBFSTree([1, 2, 3, None, 4, None, 5]), 5, 4))
    print(solution.isCousins(TreeNode.createBFSTree([1, 2, 3, None, 4]), 2, 3))
