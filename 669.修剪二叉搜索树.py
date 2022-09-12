#
# @lc app=leetcode.cn id=669 lang=python3
#
# [669] 修剪二叉搜索树
#
# 给你二叉搜索树的根节点 root ，同时给定最小边界low 和最大边界 high。通过修剪二叉搜索树，使得所有节点的值在[low, high]中。
# 修剪树 不应该 改变保留在树中的元素的相对结构(即，如果没有被移除，原有的父代子代关系都应当保留)。 可以证明，存在 唯一的答案 。

# 所以结果应当返回修剪好的二叉搜索树的新的根节点。注意，根节点可能会根据给定的边界发生改变。


# 示例 1：
# 输入：root = [1, 0, 2], low = 1, high = 2
# 输出：[1, None, 2]

# 示例 2：
# 输入：root = [3, 0, 4, None, 2, None, None, 1], low = 1, high = 3
# 输出：[3, 2, None, 1]


# 提示：
# 树中节点数在范围[1, 10^4] 内
# 0 <= Node.val <= 10^4
# 树中每个节点的值都是 唯一 的
# 题目数据保证输入是一棵有效的二叉搜索树
# 0 <= low <= high <= 10^4

# 复习

from treenode import TreeNode
from typing import Optional
from collections import deque
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        # 方法1：递归
        # if root is None:
        #     return root
        # elif root.val < low:
        #     return self.trimBST(root.right, low, high)
        # elif root.val > high:
        #     return self.trimBST(root.left, low, high)
        # root.left = self.trimBST(root.left, low, high)
        # root.right = self.trimBST(root.right, low, high)
        # return root

        # 方法2：直接遍历处理
        # 先找到在区间之内的root
        while root and (root.val < low or root.val > high):
            root = root.left if root.val > high else root.right
        if root:
            # 如果找到了root，那么依次处理其left和right
            node = root
            # 如果节点在区间内，如果节点的左节点值<low，那么左节点的左子树都不在区间，将被裁剪，左节点直接可赋值为左节点的右子树，再重新裁剪
            # 如果左节点的值>=low，那么左节点的右子树肯定都在区间内（因为右子树取值范围为左节点和根节点之间，肯定在区间内。此处，继续裁剪左节点的左子树即可
            while node.left:
                if node.left.val < low:
                    node.left = node.left.right
                else:
                    node = node.left

            node = root
            # 同理处理右子树
            while node.right:
                if node.right.val > high:
                    node.right = node.right.left
                else:
                    node = node.right
        return root

        # if root:
        #     dummy = TreeNode(low)
        #     if root.val < low:
        #         dummy.left = root
        #     else:
        #         dummy.right = root
        #     qu = deque([dummy])

        #     while qu:
        #         node = qu.popleft()
        #         for i, n in enumerate([node.left, node.right]):
        #             if n:
        #                 if n.val < low or n.val > high:
        #                     tmp = n
        #                     while tmp:
        #                         if tmp.val < low:
        #                             tmp = tmp.right
        #                         elif tmp.val > high:
        #                             tmp = tmp.left
        #                         else:
        #                             break
        #                     if i == 0:
        #                         node.left = tmp
        #                     else:
        #                         node.right = tmp
        #                     n = tmp
        #                 if n:
        #                     qu.append(n)
        #     root = dummy.left or dummy.right

        # return root


        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    # [36,34,42,33,35,41,43,32,None,None,None,37,None,None,44,None,None,None,38,None,None,None,39,None,40]
    print(TreeNode.serialize(solution.trimBST(
        TreeNode.createBFSTree([45, 30, 46, 10, 36, None, 49, 8, 24, 34, 42, 48, None, 4, 9, 14, 25, 31, 35, 41, 43, 47, None, 0, 6, None, None, 11, 20, None, 28, None, 33, None, None, 37, None, None, 44, None, None, None, 1, 5, 7, None, 12, 19, 21, 26, 29, 32, None, None, 38, None, None, None, 3, None, None, None, None, None, 13, 18, None, None, 22, None, 27, None, None, None, None, None, 39, 2, None, None, None, 15, None, None, 23, None, None, None, 40, None, None, None, 16, None, None, None, None, None, 17]), 32, 44)))
    print(TreeNode.serialize(solution.trimBST(
        TreeNode.createBFSTree([1, None, 2]), 2, 4)))  # [2]
    print(TreeNode.serialize(solution.trimBST(
        TreeNode.createBFSTree([1, 0, 2]), 1, 2)))  # [1, None, 2]
    print(TreeNode.serialize(solution.trimBST(
        TreeNode.createBFSTree([3, 0, 4, None, 2, None, None, 1]), 1, 3)))  # [3, 2, None, 1]
