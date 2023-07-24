#
# @lc app=leetcode.cn id=979 lang=python3
#
# [979] 在二叉树中分配硬币
#
# 给定一个有 N 个结点的二叉树的根结点 root，树中的每个结点上都对应有 node.val 枚硬币，并且总共有 N 枚硬币。

# 在一次移动中，我们可以选择两个相邻的结点，然后将一枚硬币从其中一个结点移动到另一个结点。
# (移动可以是从父结点到子结点，或者从子结点移动到父结点。)。

# 返回使每个结点上只有一枚硬币所需的移动次数。


# 示例 1：
# 输入：[3, 0, 0]
# 输出：2
# 解释：从树的根结点开始，我们将一枚硬币移到它的左子结点上，一枚硬币移到它的右子结点上。

# 示例 2：
# 输入：[0, 3, 0]
# 输出：3
# 解释：从根结点的左子结点开始，我们将两枚硬币移到根结点上[移动两次]。然后，我们把一枚硬币从根结点移到右子结点上。

# 示例 3：
# 输入：[1, 0, 2]
# 输出：2

# 示例 4：
# 输入：[1, 0, 0, null, 3]
# 输出：4


# 提示：
# 1 <= N <= 100
# 0 <= node.val <= N


from treenode import TreeNode
from typing import Optional, Tuple
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        # 第一次遍历得到所有节点的以该节点为根的子树值之和，以及子树所有节点数
        cache = {}

        def lrd(node: TreeNode) -> Tuple[int, int]:
            l = (0, 0) if node.left is None else lrd(node.left)
            r = (0, 0) if node.right is None else lrd(node.right)
            t = (l[0] + r[0] + node.val, l[1] + r[1] + 1)
            cache[node] = t
            return t

        def dlr(node: TreeNode) -> int:
            t = cache[node]
            res = 0
            if node.left:
                l = cache[node.left]
                res += abs(l[0] - l[1])
                res += dlr(node.left)
            if node.right:
                r = cache[node.right]
                res += abs(r[0] - r[1])
                res += dlr(node.right)

            return res

        lrd(root)
        return dlr(root)

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.distributeCoins(TreeNode.createBFSTree([3, 0, 0])))  # 2
    print(solution.distributeCoins(TreeNode.createBFSTree([0, 3, 0])))  # 3
    print(solution.distributeCoins(TreeNode.createBFSTree([1, 0, 2])))  # 2
    print(solution.distributeCoins(
        TreeNode.createBFSTree([1, 0, 0, None, 3])))  # 4
