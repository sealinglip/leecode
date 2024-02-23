#
# @lc app=leetcode.cn id=889 lang=python3
#
# [889] 根据前序和后序遍历构造二叉树
#
# 给定两个整数数组，preorder 和 postorder ，其中 preorder 是一个具有 无重复 值的二叉树的前序遍历，postorder 是同一棵树的后序遍历，重构并返回二叉树。

# 如果存在多个答案，您可以返回其中 任何 一个。

 
# 示例 1：
# 输入：preorder = [1,2,4,5,3,6,7], postorder = [4,5,2,6,7,3,1]
# 输出：[1,2,3,4,5,6,7]

# 示例 2:
# 输入: preorder = [1], postorder = [1]
# 输出: [1]
 

# 提示：
# 1 <= preorder.length <= 30
# 1 <= preorder[i] <= preorder.length
# preorder 中所有值都 不同
# postorder.length == preorder.length
# 1 <= postorder[i] <= postorder.length
# postorder 中所有值都 不同
# 保证 preorder 和 postorder 是同一棵二叉树的前序遍历和后序遍历

from typing import List, Optional
from treenode import TreeNode

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        
        def buildTree(preLeft: int, preRight: int, postLeft: int, postRight: int) -> TreeNode:
            node = TreeNode(preorder[preLeft])
            if postRight - postLeft > 1:
                if postorder[postRight-2] == preorder[preLeft+1]:
                    # 右子树为空
                    node.left = buildTree(preLeft+1, preRight, postLeft, postRight-1)
                else:
                    rightVal = postorder[postRight-2]
                    i = preLeft + 1
                    # 求node的右子树在preorder中的位置
                    while i < preRight and preorder[i] != rightVal:
                        i += 1
                    node.left = buildTree(preLeft+1, i, postLeft, i-preLeft+postLeft-1)
                    node.right = buildTree(i, preRight, postRight-preRight+i-1, postRight-1)
            return node

        return buildTree(0, len(preorder), 0, len(postorder))
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.constructFromPrePost([1,2], [2,1]).serialize()) # [1,2]
    print(solution.constructFromPrePost([1,2,4,5,3,6,7], [4,5,2,6,7,3,1]).serialize()) # [1,2,3,4,5,6,7]
    print(solution.constructFromPrePost([1], [1]).serialize()) # [1]