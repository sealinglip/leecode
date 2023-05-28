#
# @lc app=leetcode.cn id=1080 lang=python3
#
# [1080] 根到叶路径上的不足节点
#
# 给你二叉树的根节点 root 和一个整数 limit ，请你同时删除树中所有 不足节点 ，并返回最终二叉树的根节点。

# 假如通过节点 node 的每种可能的 “根-叶” 路径上值的总和全都小于给定的 limit，则该节点被称之为 不足节点 ，需要被删除。

# 叶子节点，就是没有子节点的节点。


# 示例 1：
# 输入：root = [1,2,3,4,-99,-99,7,8,9,-99,-99,12,13,-99,14], limit = 1
# 输出：[1,2,3,4,null,null,7,8,9,null,14]

# 示例 2：
# 输入：root = [5,4,8,11,null,17,4,7,1,null,null,5,3], limit = 22
# 输出：[5,4,8,11,null,17,4,7,null,null,null,5]

# 示例 3：
# 输入：root = [1,2,-3,-5,null,4,null], limit = -1
# 输出：[1,null,-3,4]


# 提示：
# 树中节点数目在范围 [1, 5000] 内
# -10^5 <= Node.val <= 10^5
# -10^9 <= limit <= 10^9

from math import inf
from typing import Optional
from treenode import TreeNode

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
        def dfs(node: TreeNode, accum: int) -> bool:
            accum += node.val
            if node.left or node.right:
                l = r = False
                if node.left:
                    l = dfs(node.left, accum)
                    if not l:
                        node.left = None
                if node.right:
                    r = dfs(node.right, accum)
                    if not r:
                        node.right = None
                return l or r
            else:
                return accum >= limit

        v = dfs(root, 0)
        return root if v else None

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.sufficientSubset(TreeNode.createBFSTree(
        [1, 2, 3, 4, -99, -99, 7, 8, 9, -99, -99, 12, 13, -99, 14]), 1).serialize())
    print(solution.sufficientSubset(TreeNode.createBFSTree(
        [5, 4, 8, 11, None, 17, 4, 7, 1, None, None, 5, 3]), 22).serialize())
    print(solution.sufficientSubset(TreeNode.createBFSTree(
        [1, 2, -3, -5, None, 4, None]), 1).serialize())
