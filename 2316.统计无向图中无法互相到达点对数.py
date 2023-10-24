#
# @lc app=leetcode.cn id=2316 lang=python3
#
# [2316] 统计无向图中无法互相到达点对数
#
# 给你一个整数 n ，表示一张 无向图 中有 n 个节点，编号为 0 到 n - 1 。同时给你一个二维整数数组 edges ，其中 edges[i] = [ai, bi] 表示节点 ai 和 bi 之间有一条 无向 边。
# 请你返回 无法互相到达 的不同 点对数目 。


# 示例 1：
# 输入：n = 3, edges = [[0, 1], [0, 2], [1, 2]]
# 输出：0
# 解释：所有点都能互相到达，意味着没有点对无法互相到达，所以我们返回 0 。

# 示例 2：
# 输入：n = 7, edges = [[0, 2], [0, 5], [2, 4], [1, 6], [5, 4]]
# 输出：14
# 解释：总共有 14 个点对互相无法到达：
# [[0, 1], [0, 3], [0, 6], [1, 2], [1, 3], [1, 4], [1, 5], [
#     2, 3], [2, 6], [3, 4], [3, 5], [3, 6], [4, 6], [5, 6]]
# 所以我们返回 14 。

# 提示：
# 1 <= n <= 10^5
# 0 <= edges.length <= 2 * 10^5
# edges[i].length == 2
# 0 <= ai, bi < n
# ai != bi
# 不会有重复边。

from collections import Counter
from typing import List

# @lc code=start


class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        # 并查集
        uf = list(range(n))

        def find(x: int) -> int:
            if uf[x] != x:
                uf[x] = find(uf[x])
            return uf[x]

        def union(x: int, y: int) -> None:
            uf[find(x)] = find(y)

        for x, y in edges:
            if find(x) != find(y):
                union(x, y)

        res = 0
        accum = 0
        for _, v in Counter([find(i) for i in range(n)]).items():
            res += accum * v
            accum += v

        return res


        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.countPairs(3, [[0, 1], [0, 2], [1, 2]]))  # 0
    print(solution.countPairs(
        7, [[0, 2], [0, 5], [2, 4], [1, 6], [5, 4]]))  # 14
