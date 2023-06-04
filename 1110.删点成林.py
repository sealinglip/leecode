#
# @lc app=leetcode.cn id=1110 lang=python3
#
# [1110] 删点成林
#
# 给出二叉树的根节点 root，树上每个节点都有一个不同的值。

# 如果节点值在 to_delete 中出现，我们就把该节点从树上删去，最后得到一个森林（一些不相交的树构成的集合）。

# 返回森林中的每棵树。你可以按任意顺序组织答案。


# 示例 1：
# 输入：root = [1, 2, 3, 4, 5, 6, 7], to_delete = [3, 5]
# 输出：[[1, 2, null, 4], [6], [7]]

# 示例 2：
# 输入：root = [1, 2, 4, null, 3], to_delete = [3]
# 输出：[[1, 2, 4]]


# 提示：
# 树中的节点数最大为 1000。
# 每个节点都有一个介于 1 到 1000 之间的值，且各不相同。
# to_delete.length <= 1000
# to_delete 包含一些从 1 到 1000、各不相同的值。

from typing import Optional, List
from treenode import TreeNode

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete = set(to_delete)
        res = []

        def deleteNode(node: TreeNode, parent: Optional[TreeNode], add_to_result: bool = False):
            d = node.val in to_delete
            if d:
                if parent:
                    if parent.left == node:
                        parent.left = None
                    if parent.right == node:
                        parent.right = None
            elif add_to_result:
                res.append(node)
            if node.left:
                deleteNode(node.left, node, d)
            if node.right:
                deleteNode(node.right, node, d)

        deleteNode(root, None, True)

        return res

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(list(map(lambda n: n.serialize(), solution.delNodes(
        TreeNode.createBFSTree([1, 2, 3, 4, 5, 6, 7]), [3, 5]))))  # ['1,2,N,4', '6', '7']
    print(list(map(lambda n: n.serialize(), solution.delNodes(
        TreeNode.createBFSTree([1, 2, 4, None, 3]), [3]))))  # [[1,2,4]]
