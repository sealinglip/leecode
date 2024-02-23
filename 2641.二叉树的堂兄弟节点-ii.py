#
# @lc app=leetcode.cn id=2641 lang=python3
#
# [2641] 二叉树的堂兄弟节点 II
#
# 给你一棵二叉树的根 root ，请你将每个节点的值替换成该节点的所有 堂兄弟节点值的和 。
# 如果两个节点在树中有相同的深度且它们的父节点不同，那么它们互为 堂兄弟 。
# 请你返回修改值之后，树的根 root 。

# 注意，一个节点的深度指的是从树根节点到这个节点经过的边数。


# 示例 1：
# 输入：root = [5,4,9,1,10,null,7]
# 输出：[0,0,0,7,7,null,11]
# 解释：上图展示了初始的二叉树和修改每个节点的值之后的二叉树。
# - 值为 5 的节点没有堂兄弟，所以值修改为 0 。
# - 值为 4 的节点没有堂兄弟，所以值修改为 0 。
# - 值为 9 的节点没有堂兄弟，所以值修改为 0 。
# - 值为 1 的节点有一个堂兄弟，值为 7 ，所以值修改为 7 。
# - 值为 10 的节点有一个堂兄弟，值为 7 ，所以值修改为 7 。
# - 值为 7 的节点有两个堂兄弟，值分别为 1 和 10 ，所以值修改为 11 。

# 示例 2：
# 输入：root = [3,1,2]
# 输出：[0,0,0]
# 解释：上图展示了初始的二叉树和修改每个节点的值之后的二叉树。
# - 值为 3 的节点没有堂兄弟，所以值修改为 0 。
# - 值为 1 的节点没有堂兄弟，所以值修改为 0 。
# - 值为 2 的节点没有堂兄弟，所以值修改为 0 。
 

# 提示：
# 树中节点数目的范围是 [1, 10^5] 。
# 1 <= Node.val <= 10^4

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
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # 先求每一层级所有节点的值之和
        nodes = [root]
        totals = []
        while nodes:
            total = 0
            newNodes = []
            for n in nodes:
                total += n.val
                if n.left:
                    newNodes.append(n.left)
                if n.right:
                    newNodes.append(n.right)

            totals.append(total)
            nodes = newNodes

        nodes = [root]
        depth = 1
        while nodes:
            newNodes = []
            for n in nodes:
                val = (n.left.val if n.left else 0) + (n.right.val if n.right else 0)
                if n.left:
                    newNodes.append(n.left)
                    n.left.val = totals[depth] - val
                if n.right:
                    newNodes.append(n.right)
                    n.right.val = totals[depth] - val

            nodes = newNodes
            depth += 1
        root.val = 0 # 根节点特殊处理

        return root
        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    root = TreeNode.createBFSTree([5,4,9,1,10,None,7])
    root = solution.replaceValueInTree(root)
    print(root.serialize()) # [0,0,0,7,7,None,11]

    root = TreeNode.createBFSTree([3,1,2])
    root = solution.replaceValueInTree(root)
    print(root.serialize()) # [0,0,0]