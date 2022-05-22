# 设计一个算法，找出二叉搜索树中指定节点的“下一个”节点（也即中序后继）。
# 如果指定节点没有对应的“下一个”节点，则返回null。

# 示例 1:
# 输入: root = [2, 1, 3], p = 1
#   2
#  / \
# 1   3
# 输出: 2

# 示例 2:
# 输入: root = [5,3,6,2,4,None,None,1], p = 6
#       5
#      / \
#     3   6
#    / \
#   2   4
#  /
# 1
# 输出: None

from treenode import TreeNode


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        if root is None:
            return None
        # 找该节点，如果找到，找其右子节点，如果有，再一直找左子节点到头，即为答案
        #                  如果没有右子节点，如果自身是父的右，返None；否则找父返回
        # 如果没找到本节点，
        node = root
        stack = []
        while node:
            stack.append(node)
            if node.val < p.val:
                if node.right:
                    node = node.right
                    continue
            elif node.val > p.val:
                if node.left:
                    node = node.left
                    continue
            break

        if node.val <= p.val:
            if node.right:
                node = node.right
                while node.left:
                    node = node.left
                return node
            else:
                while stack:
                    node = stack.pop()
                    if node.val > p.val:
                        break
                return node if node.val > p.val else None
        else:
            return node


if __name__ == "__main__":
    solution = Solution()
    root = TreeNode.createBFSTree([2, 1, 3])
    print(solution.inorderSuccessor(root, TreeNode(1)))  # TreeNode(2)
    print(solution.inorderSuccessor(root, TreeNode(2)))  # TreeNode(3)
    print(solution.inorderSuccessor(root, TreeNode(3)))  # None

    root = TreeNode.createBFSTree([5, 3, 6, 2, 4, None, None, 1])
    print(solution.inorderSuccessor(root, TreeNode(1)))  # TreeNode(2)
    print(solution.inorderSuccessor(root, TreeNode(2)))  # TreeNode(3)
    print(solution.inorderSuccessor(root, TreeNode(3)))  # TreeNode(4)
    print(solution.inorderSuccessor(root, TreeNode(4)))  # TreeNode(5)
    print(solution.inorderSuccessor(root, TreeNode(4.5)))  # TreeNode(5)
    print(solution.inorderSuccessor(root, TreeNode(5)))  # TreeNode(6)
    print(solution.inorderSuccessor(root, TreeNode(6)))  # None
