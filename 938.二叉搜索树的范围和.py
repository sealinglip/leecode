#
# @lc app=leetcode.cn id=938 lang=python3
#
# [938] 二叉搜索树的范围和
#
# 给定二叉搜索树的根结点 root，返回值位于范围[low, high] 之间的所有结点的值的和。

# 示例 1：
# 输入：root = [10, 5, 15, 3, 7, null, 18], low = 7, high = 15
# 输出：32

# 示例 2：
# 输入：root = [10, 5, 15, 3, 7, 13, 18, 1, null, 6], low = 6, high = 10
# 输出：23

# 提示：
# 树中节点数目在范围[1, 2 * 10^4] 内
# 1 <= Node.val <= 10 ^ 5
# 1 <= low <= high <= 10 ^ 5
# 所有 Node.val 互不相同

from treenode import TreeNode
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        sum = 0
        stack = [root]
        while stack:
            node = stack.pop()
            if low <= node.val <= high:
                sum += node.val
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            elif node.val > high:
                if node.left:
                    stack.append(node.left)
            elif node.right:
                stack.append(node.right)

        return sum

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.rangeSumBST(
        TreeNode.createBFSTree([10, 5, 15, 3, 7, None, 18]), 7, 15))
    print(solution.rangeSumBST(
        TreeNode.createBFSTree([10, 5, 15, 3, 7, 13, 18, 1, None, 6]), 6, 10))
