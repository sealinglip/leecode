#
# @lc app=leetcode.cn id=1782 lang=python3
#
# [1782] 统计点对的数目
#
# 给你一个无向图，无向图由整数 n  ，表示图中节点的数目，和 edges 组成，其中 edges[i] = [ui, vi] 表示 ui 和 vi 之间有一条无向边。同时给你一个代表查询的整数数组 queries 。

# 第 j 个查询的答案是满足如下条件的点对(a, b) 的数目：

# a < b
# cnt 是与 a 或者 b 相连的边的数目，且 cnt 严格大于 queries[j] 。
# 请你返回一个数组 answers ，其中 answers.length == queries.length 且 answers[j] 是第 j 个查询的答案。

# 请注意，图中可能会有 重复边 。


# 示例 1：
# 输入：n = 4, edges = [[1, 2], [2, 4], [1, 3], [2, 3], [2, 1]], queries = [2, 3]
# 输出：[6, 5]
# 解释：每个点对中，与至少一个点相连的边的数目如上图所示。

# 示例 2：
# 输入：n = 5, edges = [[1, 5], [1, 5], [3, 4], [2, 5], [1, 3], [5, 1], [2, 3], [2, 5]], queries = [1, 2, 3, 4, 5]
# 输出：[10, 10, 9, 8, 6]


# 提示：
# 2 <= n <= 2 * 10^4
# 1 <= edges.length <= 10^5
# 1 <= ui, vi <= n
# ui != vi
# 1 <= queries.length <= 20
# 0 <= queries[j] < edges.length

# Hard
# 复习

from bisect import bisect_right
from collections import defaultdict
from typing import List
# @lc code=start


class Solution:
    def countPairs(self, n: int, edges: List[List[int]], queries: List[int]) -> List[int]:
        pathes = defaultdict(int)  # 记录每个节点的边数
        cnt = defaultdict(int)  # 记录两个节点之间的边数
        for u, v in edges:
            if u > v:
                u, v = v, u
            pathes[u] += 1
            pathes[v] += 1
            cnt[(u, v)] += 1

        # 按每节点边数建列表排序并补没边的节点
        pathCount = [0] * (n - len(pathes)) + sorted(pathes.values())

        res = []
        for q in queries:
            ans = 0
            for i in range(n):
                j = bisect_right(pathCount, q - pathCount[i], i+1)
                ans += n - j
            # 去掉重复计算了共用边的情况
            for (u, v), c in cnt.items():
                if pathes[u] + pathes[v] > q and pathes[u] + pathes[v] - c <= q:
                    ans -= 1
            res.append(ans)

        return res


        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.countPairs(
        5, [[4, 5], [1, 3], [1, 4]], [0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 2]))  # [10,8,10,10,8,8,10,10,10,10,8,10,10,8,10,8,8,3]
    print(solution.countPairs(
        4, [[1, 2], [2, 4], [1, 3], [2, 3], [2, 1]], [2, 3]))  # [6,5]
    print(solution.countPairs(5, [[1, 5], [1, 5], [3, 4], [2, 5], [
          1, 3], [5, 1], [2, 3], [2, 5]], [1, 2, 3, 4, 5]))  # [10,10,9,8,6]
