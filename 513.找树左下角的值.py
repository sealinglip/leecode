#
# @lc app=leetcode.cn id=513 lang=python3
#
# [513] 找树左下角的值
#
# 给定一个二叉树的 根节点 root，请找出该二叉树的 最底层 最左边 节点的值。

# 假设二叉树中至少有一个节点。


# 示例 1:
# 输入: root = [2, 1, 3]
# 输出: 1

# 示例 2:
# 输入: [1, 2, 3, 4, None, 5, 6, None, None, 7]
# 输出: 7


# 提示:
# 二叉树的节点个数的范围是[1, 10^4]
# -2^31 <= Node.val <= 2^31 - 1


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
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return None

        def findBL(node: TreeNode, lvl: int) -> Tuple:
            bl = (node.val, lvl)
            if node.left:
                bl = findBL(node.left, lvl + 1)
            if node.right:
                rbl = findBL(node.right, lvl + 1)
                if rbl[1] > bl[1]:
                    bl = rbl
            return bl

        return findBL(root, 0)[0]


        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.findBottomLeftValue(TreeNode.createBFSTree([2, 1, 3])))  # 1
    print(solution.findBottomLeftValue(TreeNode.createBFSTree(
        [1, 2, 3, 4, None, 5, 6, None, None, 7])))  # 7
