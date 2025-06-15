#
# @lc app=leetcode.cn id=1857 lang=python3
#
# [1857] 有向图中最大颜色值
#
# https://leetcode.cn/problems/largest-color-value-in-a-directed-graph/description/
#
# algorithms
# Hard (49.98%)
# Likes:    79
# Dislikes: 0
# Total Accepted:    7.2K
# Total Submissions: 13.8K
# Testcase Example:  '"abaca"\n[[0,1],[0,2],[2,3],[3,4]]'
#
# 给你一个 有向图 ，它含有 n 个节点和 m 条边。节点编号从 0 到 n - 1 。
# 
# 给你一个字符串 colors ，其中 colors[i] 是小写英文字母，表示图中第 i 个节点的 颜色 （下标从 0 开始）。同时给你一个二维数组
# edges ，其中 edges[j] = [aj, bj] 表示从节点 aj 到节点 bj 有一条 有向边 。
# 
# 图中一条有效 路径 是一个点序列 x1 -> x2 -> x3 -> ... -> xk ，对于所有 1 <= i < k ，从 xi 到 xi+1
# 在图中有一条有向边。路径的 颜色值 是路径中 出现次数最多 颜色的节点数目。
# 
# 请你返回给定图中有效路径里面的 最大颜色值 。如果图中含有环，请返回 -1 。
# 
# 
# 示例 1：
# 输入：colors = "abaca", edges = [[0,1],[0,2],[2,3],[3,4]]
# 输出：3
# 解释：路径 0 -> 2 -> 3 -> 4 含有 3 个颜色为 "a" 的节点（上图中的红色节点）。
# 
# 示例 2：
# 输入：colors = "a", edges = [[0,0]]
# 输出：-1
# 解释：从 0 到 0 有一个环。
# 
# 
# 提示：
# n == colors.length
# m == edges.length
# 1 <= n <= 10^5
# 0 <= m <= 10^5
# colors 只含有小写英文字母。
# 0 <= aj, bj < n
#
# 复习

from collections import defaultdict, deque
from typing import List
# @lc code=start
class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        colorBase = ord('a')
        # 构建邻接表
        graph = defaultdict(list)
        indegree = [0] * n # 入度
        for x, y in edges:
            indegree[y] += 1
            graph[x].append(y)

        # 拓扑排序 + 动态规划
        visited = 0 # 记录访问节点数
        q = deque()
        dp = [[0] * 26 for _ in range(n)] # 记dp[i][j] 为以i为终点所有路径中，color为j的节点数量最大值
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)

        leaves = set()
        while q:
            node = q.popleft()
            visited += 1
            dp[node][ord(colors[node]) - colorBase] += 1
            if graph[node]:
                for v in graph[node]:
                    indegree[v] -= 1
                    if indegree[v] == 0:
                        q.append(v)
                    for c in range(26):
                        dp[v][c] = max(dp[v][c], dp[node][c])
            else:
                leaves.add(node)

        if visited != n:
            # 有环
            return -1
        
        res = 0
        # 只需要判断叶子节点
        for i in leaves:
            res = max(res, max(dp[i]))
        return res
        

# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.largestPathValue("abaca", [[0,1],[0,2],[2,3],[3,4]])) # 3
    print(solution.largestPathValue("a", [[0,0]])) # -1
