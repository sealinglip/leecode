#
# @lc app=leetcode.cn id=450 lang=python3
#
# [450] 删除二叉搜索树中的节点
#
# 给定一个二叉搜索树的根节点 root 和一个值 key，删除二叉搜索树中的 key 对应的节点，并保证二叉搜索树的性质不变。返回二叉搜索树（有可能被更新）的根节点的引用。

# 一般来说，删除节点可分为两个步骤：

# 首先找到需要删除的节点；
# 如果找到了，删除它。


# 示例 1:
# 输入：root = [5, 3, 6, 2, 4, null, 7], key = 3
# 输出：[5, 4, 6, 2, null, null, 7]
# 解释：给定需要删除的节点值是 3，所以我们首先找到 3 这个节点，然后删除它。
# 一个正确的答案是[5, 4, 6, 2, null, null, 7], 如下图所示。
# 另一个正确答案是[5, 2, 6, null, 4, null, 7]。

# 示例 2:
# 输入: root = [5, 3, 6, 2, 4, null, 7], key = 0
# 输出: [5, 3, 6, 2, 4, null, 7]
# 解释: 二叉树不包含值为 0 的节点

# 示例 3:
# 输入: root = [], key = 0
# 输出: []


# 提示:
# 节点数的范围[0, 104].
# -10^5 <= Node.val <= 10^5
# 节点值唯一
# root 是合法的二叉搜索树
# -10^5 <= key <= 10^5

# 进阶： 要求算法时间复杂度为 O(h)，h 为树的高度。
# 复习
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
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # 迭代
        node = root
        prev = None
        # 先找对应节点
        while node:
            if node.val == key:
                break
            else:
                prev = node
                if node.val < key:
                    # 走右边
                    node = node.right
                else:
                    # 走左边
                    node = node.left

        # 找到了
        if node:
            # 判断节点是不是父节点的左节点——如果节点就是根，认为也是左
            isLeft = prev is None or prev.left == node

            rp = None
            p = node
            if node.left is None or node.right is None:
                # node 有任何一支为空的话，直接将node换成自己存在的子节点即可
                rp = node.left or node.right
            else:
                # 找node的左子树的最右节点作为本节点的替代品
                rp = node.left
                while rp.right:
                    p = rp
                    rp = rp.right
                if p.right == rp:
                    p.right = rp.left
                else:
                    p.left = rp.left

                if rp:
                    rp.left = node.left
                    rp.right = node.right
            if prev:
                if isLeft:
                    prev.left = rp
                else:
                    prev.right = rp
            else:
                root = rp

        return root

        # 递归
        # if root is None:
        #     return None
        # if root.val > key:
        #     root.left = self.deleteNode(root.left, key)
        # elif root.val < key:
        #     root.right = self.deleteNode(root.right, key)
        # elif root.left is None or root.right is None:
        #     root = root.left if root.left else root.right
        # else:
        #     successor = root.right
        #     while successor.left:
        #         successor = successor.left
        #     successor.right = self.deleteNode(root.right, successor.val)
        #     successor.left = root.left
        #     return successor
        # return root

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    # root = TreeNode.createBFSTree([5, 3, 6, 2, 4, None, 7])
    # root = solution.deleteNode(root, 3)
    # print(root.serialize())

    root = TreeNode.createBFSTree(
        [4, None, 7, 6, 8, 5, None, None, 9])  # [4,null,8,6,9,5]
    root = solution.deleteNode(root, 7)
    print(root.serialize())
