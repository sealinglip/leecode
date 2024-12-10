# 给你一个整数 n 和一个二维整数数组 queries。
# 有 n 个城市，编号从 0 到 n - 1。初始时，每个城市 i 都有一条单向道路通往城市 i + 1（ 0 <= i < n - 1）。
# queries[i] = [ui, vi] 表示新建一条从城市 ui 到城市 vi 的单向道路。每次查询后，你需要找到从城市 0 到城市 n - 1 的最短路径的长度。
# 所有查询中不会存在两个查询都满足 queries[i][0] < queries[j][0] < queries[i][1] < queries[j][1]。
# 返回一个数组 answer，对于范围 [0, queries.length - 1] 中的每个 i，answer[i] 是处理完前 i + 1 个查询后，从城市 0 到城市 n - 1 的最短路径的长度。


# 示例 1：
# 输入： n = 5, queries = [[2, 4], [0, 2], [0, 4]]
# 输出： [3, 2, 1]
# 解释：
# 新增一条从 2 到 4 的道路后，从 0 到 4 的最短路径长度为 3。
# 新增一条从 0 到 2 的道路后，从 0 到 4 的最短路径长度为 2。
# 新增一条从 0 到 4 的道路后，从 0 到 4 的最短路径长度为 1。


# 示例 2：
# 输入： n = 4, queries = [[0, 3], [0, 2]]
# 输出： [1, 1]
# 解释：
# 新增一条从 0 到 3 的道路后，从 0 到 3 的最短路径长度为 1。
# 新增一条从 0 到 2 的道路后，从 0 到 3 的最短路径长度仍为 1。


# 提示:
# 3 <= n <= 10^5
# 1 <= queries.length <= 10^5
# queries[i].length == 2
# 0 <= queries[i][0] < queries[i][1] < n
# 1 < queries[i][1] - queries[i][0]
# 查询中不存在重复的道路。
# 不存在两个查询都满足 i != j 且 queries[i][0] < queries[j][0] < queries[i][1] < queries[j][1]。
# Hard

from typing import List

class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        # 本题和3243相比，增加了条件就是任意两条道路要么不相交，要么是包含关系，不存在交错。
        # 有了跨度更大的路径，被它包含的其他路径都不用考虑
        next = [i+1 for i in range(n)] # next[i] 表示第i个城市通往的最远的城市，如果next[i] == 0 表示它已经被快捷路径跳过了

        res = []
        dist = n - 1 # 初始 0 ~ n 的距离
        for u, v in queries:
            k = next[u]
            if v > k:
                next[u] = v
                while k > 0 and k < v:
                    next[k], k = 0, next[k]
                    dist -= 1
            res.append(dist)

        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.shortestDistanceAfterQueries(10, [[1, 9], [2, 7], [2, 4], [2, 5]])) # [2, 2, 2, 1]
    print(solution.shortestDistanceAfterQueries(5, [[2, 4], [0, 2], [0, 4]])) # [3, 2, 1]
    print(solution.shortestDistanceAfterQueries(4, [[0, 3], [0, 2]])) # [1, 1]
