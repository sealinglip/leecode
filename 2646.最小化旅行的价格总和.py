#
# @lc app=leetcode.cn id=2646 lang=python3
#
# [2646] 最小化旅行的价格总和
#
# 现有一棵无向、无根的树，树中有 n 个节点，按从 0 到 n - 1 编号。给你一个整数 n 和一个长度为 n - 1 的二维整数数组 edges ，
# 其中 edges[i] = [ai, bi] 表示树中节点 ai 和 bi 之间存在一条边。

# 每个节点都关联一个价格。给你一个整数数组 price ，其中 price[i] 是第 i 个节点的价格。
# 给定路径的 价格总和 是该路径上所有节点的价格之和。

# 另给你一个二维整数数组 trips ，其中 trips[i] = [starti, endi] 表示您从节点 starti 开始第 i 次旅行，并通过任何你喜欢的路径前往节点 endi 。
# 在执行第一次旅行之前，你可以选择一些 非相邻节点 并将价格减半。
# 返回执行所有旅行的最小价格总和。


# 示例 1：
# 输入：n = 4, edges = [[0,1],[1,2],[1,3]], price = [2,2,10,6], trips = [[0,3],[2,1],[2,3]]
# 输出：23
# 解释：
# 上图表示将节点 2 视为根之后的树结构。第一个图表示初始树，第二个图表示选择节点 0 、2 和 3 并使其价格减半后的树。
# 第 1 次旅行，选择路径 [0,1,3] 。路径的价格总和为 1 + 2 + 3 = 6 。
# 第 2 次旅行，选择路径 [2,1] 。路径的价格总和为 2 + 5 = 7 。
# 第 3 次旅行，选择路径 [2,1,3] 。路径的价格总和为 5 + 2 + 3 = 10 。
# 所有旅行的价格总和为 6 + 7 + 10 = 23 。可以证明，23 是可以实现的最小答案。

# 示例 2：
# 输入：n = 2, edges = [[0,1]], price = [2,2], trips = [[0,0]]
# 输出：1
# 解释：
# 上图表示将节点 0 视为根之后的树结构。第一个图表示初始树，第二个图表示选择节点 0 并使其价格减半后的树。 
# 第 1 次旅行，选择路径 [0] 。路径的价格总和为 1 。 
# 所有旅行的价格总和为 1 。可以证明，1 是可以实现的最小答案。
 
# 提示：
# 1 <= n <= 50
# edges.length == n - 1
# 0 <= ai, bi <= n - 1
# edges 表示一棵有效的树
# price.length == n
# price[i] 是一个偶数
# 1 <= price[i] <= 1000
# 1 <= trips.length <= 100
# 0 <= starti, endi <= n - 1

# Hard
# 复习

from collections import defaultdict
from functools import cache
from typing import List
# @lc code=start
class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        paths = defaultdict(list)
        for u, v in edges:
            paths[u].append(v)
            paths[v].append(u)

        visitedCnt = [0] * n
        visitedFlag = [False] * n
        
        def bfs(start: int, end: int) -> bool:
            if start == end:
                visitedCnt[end] += 1
                return True
            
            visitedFlag[start] = True
            canReach = False
            for n in paths[start]:
                if not visitedFlag[n]:
                    if bfs(n, end):
                        canReach = True
                        break
            visitedFlag[start] = False
            if canReach:
                visitedCnt[start] += 1
            return canReach

        # 统计每个城市到访的次数
        for s, e in trips:
            bfs(s, e)

        total = sum(visitedCnt[i] * price[i] for i in range(n) if visitedCnt[i] > 0) # 不减半时的花费
        # 现在来规划哪些城市的价格减半
        # 某个城市减半，与之相邻的就不能减半
        @cache
        def dfs(node: int, discount: bool) -> int:
            '''
            node: 某城市
            discount: 本市是否打折
            返回，此时其所有子（含自己）打折收益的最大值
            '''
            visitedFlag[node] = True
            saving = 0
            if discount:
                saving += visitedCnt[node] * (price[node] >> 1) # 本市节约金额
                for n in paths[node]:
                    if (not visitedFlag[n]): # 当下未处理过
                        saving += dfs(n, False) # 本市打折，相邻市就不能打折了
            else:
                for n in paths[node]:
                    # if (not visitedFlag[n]) and visitedCnt[n]: # 有到访且当下未处理过
                    if (not visitedFlag[n]): # 当下未处理过
                        saving += max(dfs(n, False), dfs(n, True))

            visitedFlag[node] = False
            print("n: %d, d: %r: s: %d" % (node, discount, saving))
            return saving

        # 本意是随便从路径中选一个节点当成根遍历，遍历过程中，只考虑有到访的节点，但这样下面的第一个用例过不了
        # 原因是：随意选一个点作为根，只遍历到访的节点，那么只有当所有到访节点形成一个连通集时，遍历才完整，如果是多个连通集，那么有的到访点不会被遍历
        saving = max(dfs(trips[0][0], True), dfs(trips[0][0], False))
        return total - saving

# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.minimumTotalPrice(42, 
                                     [[3,24],[6,2],[2,23],[7,35],[12,28],[13,20],[15,21],[20,5],[23,18],[18,33],[27,9],[28,8],[8,4],[4,22],[22,21],[21,10],[10,0],[0,9],[31,30],[30,33],[32,16],[16,39],[34,35],[35,26],[26,33],[36,33],[37,40],[38,33],[33,24],[24,19],[19,25],[25,29],[29,14],[14,5],[39,17],[17,1],[1,9],[9,11],[40,11],[11,5],[5,41]], 
                                     [34,34,8,44,26,8,44,38,4,26,6,2,20,10,8,8,38,38,12,22,16,14,28,16,28,20,22,32,14,8,42,20,42,36,14,38,24,4,2,20,36,2], [[35,35],[36,3],[8,2]])) # 335
    print(solution.minimumTotalPrice(4, [[0,1],[1,2],[1,3]], [2,2,10,6], [[0,3],[2,1],[2,3]])) # 23
    print(solution.minimumTotalPrice(2, [[0,1]], [2,2], [[0,0]])) # 1