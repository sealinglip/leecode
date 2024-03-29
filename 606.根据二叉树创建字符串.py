#
# @lc app=leetcode.cn id=606 lang=python3
#
# [606] 根据二叉树创建字符串
#
# 你需要采用前序遍历的方式，将一个二叉树转换成一个由括号和整数组成的字符串。

# 空节点则用一对空括号 "()" 表示。而且你需要省略所有不影响字符串与原始二叉树之间的一对一映射关系的空括号对。

# 示例 1:
# 输入: 二叉树: [1, 2, 3, 4]
#        1
#      /   \
#     2     3
#    /
#   4

# 输出: "1(2(4))(3)"

# 解释: 原本将是“1(2(4)())(3())”，
# 在你省略所有不必要的空括号对之后，
# 它将是“1(2(4))(3)”。

# 示例 2:
# 输入: 二叉树: [1,2,3,null,4]
#        1
#      /   \
#     2     3
#      \
#       4

# 输出: "1(2()(4))(3)"

# 解释: 和第一个示例相似，
# 除了我们不能省略第一个对括号来中断输入和输出之间的一对一映射关系。


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
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return "()"
        output = []
        stack = [root]
        while stack:
            ele = stack.pop()
            if isinstance(ele, str):
                output.append(ele)
            else:
                node = ele
                output.append(str(node.val))
                if node.left is None and node.right:
                    output.append("()")
                if node.right:
                    stack.append(")")
                    stack.append(node.right)
                    stack.append("(")
                if node.left:
                    stack.append(")")
                    stack.append(node.left)
                    stack.append("(")

        return "".join(output)


# @lc code=end
if __name__ == "__main__":
    solution = Solution()
    # "1(2(4))(3)"
    print(solution.tree2str(TreeNode.createBFSTree([1, 2, 3, 4])))
    print(solution.tree2str(TreeNode.createBFSTree(
        [1, 2, 3, None, 4])))  # "1(2()(4))(3)"
