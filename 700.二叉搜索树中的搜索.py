#
# @lc app=leetcode.cn id=700 lang=python3
#
# [700] 二叉搜索树中的搜索
#
# 给定二叉搜索树（BST）的根节点和一个值。 你需要在BST中找到节点值等于给定值的节点。 返回以该节点为根的子树。 如果节点不存在，则返回 NULL。

# 例如，

# 给定二叉搜索树:
#         4
#        / \
#       2   7
#      / \
#     1   3

# 和值: 2
# 你应该返回如下子树:

#       2
#      / \
#     1   3
# 在上述示例中，如果要找的值是 5，但因为没有节点值为 5，我们应该返回 NULL。
from treenode import TreeNode

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        node = root
        while node:
            if node.val == val:
                break
            elif node.val < val:
                node = node.right
            else:
                node = node.left

        return node

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.searchBST(TreeNode.createBFSTree(
        [4, 2, 7, 1, 3]), 2).serialize())
