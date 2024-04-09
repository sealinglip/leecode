#
# @lc app=leetcode.cn id=894 lang=python3
#
# [894] 所有可能的真二叉树
#
# 给你一个整数 n ，请你找出所有可能含 n 个节点的 真二叉树 ，并以列表形式返回。答案中每棵树的每个节点都必须符合 Node.val == 0 。

# 答案的每个元素都是一棵真二叉树的根节点。你可以按 任意顺序 返回最终的真二叉树列表。

# 真二叉树 是一类二叉树，树中每个节点恰好有 0 或 2 个子节点。


# 示例 1：
# 输入：n = 7
# 输出：[[0,0,0,None,None,0,0,None,None,0,0],[0,0,0,None,None,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,None,None,None,None,0,0],[0,0,0,0,0,None,None,0,0]]

# 示例 2：
# 输入：n = 3
# 输出：[[0,0,0]]
 

# 提示：
# 1 <= n <= 20

from treenode import TreeNode
from typing import List, Optional
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        # n的数值很小，递归即可
        if n == 1:
            return [TreeNode(0)]
        elif (n & 1) == 0: # 真二叉树不可能是偶数个节点
            return []
        
        res = []
        for i in range(1, n-1, 2):
            l = self.allPossibleFBT(i)
            r = self.allPossibleFBT(n - 1 - i)
            for li in l:
                for ri in r:
                    root = TreeNode(0, li, ri)
                    res.append(root)
        return res
# @lc code=end

def printResult(trees: List[TreeNode]) -> List[str]:
    return [root.serialize() for root in trees]

if __name__ == "__main__":
    solution = Solution()
    print(printResult(solution.allPossibleFBT(7))) # [[0,0,0,None,None,0,0,None,None,0,0],[0,0,0,None,None,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,None,None,None,None,0,0],[0,0,0,0,0,None,None,0,0]]
    print(printResult(solution.allPossibleFBT(3))) # [[0,0,0]]
