#
# @lc app=leetcode.cn id=1305 lang=python3
#
# [1305] 两棵二叉搜索树中的所有元素
#
# 给你 root1 和 root2 这两棵二叉搜索树。请你返回一个列表，其中包含 两棵树 中的所有整数并按 升序 排序。.


# 示例 1：
# 输入：root1 = [2, 1, 4], root2 = [1, 0, 3]
# 输出：[0, 1, 1, 2, 3, 4]

# 示例 2：
# 输入：root1 = [1, null, 8], root2 = [8, 1]
# 输出：[1, 1, 8, 8]


# 提示：
# 每棵树的节点数在[0, 5000] 范围内
# -10^5 <= Node.val <= 10^5


from treenode import TreeNode
from typing import List
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        # 中序遍历 + 归并排序
        def mid(node: TreeNode) -> List[int]:
            '''
            中序遍历
            '''
            res = []
            stack = []
            while node or stack:
                if node:
                    stack.append(node)
                    node = node.left
                else:
                    node = stack.pop()
                    res.append(node.val)
                    node = node.right
            return res

        def merge(list1: List[int], list2: List[int]) -> List[int]:
            '''
            归并排序
            '''
            i = j = 0
            m = len(list1)
            n = len(list2)
            res = []
            while i < m and j < n:
                if list1[i] < list2[j]:
                    res.append(list1[i])
                    i += 1
                elif list1[i] > list2[j]:
                    res.append(list2[j])
                    j += 1
                else:
                    res.append(list1[i])
                    res.append(list2[j])
                    i += 1
                    j += 1
            if i < m:
                res.extend(list1[i:])
            elif j < n:
                res.extend(list2[j:])

            return res

        return merge(mid(root1), mid(root2))

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.getAllElements(TreeNode.createBFSTree(
        [2, 1, 4]), TreeNode.createBFSTree([1, 0, 3])))  # [0, 1, 1, 2, 3, 4]
