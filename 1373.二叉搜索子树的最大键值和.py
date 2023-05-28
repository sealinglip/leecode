#
# @lc app=leetcode.cn id=1373 lang=python3
#
# [1373] 二叉搜索子树的最大键值和
#
# 给你一棵以 root 为根的 二叉树 ，请你返回 任意 二叉搜索子树的最大键值和。

# 二叉搜索树的定义如下：

# 任意节点的左子树中的键值都 小于 此节点的键值。
# 任意节点的右子树中的键值都 大于 此节点的键值。
# 任意节点的左子树和右子树都是二叉搜索树。


# 示例 1：
# 输入：root = [1, 4, 3, 2, 4, 2, 5, null, null, null, null, null, null, 4, 6]
# 输出：20
# 解释：键值为 3 的子树是和最大的二叉搜索树。

# 示例 2：
# 输入：root = [4, 3, null, 1, 2]
# 输出：2
# 解释：键值为 2 的单节点子树是和最大的二叉搜索树。

# 示例 3：
# 输入：root = [-4, -2, -5]
# 输出：0
# 解释：所有节点键值都为负数，和最大的二叉搜索树为空。

# 示例 4：
# 输入：root = [2, 1, 3]
# 输出：6

# 示例 5：
# 输入：root = [5, 4, 8, 3, null, 6, 3]
# 输出：7


# 提示：
# 每棵树有 1 到 40000 个节点。
# 每个节点的键值在[-4 * 10 ^ 4, 4 * 10 ^ 4] 之间。

# Hard

from typing import Optional, Tuple
from treenode import TreeNode
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        res = 0

        def isBST(node: TreeNode) -> Tuple:
            nonlocal res
            if node.left is None and node.right is None:
                # 叶子节点
                res = max(res, node.val)
                return (True, node.val, node.val, node.val)
            else:
                su = mi = ma = node.val
                lValid = True
                if node.left:
                    lValid = False
                    l = isBST(node.left)
                    if l[0]:
                        # 左子树是二叉搜索树
                        lsu, lmi, lma = l[1:]
                        if lma < mi:
                            # 满足要求
                            su += lsu
                            mi = lmi
                            lValid = True

                rValid = True
                if node.right:
                    rValid = False
                    r = isBST(node.right)
                    if r[0]:
                        # 右子树是二叉搜索树
                        rsu, rmi, rma = r[1:]
                        if rmi > ma:
                            # 满足要求
                            su += rsu
                            ma = rma
                            rValid = True

                if lValid and rValid:
                    res = max(res, su)
                    return (True, su, mi, ma)
                else:
                    return (False, node.val, node.val, node.val)

        isBST(root)

        return res

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.maxSumBST(TreeNode.createBFSTree(
        [-4, -2, -5])))  # 0
    print(solution.maxSumBST(TreeNode.createBFSTree(
        [1, 4, 3, 2, 4, 2, 5, None, None, None, None, None, None, 4, 6])))  # 20
    print(solution.maxSumBST(TreeNode.createBFSTree(
        [4, 3, None, 1, 2])))  # 2
    print(solution.maxSumBST(TreeNode.createBFSTree(
        [2, 1, 3])))  # 6
    print(solution.maxSumBST(TreeNode.createBFSTree(
        [5, 4, 8, 3, None, 6, 3])))  # 7
