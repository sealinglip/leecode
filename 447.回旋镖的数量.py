#
# @lc app=leetcode.cn id=447 lang=python3
#
# [447] 回旋镖的数量
#
# 给定平面上 n 对 互不相同 的点 points ，其中 points[i] = [xi, yi] 。回旋镖 是由点(i, j, k) 表示的元组 ，
# 其中 i 和 j 之间的距离和 i 和 k 之间的距离相等（需要考虑元组的顺序）。
# 返回平面上所有回旋镖的数量。

# 示例 1：
# 输入：points = [[0, 0], [1, 0], [2, 0]]
# 输出：2
# 解释：两个回旋镖为[[1, 0], [0, 0], [2, 0]] 和[[1, 0], [2, 0], [0, 0]]

# 示例 2：
# 输入：points = [[1, 1], [2, 2], [3, 3]]
# 输出：2

# 示例 3：
# 输入：points = [[1, 1]]
# 输出：0


# 提示：
# n == points.length
# 1 <= n <= 500
# points[i].length == 2
# -10^4 <= xi, yi <= 10^4
# 所有点都 互不相同

from typing import List
# @lc code=start
from collections import defaultdict


class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        N = len(points)
        if N < 3:
            return 0

        # cache = {}

        def getDistance(i: int, j: int) -> int:
            # if i > j:
            #     i, j = j, i
            # key = (i << 9) + j
            # if key in cache:
            #     return cache[key]
            # else:
            d = (points[i][0] - points[j][0]) ** 2 + \
                (points[i][1] - points[j][1]) ** 2
            # cache[key] = d
            return d

        res = 0
        for i in range(N):
            nodeList = defaultdict(int)
            for j in range(N):
                if j == i:
                    continue
                d = getDistance(i, j)
                nodeList[d] += 1

            for v in nodeList.values():
                if v > 1:
                    res += v * (v - 1)

        return res

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.numberOfBoomerangs([[0, 0], [1, 0], [2, 0]]))  # 2
    print(solution.numberOfBoomerangs([[1, 1], [2, 2], [3, 3]]))  # 2
    print(solution.numberOfBoomerangs([[1, 1]]))  # 0
