#
# @lc app=leetcode.cn id=337 lang=python3
#
# [337] 打家劫舍 III
#
# 小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为 root 。
# 除了 root 之外，每栋房子有且只有一个“父“房子与之相连。一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。
# 如果 两个直接相连的房子在同一天晚上被打劫 ，房屋将自动报警。
# 给定二叉树的 root 。返回 在不触动警报的情况下 ，小偷能够盗取的最高金额 。


# 示例 1:
# 输入: root = [3, 2, 3, null, 3, null, 1]
# 输出: 7
# 解释: 小偷一晚能够盗取的最高金额 3 + 3 + 1 = 7

# 示例 2:
# 输入: root = [3, 4, 5, 1, 3, null, 1]
# 输出: 9
# 解释: 小偷一晚能够盗取的最高金额 4 + 5 = 9


# 提示：
# 树的节点数在[1, 10^4] 范围内
# 0 <= Node.val <= 10^4

from functools import cache
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
    def rob(self, root: Optional[TreeNode]) -> int:
        # 记 dp(node, f) 为以node为根节点的最高金额，f=0时不偷根节点，f=1时偷根节点
        @cache
        def dp(node: TreeNode, flag: int) -> int:
            if node is None:
                return 0
            if flag == 0:
                return max(dp(node.left, 0), dp(node.left, 1)) + max(dp(node.right, 0), dp(node.right, 1))
            else:
                return node.val + dp(node.left, 0) + dp(node.right, 0)

        return max(dp(root, 0), dp(root, 1))


        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.rob(TreeNode.createBFSTree(
        [3, 2, 3, None, 3, None, 1])))  # 7
    print(solution.rob(TreeNode.createBFSTree([3, 4, 5, 1, 3, None, 1])))  # 9
