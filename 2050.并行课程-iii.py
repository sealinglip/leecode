#
# @lc app=leetcode.cn id=2050 lang=python3
#
# [2050] 并行课程 III
#
# 给你一个整数 n ，表示有 n 节课，课程编号从 1 到 n 。同时给你一个二维整数数组 relations ，其中 relations[j] = [prevCoursej, nextCoursej] ，表示课程 prevCoursej 必须在课程 nextCoursej 之前 完成（先修课的关系）。同时给你一个下标从 0 开始的整数数组 time ，其中 time[i] 表示完成第(i+1) 门课程需要花费的 月份 数。

# 请你根据以下规则算出完成所有课程所需要的 最少 月份数：

# 如果一门课的所有先修课都已经完成，你可以在 任意 时间开始这门课程。
# 你可以 同时 上 任意门课程 。
# 请你返回完成所有课程所需要的 最少 月份数。

# 注意：测试数据保证一定可以完成所有课程（也就是先修课的关系构成一个有向无环图）。


# 示例 1:
# 输入：n = 3, relations = [[1, 3], [2, 3]], time = [3, 2, 5]
# 输出：8
# 解释：上图展示了输入数据所表示的先修关系图，以及完成每门课程需要花费的时间。
# 你可以在月份 0 同时开始课程 1 和 2 。
# 课程 1 花费 3 个月，课程 2 花费 2 个月。
# 所以，最早开始课程 3 的时间是月份 3 ，完成所有课程所需时间为 3 + 5 = 8 个月。

# 示例 2：
# 输入：n = 5, relations = [[1, 5], [2, 5], [3, 5], [3, 4], [4, 5]], time = [1, 2, 3, 4, 5]
# 输出：12
# 解释：上图展示了输入数据所表示的先修关系图，以及完成每门课程需要花费的时间。
# 你可以在月份 0 同时开始课程 1 ，2 和 3 。
# 在月份 1，2 和 3 分别完成这三门课程。
# 课程 4 需在课程 3 之后开始，也就是 3 个月后。课程 4 在 3 + 4 = 7 月完成。
# 课程 5 需在课程 1，2，3 和 4 之后开始，也就是在 max(1, 2, 3, 7) = 7 月开始。
# 所以完成所有课程所需的最少时间为 7 + 5 = 12 个月。


# 提示：
# 1 <= n <= 5 * 10^4
# 0 <= relations.length <= min(n * (n - 1) / 2, 5 * 10^4)
# relations[j].length == 2
# 1 <= prevCoursej, nextCoursej <= n
# prevCoursej != nextCoursej
# 所有的先修课程对[prevCoursej, nextCoursej] 都是 互不相同 的。
# time.length == n
# 1 <= time[i] <= 10^4
# 先修课程图是一个有向无环图。

from collections import defaultdict
from typing import List
import heapq
# @lc code=start


class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        # 维护依赖关系、入度
        follow = defaultdict(list)
        in_degree = [0] * n
        for c1, c2 in relations:
            # 统一搞成0开始
            c1 -= 1
            c2 -= 1
            in_degree[c2] += 1  # 入度+1
            follow[c1].append(c2)

        # 优先队列保存课程结束时间
        queue = []
        # 初始化优先队列
        for i, d in enumerate(in_degree):
            if d == 0:
                heapq.heappush(queue, (time[i], i))

        res = 0
        while queue:
            t, i = heapq.heappop(queue)
            if i in follow:
                # 处理后续课程
                for c in follow[i]:
                    in_degree[c] -= 1
                    if in_degree[c] <= 0:
                        heapq.heappush(queue, (t + time[c], c))
            res = t

        return res
# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    print(solution.minimumTime(3, [[1, 3], [2, 3]], [3, 2, 5]))  # 8
    print(solution.minimumTime(
        5, [[1, 5], [2, 5], [3, 5], [3, 4], [4, 5]], [1, 2, 3, 4, 5]))  # 12
