#
# @lc app=leetcode.cn id=1326 lang=python3
#
# [1326] 灌溉花园的最少水龙头数目
#
# 在 x 轴上有一个一维的花园。花园长度为 n，从点 0 开始，到点 n 结束。
# 花园里总共有 n + 1 个水龙头，分别位于[0, 1, ..., n] 。
# 给你一个整数 n 和一个长度为 n + 1 的整数数组 ranges ，其中 ranges[i] （下标从 0 开始）
# 表示：如果打开点 i 处的水龙头，可以灌溉的区域为[i - ranges[i], i + ranges[i]] 。
# 请你返回可以灌溉整个花园的 最少水龙头数目 。如果花园始终存在无法灌溉到的地方，请你返回 - 1 。


# 示例 1：
# 输入：n = 5, ranges = [3, 4, 1, 1, 0, 0]
# 输出：1
# 解释：
# 点 0 处的水龙头可以灌溉区间[-3, 3]
# 点 1 处的水龙头可以灌溉区间[-3, 5]
# 点 2 处的水龙头可以灌溉区间[1, 3]
# 点 3 处的水龙头可以灌溉区间[2, 4]
# 点 4 处的水龙头可以灌溉区间[4, 4]
# 点 5 处的水龙头可以灌溉区间[5, 5]
# 只需要打开点 1 处的水龙头即可灌溉整个花园[0, 5] 。

# 示例 2：
# 输入：n = 3, ranges = [0, 0, 0, 0]
# 输出：- 1
# 解释：即使打开所有水龙头，你也无法灌溉整个花园。

# 提示：
# 1 <= n <= 10^4
# ranges.length == n + 1
# 0 <= ranges[i] <= 100

# Hard
# 复习

from math import inf
from typing import List
# @lc code=start


class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        intervals = [(max(0, i-x), min(n, i+x)) for i, x in enumerate(ranges)]
        # intervals.sort()  # 排序
        # 动规
        # # 要求选择最少的区间形成连续区间
        # # 记dp[i] 为覆盖[0,i]区间所需要最少的区间数量
        # # 有dp[0] = 0
        # dp = [inf] * (n + 1)
        # dp[0] = 0
        # for s, e in intervals:
        #     if dp[s] == inf:
        #         return -1
        #     for j in range(s, e + 1):
        #         dp[j] = min(dp[j], dp[s] + 1)
        # return dp[n]

        # 贪心
        intervals.sort(key=lambda i: (i[0], -i[1]))  # 按区间起点升序，终点降序排序
        res = 0
        pos = reach = 0
        for s, e in intervals:
            if s > reach:
                return -1
            if s > pos:
                res += 1
                pos = reach
            reach = max(reach, e)
        if n > pos:
            res += 1

        return res


        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.minTaps(7, [1, 2, 1, 0, 2, 1, 0, 1]))  # 3
    print(solution.minTaps(5, [3, 4, 1, 1, 0, 0]))  # 1
    print(solution.minTaps(3, [0, 0, 0, 0]))  # -1
