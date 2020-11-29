#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2020-11-09 13:26:46
LastEditors: Thomas Young
LastEditTime: 2020-11-09 22:23:00
'''
#
# @lc app=leetcode.cn id=973 lang=python3
#
# [973] 最接近原点的 K 个点
#
# 我们有一个由平面上的点组成的列表 points。需要从中找出 K 个距离原点(0, 0) 最近的点。
# （这里，平面上两点之间的距离是欧几里德距离。）

# 你可以按任何顺序返回答案。除了点坐标的顺序之外，答案确保是唯一的。

# 示例 1：
# 输入：points = [[1, 3], [-2, 2]], K = 1
# 输出：[[-2, 2]]
# 解释：
# (1, 3) 和原点之间的距离为 sqrt(10)，
# (-2, 2) 和原点之间的距离为 sqrt(8)，
# 由于 sqrt(8) < sqrt(10)，(-2, 2) 离原点更近。
# 我们只需要距离原点最近的 K = 1 个点，所以答案就是[[-2, 2]]。

# 示例 2：
# 输入：points = [[3, 3], [5, -1], [-2, 4]], K = 2
# 输出：[[3, 3], [-2, 4]]
# （答案[[-2, 4], [3, 3]] 也会被接受。）

# 提示：
# 1 <= K <= points.length <= 10000
# -10000 < points[i][0] < 10000
# -10000 < points[i][1] < 10000

from typing import List, Tuple
# @lc code=start
import math
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        if not points:
            return points

        # 采用大顶堆来解决
        topK, size = [None for i in range(K)], 0

        def siftup(i: int, pt: Tuple):
            while i > 0:
                parent = (i - 1) >> 1
                p = topK[parent]
                if pt[0] <= p[0]:
                    break
                topK[i] = p
                i = parent
            topK[i] = pt

        def siftdown(i: int, pt: Tuple):
            half = K >> 1
            while i < half:
                child = (i << 1) + 1
                c = topK[child]
                right = child + 1
                if right < size and c[0] < topK[right][0]:  # 取左右节点里的大值
                    child = right
                    c = topK[right]
                if pt[0] >= c[0]:
                    break
                topK[i] = c
                i = child
            topK[i] = pt

        def offer(pt: Tuple):
            nonlocal size
            i = size
            if size < K:
                size += 1
            if i == 0:
                topK[0] = pt
            elif i < K:
                siftup(i, pt)
            elif pt[0] < topK[0][0]:
                siftdown(0, pt)
        
        for pt in points:
            offer((math.sqrt(pt[0] ** 2 + pt[1] ** 2), pt))
        
        return [pt[1] for pt in topK]
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.kClosest([[1, 3], [-2, 2]], 1))
    print(solution.kClosest([[3, 3], [5, -1], [-2, 4]], 2))
    print(solution.kClosest([[68, 97], [34, -84], [60, 100], [2, 31],
                             [-27, -38], [-73, -74], [-55, -39], [62, 91], [62, 92], [-57, -67]], 5))
