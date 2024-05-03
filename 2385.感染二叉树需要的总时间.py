#
# @lc app=leetcode.cn id=2385 lang=python3
#
# [2385] 感染二叉树需要的总时间
#
# 给你一棵二叉树的根节点 root ，二叉树中节点的值 互不相同 。另给你一个整数 start 。在第 0 分钟，感染 将会从值为 start 的节点开始爆发。

# 每分钟，如果节点满足以下全部条件，就会被感染：

# 节点此前还没有感染。
# 节点与一个已感染节点相邻。
# 返回感染整棵树需要的分钟数。


# 示例 1：
# 输入：root = [1,5,3,null,4,10,6,9,2], start = 3
# 输出：4
# 解释：节点按以下过程被感染：
# - 第 0 分钟：节点 3
# - 第 1 分钟：节点 1、10、6
# - 第 2 分钟：节点5
# - 第 3 分钟：节点 4
# - 第 4 分钟：节点 9 和 2
# 感染整棵树需要 4 分钟，所以返回 4 。

# 示例 2：
# 输入：root = [1], start = 1
# 输出：0
# 解释：第 0 分钟，树中唯一一个节点处于感染状态，返回 0 。
 

# 提示：
# 树中节点的数目在范围 [1, 10^5] 内
# 1 <= Node.val <= 10^5
# 每个节点的值 互不相同
# 树中必定存在值为 start 的节点

# 复习

from collections import defaultdict
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
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        # 方法1：效率更高，不太简捷
        # 记录start节点及其所有父节点本身的level和除start外的子树的深度
        state = {}
        st = []
        def dfs(node: TreeNode, level: int, underStart: bool) -> int:
            if not underStart and node.val == start:
                for n in st:
                    state[n.val] = None
                state[start] = None
                underStart = True
            depth = level
            st.append(node)
            if node.left:
                d = dfs(node.left, level+1, underStart)
                if node.left.val not in state:
                    depth = max(depth, d)
            if node.right:
                d = dfs(node.right, level+1, underStart)
                if node.right.val not in state:
                    depth = max(depth, d)
            st.pop()
            if node.val in state:
                state[node.val] = [level, depth]
            return depth if node.val != start else 0
        
        dfs(root, 0, False)

        startLevel, startDepth = state.pop(start)
        res = startDepth - startLevel
        for nl, nd in state.values():
            res = max(res, startLevel - (nl << 1) + nd)

        return res
    
        # 方法2：
        # 将树变成图，遍历求最大深度
        # graph = defaultdict(list)
        # def dfs(node: TreeNode) -> None:
        #     if node.left:
        #         graph[node.val].append(node.left.val)
        #         graph[node.left.val].append(node.val)
        #         dfs(node.left)
        #     if node.right:
        #         graph[node.val].append(node.right.val)
        #         graph[node.right.val].append(node.val)
        #         dfs(node.right)
        # dfs(root)

        # visited = set()
        # def dfsGraph(n: int, distance: int) -> int:
        #     visited.add(n)
        #     d = distance
        #     for v in graph[n]:
        #         if v not in visited:
        #             d = max(d, dfsGraph(v, distance+1))
        #     return d
        
        # return dfsGraph(start, 0)

# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    # print(solution.amountOfTime(TreeNode.createBFSTree([1,5,3,None,4,10,6,9,2]), 3)) # 4
    print(solution.amountOfTime(TreeNode.createBFSTree([1,5,3,None,4,10,6,9,2]), 9)) # 5
    print(solution.amountOfTime(TreeNode.createBFSTree([1]), 1)) # 0