#
# @lc app=leetcode.cn id=572 lang=python3
#
# [572] 另一棵树的子树
#
# 给你两棵二叉树 root 和 subRoot 。检验 root 中是否包含和 subRoot 具有相同结构和节点值的子树。如果存在，返回 true ；否则，返回 false 。

# 二叉树 tree 的一棵子树包括 tree 的某个节点和这个节点的所有后代节点。tree 也可以看做它自身的一棵子树。

# 示例 1：
# 输入：root = [3,4,5,1,2], subRoot = [4,1,2]
# 输出：true

# 示例 2：
# 输入：root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
# 输出：false
 

# 提示：
# root 树上的节点数量范围是 [1, 2000]
# subRoot 树上的节点数量范围是 [1, 1000]
# -10^4 <= root.val <= 10^4
# -10^4 <= subRoot.val <= 10^4

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
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(node: TreeNode) -> str:
            """
            深度优先遍历节点，得到一个序列
            """
            arr = [""] # 防止这样的测试用例过不了：root = [12], subRoot = [2]
            st = []
            while node or st:
                if node:
                    arr.append(str(node.val))
                    st.append(node)
                    node = node.left
                else:
                    arr.append("N")
                    node = st.pop()
                    node = node.right
            arr.append("N")

            return ",".join(arr)
        
        ser = dfs(root)
        subSer = dfs(subRoot)
        return ser.find(subSer) != -1

# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.isSubtree(TreeNode.createBFSTree([12]), TreeNode.createBFSTree([2]))) # False
    print(solution.isSubtree(TreeNode.createBFSTree([3,4,5,1,2]), TreeNode.createBFSTree([4,1,2]))) # True
    print(solution.isSubtree(TreeNode.createBFSTree([3,4,5,1,2]), TreeNode.createBFSTree([4,1]))) # False
    print(solution.isSubtree(TreeNode.createBFSTree([3,4,5,1,2,None,None,None,None,0]), TreeNode.createBFSTree([4,1,2]))) # False