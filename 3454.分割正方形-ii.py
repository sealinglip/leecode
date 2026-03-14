#
# @lc app=leetcode.cn id=3454 lang=python3
#
# [3454] 分割正方形 II
#
# https://leetcode.cn/problems/separate-squares-ii/description/
#
# algorithms
# Hard (39.22%)
# Likes:    9
# Dislikes: 0
# Total Accepted:    2K
# Total Submissions: 4.2K
# Testcase Example:  '[[0,0,1],[2,2,1]]'
#
# 给你一个二维整数数组 squares ，其中 squares[i] = [xi, yi, li] 表示一个与 x
# 轴平行的正方形的左下角坐标和正方形的边长。
# 
# 找到一个最小的 y 坐标，它对应一条水平线，该线需要满足它以上正方形的总面积 等于 该线以下正方形的总面积。
# 答案如果与实际答案的误差在 10^-5 以内，将视为正确答案。
# 
# 注意：正方形 可能会 重叠。重叠区域只 统计一次 。
# 
# 
# 示例 1：
# 输入： squares = [[0,0,1],[2,2,1]]
# 输出： 1.00000
# 解释：
# 任何在 y = 1 和 y = 2 之间的水平线都会有 1 平方单位的面积在其上方，1 平方单位的面积在其下方。最小的 y 坐标是 1。
# 
# 示例 2：
# 输入： squares = [[0,0,2],[1,1,1]]
# 输出： 1.00000
# 解释：
# 由于蓝色正方形和红色正方形有重叠区域且重叠区域只统计一次。所以直线 y = 1 将正方形分割成两部分且面积相等。
# 
# 
# 提示：
# 1 <= squares.length <= 5 * 10^4
# squares[i] = [xi, yi, li]
# squares[i].length == 3
# 0 <= xi, yi <= 10^9
# 1 <= li <= 10^9
# 所有正方形的总面积不超过 10^15。
# 
# 复习
#

from bisect import bisect_left
from math import inf
from typing import List

# from sortedcontainers import SortedList
# class Solution:
#     def separateSquares(self, squares: List[List[int]]) -> float:
#         # 下面的算法会超时，引入线段树解效率问题
#         # 扫描线算法
#         evts = []
#         for x, y, l in squares:
#             evts.append((y, (x, x+l), True))
#             evts.append((y+l, (x, x+l), False))

#         evts.sort(key=lambda e: e[0])
        
#         cuts = SortedList() # 当前扫描线切割的正方形边长列表

#         def calcTotalWidth() -> int:
#             res = 0
#             start = end = -inf
#             for x1, x2 in cuts:
#                 if x1 > end:
#                     res += 0 if end == -inf else (end - start)
#                     start = x1
#                 if x2 > end:
#                     end = x2

#             res += 0 if end == -inf else (end - start)

#             return res
        
#         # 先计算总面积
#         totalArea = 0.0
#         totalWidthCache = dict()
#         totalWidth = 0.0 # 当前扫描线切割的正方形边长和（去除重叠）
#         prevY = 0.0 # 前扫描线的纵坐标
#         for i, (y, interval, flag) in enumerate(evts):
#             delta = y - prevY
#             # 两条扫描线之间新增的面积
#             totalArea += delta * totalWidth
#             if flag:
#                 cuts.add(interval)
#             else:
#                 cuts.remove(interval)

#             totalWidth = calcTotalWidth()
#             totalWidthCache[i] = totalWidth
#             prevY = y
        
#         # reset
#         totalWidth = 0.0
#         prevY = 0.0 
#         accumArea = 0.0 # 当前累计面积（扫描线以下的）

#         for i, (y, _, _) in enumerate(evts):
#             delta = y - prevY
#             # 两条扫描线之间新增的面积
#             area = delta * totalWidth
#             if 2 * (area + accumArea) >= totalArea:
#                 return prevY + (totalArea / 2 - accumArea) / totalWidth

#             totalWidth = totalWidthCache[i]
#             accumArea += area
#             prevY = y

#         return 0

# @lc code=start
class SegmentTree:
    def __init__(self, xs: List[int]):
        self.xs = xs
        self.n = len(xs) - 1
        self.count = [0] * (self.n << 2) # * 4，区间覆盖计数
        self.covered = [0] * (self.n << 2) # * 4，覆盖区间长度合计

    def update(self, qleft, qright, flag, left, right, pos):
        qval = 1 if flag else -1
        if self.xs[right+1] <= qleft or self.xs[left] >= qright: # 区间没交集
            return
        if qleft <= self.xs[left] and self.xs[right+1] <= qright:
            self.count[pos] += qval
        else: 
            mid = (left + right) // 2
            self.update(qleft, qright, flag, left, mid, pos * 2 + 1)
            self.update(qleft, qright, flag, mid+1, right, pos * 2 + 2)

        if self.count[pos] > 0:
            self.covered[pos] = self.xs[right + 1] - self.xs[left]
        else:
            if left == right:
                self.covered[pos] = 0
            else:
                self.covered[pos] = self.covered[pos * 2 + 1] + self.covered[pos * 2 + 2]
    
    def query(self):
        return self.covered[0]


class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        # 原算法会超时，引入线段树解效率问题
        # 扫描线算法
        evts = []
        xsSet = set()
        for x, y, l in squares:
            interval = (x, x+l)
            evts.append((y, interval, True))
            evts.append((y+l, interval, False))
            xsSet.update(interval)
        xs = sorted(xsSet)

        segmentTree = SegmentTree(xs)
        evts.sort()

        areaSum = []
        widths = []
        totalArea = 0.0
        prevY = evts[0][0]

        for y, (xl, xr), flag in evts:
            width = segmentTree.query()
            totalArea += width * (y - prevY)
            segmentTree.update(xl, xr, flag, 0, segmentTree.n - 1, 0)
            areaSum.append(totalArea)
            widths.append(segmentTree.query())
            prevY = y

        # 二分查找
        target = (totalArea + 1) // 2
        # 查找第一个小于等于target的位置
        i = bisect_left(areaSum, target) - 1
        return evts[i][0] + (totalArea / 2.0 - areaSum[i]) / widths[i]
        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.separateSquares([[0,0,1],[2,2,1]])) # 1
    print(solution.separateSquares([[0,0,2],[1,1,1]])) # 1
