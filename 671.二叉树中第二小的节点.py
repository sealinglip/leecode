#
# @lc app=leetcode.cn id=671 lang=python3
#
# [671] 二叉树中第二小的节点
#
# 给定一个非空特殊的二叉树，每个节点都是正数，并且每个节点的子节点数量只能为 2 或 0。如果一个节点有两个子节点的话，那么该节点的值等于两个子节点中较小的一个。
# 更正式地说，root.val = min(root.left.val, root.right.val) 总成立。
# 给出这样的一个二叉树，你需要输出所有节点中的第二小的值。如果第二小的值不存在的话，输出 - 1 。

# 示例 1：
# 输入：root = [2, 2, 5, null, null, 5, 7]
# 输出：5
# 解释：最小的值是 2 ，第二小的值是 5 。

# 示例 2：
# 输入：root = [2, 2, 2]
# 输出：- 1
# 解释：最小的值是 2, 但是不存在第二小的值。

# 提示：
# 树中节点数目在范围[1, 25] 内
# 1 <= Node.val <= 2^31 - 1
# 对于树中每个节点 root.val == min(root.left.val, root.right.val)

from treenode import TreeNode
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        # 根节点就是最小值
        minVal = root.val
        res = -1
        # BFS遍历树，找到严格大于根节点值的最小值，就是答案
        stack = deque([root])
        while stack:
            node = stack.popleft()
            val = node.val
            if val > minVal:
                res = val
            if node.left and (res == -1 or res >= node.left.val):
                stack.append(node.left)
            if node.right and (res == -1 or res >= node.right.val):
                stack.append(node.right)

        return res


# @lc code=end
if __name__ == "__main__":
    solution = Solution()
    # root = TreeNode.createBFSTree(
    #     [1, 1, 3, 1, 1, 3, 4, 3, 1, 1, 1, 3, 8, 4, 8, 3, 3, 1, 6, 2, 1])
    # print(solution.findSecondMinimumValue(root))
    print(solution.findSecondMinimumValue(
        TreeNode.createBFSTree([2, 2, 5, None, None, 5, 7])))
