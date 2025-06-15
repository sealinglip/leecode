#
# @lc app=leetcode.cn id=3372 lang=python3
#
# [3372] 连接两棵树后最大目标节点数目 I
#
# https://leetcode.cn/problems/maximize-the-number-of-target-nodes-after-connecting-trees-i/description/
#
# algorithms
# Medium (50.76%)
# Likes:    13
# Dislikes: 0
# Total Accepted:    3.5K
# Total Submissions: 6.1K
# Testcase Example:  '[[0,1],[0,2],[2,3],[2,4]]\n[[0,1],[0,2],[0,3],[2,7],[1,4],[4,5],[4,6]]\n2'
#
# 有两棵 无向 树，分别有 n 和 m 个树节点。两棵树中的节点编号分别为[0, n - 1] 和 [0, m - 1] 中的整数。
# 
# 给你两个二维整数 edges1 和 edges2 ，长度分别为 n - 1 和 m - 1 ，其中 edges1[i] = [ai, bi]
# 表示第一棵树中节点 ai 和 bi 之间有一条边，edges2[i] = [ui, vi] 表示第二棵树中节点 ui 和 vi
# 之间有一条边。同时给你一个整数 k 。
# 
# 如果节点 u 和节点 v 之间路径的边数小于等于 k ，那么我们称节点 u 是节点 v 的 目标节点 。注意 ，一个节点一定是它自己的 目标节点 。
# 
# 请你返回一个长度为 n 的整数数组 answer ，answer[i] 表示将第一棵树中的一个节点与第二棵树中的一个节点连接一条边后，第一棵树中节点 i
# 的 目标节点 数目的 最大值 。
# 
# 注意 ，每个查询相互独立。意味着进行下一次查询之前，你需要先把刚添加的边给删掉。
# 
# 
# 示例 1：
# 输入：edges1 = [[0,1],[0,2],[2,3],[2,4]], edges2 =
# [[0,1],[0,2],[0,3],[2,7],[1,4],[4,5],[4,6]], k = 2
# 输出：[9,7,9,8,8]
# 解释：
# 对于 i = 0 ，连接第一棵树中的节点 0 和第二棵树中的节点 0 。
# 对于 i = 1 ，连接第一棵树中的节点 1 和第二棵树中的节点 0 。
# 对于 i = 2 ，连接第一棵树中的节点 2 和第二棵树中的节点 4 。
# 对于 i = 3 ，连接第一棵树中的节点 3 和第二棵树中的节点 4 。
# 对于 i = 4 ，连接第一棵树中的节点 4 和第二棵树中的节点 4 。
# 
# 示例 2：
# 输入：edges1 = [[0,1],[0,2],[0,3],[0,4]], edges2 = [[0,1],[1,2],[2,3]], k = 1
# 输出：[6,3,3,3,3]
# 解释：
# 对于每个 i ，连接第一棵树中的节点 i 和第二棵树中的任意一个节点。
# 
# 
# 提示：
# 2 <= n, m <= 1000
# edges1.length == n - 1
# edges2.length == m - 1
# edges1[i].length == edges2[i].length == 2
# edges1[i] = [ai, bi]
# 0 <= ai, bi < n
# edges2[i] = [ui, vi]
# 0 <= ui, vi < m
# 输入保证 edges1 和 edges2 都表示合法的树。
# 0 <= k <= 1000
# 
#

from typing import Dict, List
from collections import defaultdict
# @lc code=start
class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        def dfs(graph: Dict[int, List[int]], u: int, p: int, k: int) -> int:
            res = int(k >= 0) # 自身
            if k > 0:
                for v in graph[u]:
                    if v == p:
                        continue
                    res += dfs(graph, v, u, k-1)
            return res

        def traverse(edges: List[List[int]], k: int) -> List[int]:
            '''
            根据边构建树，遍历树节点，返回以每个节点的距离为k的目标节点数
            '''
            # 构建邻接表
            graph = defaultdict(list)
            for u, v in edges:
                graph[u].append(v)
                graph[v].append(u)
            res = []
            for i in range(len(edges)+1):
                res.append(dfs(graph, i, -1, k))

            return res

        # 先求出tree2中哪个节点有 对应 k-1 的最大目标节点数
        ma2 = max(traverse(edges2, k-1))
        r1 = traverse(edges1, k)
        return [r + ma2 for r in r1]
        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.maxTargetNodes([[0,1]], [[0,1]], 0)) # [1,1]
    print(solution.maxTargetNodes([[0,1],[0,2],[2,3],[2,4]], [[0,1],[0,2],[0,3],[2,7],[1,4],[4,5],[4,6]], 2)) # [9,7,9,8,8]
    print(solution.maxTargetNodes([[0,1],[0,2],[0,3],[0,4]], [[0,1],[1,2],[2,3]], 1)) # [6,3,3,3,3]
