#
# @lc app=leetcode.cn id=1457 lang=python3
#
# [1457] 二叉树中的伪回文路径
#
# 给你一棵二叉树，每个节点的值为 1 到 9 。我们称二叉树中的一条路径是 「伪回文」的，
# 当它满足：路径经过的所有节点值的排列中，存在一个回文序列。

# 请你返回从根到叶子节点的所有路径中 伪回文 路径的数目。

# 示例 1：
# 输入：root = [2,3,1,3,1,null,1]
# 输出：2 
# 解释：上图为给定的二叉树。总共有 3 条从根到叶子的路径：红色路径 [2,3,3] ，绿色路径 [2,1,1] 和路径 [2,3,1] 。
#      在这些路径中，只有红色和绿色的路径是伪回文路径，因为红色路径 [2,3,3] 存在回文排列 [3,2,3] ，
#      绿色路径 [2,1,1] 存在回文排列 [1,2,1] 。

# 示例 2：
# 输入：root = [2,1,1,1,3,null,null,null,null,null,1]
# 输出：1 
# 解释：上图为给定二叉树。总共有 3 条从根到叶子的路径：绿色路径 [2,1,1] ，路径 [2,1,3,1] 和路径 [2,1] 。
#      这些路径中只有绿色路径是伪回文路径，因为 [2,1,1] 存在回文排列 [1,2,1] 。

# 示例 3：
# 输入：root = [9]
# 输出：1
 
# 提示：
# 给定二叉树的节点数目在范围 [1, 10^5] 内
# 1 <= Node.val <= 9

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
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        # 伪回文序列满足所有元素去重计数后，奇数至多一个，所以也不用关心实际的数量，只用关心奇偶性即可
        def dfs(node: TreeNode, mask: int) -> int:
            '''
            返回从node出发，初始掩码mask的情况下，伪回文路径个数
            '''
            res = 0
            if node == None:
                return res
            mask ^= (1 << node.val)
            if not node.left and not node.right:
                if mask.bit_count() <= 1:
                    res = 1
            else:
                res = dfs(node.left, mask) + dfs(node.right, mask)
            return res
        
        return dfs(root, 0)

# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.pseudoPalindromicPaths(TreeNode.createBFSTree([2,3,1,3,1,None,1]))) # 2
    print(solution.pseudoPalindromicPaths(TreeNode.createBFSTree([2,1,1,1,3,None,None,None,None,None,1]))) # 1
    print(solution.pseudoPalindromicPaths(TreeNode.createBFSTree([2]))) # 1