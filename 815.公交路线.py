#
# @lc app=leetcode.cn id=815 lang=python3
#
# [815] 公交路线
#
# 给你一个数组 routes ，表示一系列公交线路，其中每个 routes[i] 表示一条公交线路，第 i 辆公交车将会在上面循环行驶。
# 例如，路线 routes[0] = [1, 5, 7] 表示第 0 辆公交车会一直按序列 1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ... 这样的车站路线行驶。
# 现在从 source 车站出发（初始时不在公交车上），要前往 target 车站。 期间仅可乘坐公交车。
# 求出 最少乘坐的公交车数量 。如果不可能到达终点车站，返回 - 1 。

# 示例 1：
# 输入：routes = [[1, 2, 7], [3, 6, 7]], source = 1, target = 6
# 输出：2
# 解释：最优策略是先乘坐第一辆公交车到达车站 7, 然后换乘第二辆公交车到车站 6 。

# 示例 2：
# 输入：routes = [[7, 12], [4, 5, 15], [6], [15, 19], [9, 12, 13]], source = 15, target = 12
# 输出：- 1

# 提示：
# 1 <= routes.length <= 500.
# 1 <= routes[i].length <= 10 ^ 5
# routes[i] 中的所有值 互不相同
# sum(routes[i].length) <= 10 ^ 5
# 0 <= routes[i][j] < 10 ^ 6
# 0 <= source, target < 10 ^ 6

from typing import List
from collections import deque, defaultdict
# @lc code=start


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        # 重新处理路线
        rList = defaultdict(list)
        for i, r in enumerate(routes):
            for s in r:
                rList[s].append(i)

        if source == target:
            return 0 if len(rList[source]) > 0 else -1
        q = deque([(i, 1) for i in rList[source]])  # 初始化尝试队列
        tried = set(rList[source])  # 记录尝试过的线路
        # BFS
        while q:
            i, cnt = q.popleft()
            for s in routes[i]:
                if s == target:
                    return cnt
                else:
                    rs = [r for r in rList.get(s) if r not in tried]
                    for r in rs:
                        tried.add(r)
                        q.append((r, cnt + 1))

        return -1

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.numBusesToDestination([[1, 7], [3, 5]], 5, 5))
    print(solution.numBusesToDestination([[1, 2, 7], [3, 6, 7]], 1, 6))
    print(solution.numBusesToDestination(
        [[7, 12], [4, 5, 15], [6], [15, 19], [9, 12, 13]], 15, 12))
