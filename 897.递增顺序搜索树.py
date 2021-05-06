#
# @lc app=leetcode.cn id=897 lang=python3
#
# [897] 递增顺序搜索树
#
# 给你一棵二叉搜索树，请你 按中序遍历 将其重新排列为一棵递增顺序搜索树，使树中最左边的节点成为树的根节点，并且每个节点没有左子节点，只有一个右子节点。

# 示例 1：
# 输入：root = [5, 3, 6, 2, 4, null, 8, 1, null, null, null, 7, 9]
# 输出：[1, null, 2, null, 3, null, 4, null, 5, null, 6, null, 7, null, 8, null, 9]

# 示例 2：
# 输入：root = [5, 1, 7]
# 输出：[1, null, 5, null, 7]

# 提示：
# 树中节点数的取值范围是[1, 100]
# 0 <= Node.val <= 1000


from treenode import TreeNode
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return root

        stack = []
        queue = []
        # 非递归方式中序遍历
        node = root
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            if stack:
                node = stack.pop()
                queue.append(node)
                node = node.right

        # 重新组织树
        prevNode = None
        for node in queue:
            if prevNode:
                prevNode.left = None
                prevNode.right = node
            prevNode = node
        prevNode.left = prevNode.right = None
        return queue[0]
# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    print(solution.increasingBST(TreeNode.createBFSTree(
        [2, 1, 4, None, None, 3])).serialize())
    print(solution.increasingBST(TreeNode.createBFSTree(
        [5, 3, 6, 2, 4, None, 8, 1, None, None, None, 7, 9])).serialize())
    print(solution.increasingBST(TreeNode.createBFSTree(
        [5, 1, 7])).serialize())
