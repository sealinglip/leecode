#
# @lc app=leetcode.cn id=3102 lang=python3
#
# [3102] 最小化曼哈顿距离
#
# 给你一个下标从 0 开始的数组 points ，它表示二维平面上一些点的整数坐标，其中 points[i] = [xi, yi] 。
# 两点之间的距离定义为它们的曼哈顿距离。
# 请你恰好移除一个点，返回移除后任意两点之间的 最大 距离可能的 最小 值。

# 示例 1：
# 输入：points = [[3,10],[5,15],[10,2],[4,4]]
# 输出：12
# 解释：移除每个点后的最大距离如下所示：
# - 移除第 0 个点后，最大距离在点 (5, 15) 和 (10, 2) 之间，为 |5 - 10| + |15 - 2| = 18 。
# - 移除第 1 个点后，最大距离在点 (3, 10) 和 (10, 2) 之间，为 |3 - 10| + |10 - 2| = 15 。
# - 移除第 2 个点后，最大距离在点 (5, 15) 和 (4, 4) 之间，为 |5 - 4| + |15 - 4| = 12 。
# - 移除第 3 个点后，最大距离在点 (5, 15) 和 (10, 2) 之间的，为 |5 - 10| + |15 - 2| = 18 。
# 在恰好移除一个点后，任意两点之间的最大距离可能的最小值是 12 。

# 示例 2：
# 输入：points = [[1,1],[1,1],[1,1]]
# 输出：0
# 解释：移除任一点后，任意两点之间的最大距离都是 0 。
 
# 提示：
# 3 <= points.length <= 10^5
# points[i].length == 2
# 1 <= points[i][0], points[i][1] <= 10^8

# Hard

from math import inf
from typing import List, Tuple
# @lc code=start
class Solution:
    def minimumDistance(self, points: List[List[int]]) -> int:
        # 找出最大距离的两个点，如果有多组，直接返回这个最大距离
        # 如果只有一组，那么分别去掉这一组的两个点，记得次最大距离，里面最小的那个即为结果
        # 设A，B两点坐标分别为(x1, y1)、(x2, y2)
        # 则A，B两点的曼哈顿距离d(A, B) = max(|(x1-y1) - (x2-y2)|, |(x1+y1) - (x2+y2)|)
        # 即曼哈顿距离是两点各自坐标和之差、各自坐标差之差的绝对值最大值
        n = len(points)
        sx = sorted((x-y, i) for i, (x, y) in enumerate(points))
        sy = sorted((x+y, i) for i, (x, y) in enumerate(points))
        ma1 = sx[-1][0] - sx[0][0]
        ma2 = sy[-1][0] - sy[0][0]
        res = inf
        i = j = 0
        if ma1 >= ma2:
            i, j = sx[0][1], sx[-1][1]
        else:
            i, j = sy[0][1], sy[-1][1]

        def maxWithout(arr: List[Tuple[int]], p: int) -> int:
            d = 0
            if arr[0][1] == p:
                d = max(d, arr[-1][0] - arr[1][0])
            elif arr[-1][1] == p:
                d = max(d, arr[-2][0] - arr[0][0])
            else:
                d = max(d, arr[-1][0] - arr[0][0])
            return d

        # 去掉i后的最大距离
        res = min(res, max(maxWithout(sx, i), maxWithout(sy, i)))
        # 去掉j后的最大距离
        res = min(res, max(maxWithout(sx, j), maxWithout(sy, j)))
        return res


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.minimumDistance([[3,10],[5,15],[10,2],[4,4]])) # 12
    print(solution.minimumDistance([[1,1],[1,1],[1,1]])) # 0