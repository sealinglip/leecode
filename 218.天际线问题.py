#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2021-07-13 21:33:04
LastEditors: Thomas Young
LastEditTime: 2021-07-13 22:34:50
'''
#
# @lc app=leetcode.cn id=218 lang=python3
#
# [218] 天际线问题
#
# 城市的天际线是从远处观看该城市中所有建筑物形成的轮廓的外部轮廓。给你所有建筑物的位置和高度，请返回由这些建筑物形成的 天际线 。
# 每个建筑物的几何信息由数组 buildings 表示，其中三元组 buildings[i] = [lefti, righti, heighti] 表示：

# lefti 是第 i 座建筑物左边缘的 x 坐标。
# righti 是第 i 座建筑物右边缘的 x 坐标。
# heighti 是第 i 座建筑物的高度。
# 天际线 应该表示为由 “关键点” 组成的列表，格式[[x1, y1], [x2, y2], ...] ，并按 x 坐标 进行 排序 。关键点是水平线段的左端点。列表中最后一个点是最右侧建筑物的终点，y 坐标始终为 0 ，仅用于标记天际线的终点。此外，任何两个相邻建筑物之间的地面都应被视为天际线轮廓的一部分。

# 注意：输出天际线中不得有连续的相同高度的水平线。例如[...[2 3], [4 5], [7 5], [11 5], [12 7]...] 是不正确的答案；三条高度为 5 的线应该在最终输出中合并为一个：[...[2 3], [4 5], [12 7], ...]

# 示例 1：
# 输入：buildings = [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]
# 输出：[[2, 10], [3, 15], [7, 12], [12, 0], [15, 10], [20, 8], [24, 0]]
# 解释：
# 图 A 显示输入的所有建筑物的位置和高度，
# 图 B 显示由这些建筑物形成的天际线。图 B 中的红点表示输出列表中的关键点。

# 示例 2：
# 输入：buildings = [[0, 2, 3], [2, 5, 3]]
# 输出：[[0, 3], [5, 0]]

# 提示：
# 1 <= buildings.length <= 10^4
# 0 <= lefti < righti <= 2^31 - 1
# 1 <= heighti <= 2^31 - 1
# buildings 按 lefti 非递减排序

# Hard
# 复习

from typing import List
# @lc code=start
import heapq


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        s = []  # 优先队列
        ans = []
        cur = 0
        # 初始化优先队列
        for left, right, height in buildings:
            while s and s[0][1] < left:
                rh, r = heapq.heappop(s)
                if r >= cur:
                    if not s or rh != s[0][0]:
                        while s and r > s[0][1]:
                            heapq.heappop(s)
                        rh = -s[0][0] if s else 0
                        # 避免右端点重复
                        if r == ans[-1][0]:
                            ans[-1][1] = min(ans[-1][1], rh)
                        else:
                            ans.append([r, rh])
                    cur = r
            if not s or height > -s[0][0]:
                # 避免左端点重复的问题
                if ans and left == ans[-1][0]:
                    ans[-1][1] = height
                else:
                    ans.append([left, height])
            heapq.heappush(s, [-height, right])
        while s:
            rh, r = heapq.heappop(s)
            if r >= cur:
                if not s or rh != s[0][0]:
                    while s and r > s[0][1]:
                        heapq.heappop(s)
                    rh = -s[0][0] if s else 0
                    # 避免右端点重复
                    if r == ans[-1][0]:
                        ans[-1][1] = min(ans[-1][1], rh)
                    else:
                        ans.append([r, rh])
                cur = r
        return ans


        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.getSkyline(
        [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]))  # [[2, 10], [3, 15], [7, 12], [12, 0], [15, 10], [20, 8], [24, 0]]
    print(solution.getSkyline([[0, 2, 3], [2, 5, 3]]))  # [[0, 3], [5, 0]]
