#
# @lc app=leetcode.cn id=1494 lang=python3
#
# [1494] 并行课程 II
#
# 给你一个整数 n 表示某所大学里课程的数目，编号为 1 到 n ，数组 relations 中， relations[i] = [xi, yi]
# 表示一个先修课的关系，也就是课程 xi 必须在课程 yi 之前上。同时你还有一个整数 k 。
# 在一个学期中，你 最多 可以同时上 k 门课，前提是这些课的先修课在之前的学期里已经上过了。
# 请你返回上完所有课最少需要多少个学期。题目保证一定存在一种上完所有课的方式。


# 示例 1：
# 输入：n = 4, relations = [[2, 1], [3, 1], [1, 4]], k = 2
# 输出：3
# 解释：上图展示了题目输入的图。在第一个学期中，我们可以上课程 2 和课程 3 。然后第二个学期上课程 1 ，第三个学期上课程 4 。

# 示例 2：
# 输入：n = 5, relations = [[2, 1], [3, 1], [4, 1], [1, 5]], k = 2
# 输出：4
# 解释：上图展示了题目输入的图。一个最优方案是：第一学期上课程 2 和 3，第二学期上课程 4 ，第三学期上课程 1 ，第四学期上课程 5 。

# 示例 3：
# 输入：n = 11, relations = [], k = 2
# 输出：6


# 提示：
# 1 <= n <= 15
# 1 <= k <= n
# 0 <= relations.length <= n * (n-1) / 2
# relations[i].length == 2
# 1 <= xi, yi <= n
# xi != yi
# 所有先修关系都是不同的，也就是说 relations[i] != relations[j] 。
# 题目输入的图是个有向无环图。

# 复习
from math import inf
from typing import List
# @lc code=start


class Solution:
    def minNumberOfSemesters(self, n: int, relations: List[List[int]], k: int) -> int:
        # 拓扑排序很难
        # target = (1 << (n + 1)) - 2  # 所有功课都修了

        # preq = [0] * (n + 1)  # 记录前置条件
        # post = [0] * (n + 1)  # 后置依赖
        # for x, y in relations:
        #     preq[y] |= (1 << x)
        #     post[x] |= (1 << y)
        # # 如果当前轮次有超过k门功课可修，修哪些不修哪些？需要有一个优先级选择，倒排级次高的优先修
        # inverted_level_and_weight = [[0, 0] for i in range(n + 1)]  # 倒排级次和权重
        # mask = 0  # 记录已经标记倒排级次的功课
        # while mask != target:
        #     newmask = mask
        #     for j in range(1, n+1):
        #         c = 1 << j
        #         if (mask & c) == 0 and (mask & post[j]) == post[j]:
        #             # 当前功课未标记倒排级次，且其后续都已经标记级次
        #             inverted_level_and_weight[j][0] = (max(inverted_level_and_weight[i][0] for i in range(
        #                 1, n+1) if post[j] & (1 << i)) if post[j] else 0) + 1
        #             inverted_level_and_weight[j][1] += 1
        #             if preq[j]:
        #                 contri_weight = inverted_level_and_weight[j][1] / \
        #                     preq[j].bit_count()
        #                 for i in range(1, n+1):
        #                     if preq[j] & (1 << i):
        #                         inverted_level_and_weight[i][1] += contri_weight

        #             newmask |= c
        #     mask = newmask
        # inverted_level_and_weight[0][0] = n+1

        # topo_sorted = list(i for _, _, i in sorted((-x, -w, i)
        #                    for i, (x, w) in enumerate(inverted_level_and_weight)))[1:]

        # mask = 0  # 记录已经修过的功课。重置为0：此时还一门都没修
        # semesters = 0
        # while mask != target:
        #     newmask = mask
        #     # 修现在可以修的功课，到k为止
        #     i = 0
        #     for j in topo_sorted:
        #         if i >= k:
        #             break
        #         c = 1 << j
        #         # 没修过j，可以修了
        #         if (mask & c) == 0 and (mask & preq[j]) == preq[j]:
        #             newmask |= c
        #             i += 1
        #     if mask == newmask:
        #         # 无解
        #         return -1
        #     mask = newmask
        #     semesters += 1

        # return semesters
        dp = [inf] * (1 << n)
        need = [0] * (1 << n)
        for x, y in relations:
            need[1 << (y-1)] |= 1 << (x-1)

        dp[0] = 0
        for i in range(1, 1 << n):
            need[i] = need[i & (i-1)] | need[i & (-i)]
            if (need[i] | i) != i:
                continue
            sub = valid = i ^ need[i]
            if sub.bit_count() <= k:
                dp[i] = min(dp[i], dp[i ^ sub] + 1)
            else:
                while sub:
                    if sub.bit_count() <= k:
                        dp[i] = min(dp[i], dp[i ^ sub] + 1)
                    sub = (sub - 1) & valid

        return dp[-1]

# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    print(solution.minNumberOfSemesters(
        12, [[11, 10], [6, 3], [2, 5], [9, 2], [4, 12], [8, 7], [9, 5], [6, 2], [7, 2], [7, 4], [9, 3], [11, 1], [4, 3]], 3))  # 4
    print(solution.minNumberOfSemesters(
        5, [[1, 5], [1, 3], [1, 2], [4, 2], [4, 5], [2, 5], [1, 4], [4, 3], [3, 5], [3, 2]], 3))  # 5
    print(solution.minNumberOfSemesters(
        9, [[1, 5], [2, 5], [3, 5], [4, 6], [4, 7], [4, 8], [4, 9]], 3))  # 3
    print(solution.minNumberOfSemesters(13, [[12, 8], [2, 4], [3, 7], [6, 8], [11, 8], [9, 4], [9, 7], [12, 4], [11, 4], [6, 4], [1, 4], [
          10, 7], [10, 4], [1, 7], [1, 8], [2, 7], [8, 4], [10, 8], [12, 7], [5, 4], [3, 4], [11, 7], [7, 4], [13, 4], [9, 8], [13, 8]], 9))  # 3
    print(solution.minNumberOfSemesters(4, [[2, 1], [3, 1], [1, 4]], 2))  # 3
    print(solution.minNumberOfSemesters(
        5, [[2, 1], [3, 1], [4, 1], [1, 5]], 2))  # 4
    print(solution.minNumberOfSemesters(11, [], 2))  # 6
