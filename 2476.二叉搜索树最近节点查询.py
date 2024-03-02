#
# @lc app=leetcode.cn id=2476 lang=python3
#
# [2476] 二叉搜索树最近节点查询
#
# 给你一个 二叉搜索树 的根节点 root ，和一个由正整数组成、长度为 n 的数组 queries 。

# 请你找出一个长度为 n 的 二维 答案数组 answer ，其中 answer[i] = [mini, maxi] ：

# mini 是树中小于等于 queries[i] 的 最大值 。如果不存在这样的值，则使用 -1 代替。
# maxi 是树中大于等于 queries[i] 的 最小值 。如果不存在这样的值，则使用 -1 代替。
# 返回数组 answer 。


# 示例 1 ：
# 输入：root = [6,2,13,1,4,9,15,None,None,None,None,None,None,14], queries = [2,5,16]
# 输出：[[2,2],[4,6],[15,-1]]
# 解释：按下面的描述找出并返回查询的答案：
# - 树中小于等于 2 的最大值是 2 ，且大于等于 2 的最小值也是 2 。所以第一个查询的答案是 [2,2] 。
# - 树中小于等于 5 的最大值是 4 ，且大于等于 5 的最小值是 6 。所以第二个查询的答案是 [4,6] 。
# - 树中小于等于 16 的最大值是 15 ，且大于等于 16 的最小值不存在。所以第三个查询的答案是 [15,-1] 。

# 示例 2 ：
# 输入：root = [4,None,9], queries = [3]
# 输出：[[-1,4]]
# 解释：树中不存在小于等于 3 的最大值，且大于等于 3 的最小值是 4 。所以查询的答案是 [-1,4] 。
 

# 提示：
# 树中节点的数目在范围 [2, 10^5] 内
# 1 <= Node.val <= 10^6
# n == queries.length
# 1 <= n <= 10^5
# 1 <= queries[i] <= 10^6

# 复习

from bisect import bisect_left
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
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        # 下面的解法会TLE，测试用例会用一颗极不平衡的二叉树来测试
        # def search(val: int) -> List[int]:
        #     mi = ma = -1
        #     node = root
        #     while node:
        #         if node.val == val:
        #             mi = ma = val
        #             break
        #         elif node.val > val:
        #             ma = node.val
        #             node = node.left
        #         else:
        #             mi = node.val
        #             node = node.right                

        #     return [mi, ma]
        
        # return [search(val) for val in queries]
        inorder = [] # 中序遍历
        def dfs(node: TreeNode):
            if node:
                dfs(node.left)
                inorder.append(node.val)
                dfs(node.right)
        dfs(root)

        res = []
        for val in queries:
            mi = ma = -1
            idx = bisect_left(inorder, val)
            if idx != len(inorder):
                ma = inorder[idx]
                if ma == val:
                    mi = val
                    res.append([mi, ma])
                    continue
            if idx != 0:
                mi = inorder[idx - 1]
            res.append([mi, ma])
            
        return res
            

# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.closestNodes(TreeNode.createBFSTree([6,2,13,1,4,9,15,None,None,None,None,None,None,14]), [2,5,16])) # [[2,2],[4,6],[15,-1]]
    print(solution.closestNodes(TreeNode.createBFSTree([4,None,9]), [3])) # [[-1,4]]