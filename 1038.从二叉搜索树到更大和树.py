#
# @lc app=leetcode.cn id=1038 lang=python3
#
# [1038] 从二叉搜索树到更大和树
#
# 给定一个二叉搜索树 root (BST)，请将它的每个节点的值替换成树中大于或者等于该节点值的所有节点值之和。

# 提醒一下， 二叉搜索树 满足下列约束条件：

# 节点的左子树仅包含键 小于 节点键的节点。
# 节点的右子树仅包含键 大于 节点键的节点。
# 左右子树也必须是二叉搜索树。
 

# 示例 1：
# 输入：[4,1,6,0,2,5,7,None,None,None,3,None,None,None,8]
# 输出：[30,36,21,36,35,26,15,None,None,None,33,None,None,None,8]

# 示例 2：
# 输入：root = [0,None,1]
# 输出：[1,None,1]
 

# 提示：
# 树中的节点数在 [1, 100] 范围内。
# 0 <= Node.val <= 100
# 树中的所有值均 不重复 。
 

# 注意：该题目与 538: https://leetcode-cn.com/problems/convert-bst-to-greater-tree/  相同

from treenode import TreeNode
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        # 遍历顺序：先右后中再左
        def traverse(node: TreeNode, gt: int) -> int:
            '''
            node: 当前节点
            gt: 比当前节点值大，除本节点的右子树之外的所有节点值之和
            返回以该节点为根的所有树节点值之和
            '''
            v = node.val
            if node.right:
                v += traverse(node.right, gt)
            node.val = gt + v
            if node.left:
                v += traverse(node.left, node.val)
            return v

        traverse(root, 0)
        return root
        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.bstToGst(TreeNode.createBFSTree([4,1,6,0,2,5,7,None,None,None,3,None,None,None,8])).serialize()) # [30,36,21,36,35,26,15,None,None,None,33,None,None,None,8]
    print(solution.bstToGst(TreeNode.createBFSTree([0,None,1])).serialize()) # [1,None,1]