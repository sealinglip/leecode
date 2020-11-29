#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2020-09-06 08:51:12
LastEditors: Thomas Young
LastEditTime: 2020-10-25 19:35:25
'''
#
# @lc app=leetcode.cn id=1024 lang=python3
#
# [1024] 视频拼接
#
# 你将会获得一系列视频片段，这些片段来自于一项持续时长为 T 秒的体育赛事。这些片段可能有所重叠，也可能长度不一。
# 视频片段 clips[i] 都用区间进行表示：开始于 clips[i][0] 并于 clips[i][1] 结束。我们甚至可以对这些片段自由地再剪辑，
# 例如片段[0, 7] 可以剪切成[0, 1] + [1, 3] + [3, 7] 三部分。
# 我们需要将这些片段进行再剪辑，并将剪辑后的内容拼接成覆盖整个运动过程的片段（[0, T]）。返回所需片段的最小数目，如果无法完成该任务，则返回 - 1 。

# 示例 1：
# 输入：clips = [[0, 2], [4, 6], [8, 10], [1, 9], [1, 5], [5, 9]], T = 10
# 输出：3
# 解释：
# 我们选中[0, 2], [8, 10], [1, 9] 这三个片段。
# 然后，按下面的方案重制比赛片段：
# 将[1, 9] 再剪辑为[1, 2] + [2, 8] + [8, 9] 。
# 现在我们手上有[0, 2] + [2, 8] + [8, 10]，而这些涵盖了整场比赛[0, 10]。

# 示例 2：
# 输入：clips = [[0, 1], [1, 2]], T = 5
# 输出：- 1
# 解释：
# 我们无法只用[0, 1] 和[1, 2] 覆盖[0, 5] 的整个过程。

# 示例 3：
# 输入：clips = [[0, 1], [6, 8], [0, 2], [5, 6], [0, 4], [0, 3], [6, 7], [1, 3], [4, 7], [1, 4], 
# [2, 5], [2, 6], [3, 4], [4, 5], [5, 7], [6, 9]], T = 9
# 输出：3
# 解释：
# 我们选取片段[0, 4], [4, 7] 和[6, 9] 。

# 示例 4：
# 输入：clips = [[0, 4], [2, 8]], T = 5
# 输出：2
# 解释：
# 注意，你可能录制超过比赛结束时间的视频。

# 提示：
# 1 <= clips.length <= 100
# 0 <= clips[i][0] <= clips[i][1] <= 100
# 0 <= T <= 100

from typing import List
# @lc code=start
class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        if not clips and T > 0:
            return -1
        elif not T:
            return 0
        
        # 方法1
        # # 对 clips进行排序
        # # 根据clip[0] * 128 - clip[1]的值排序，等效于order by clip[0], clip[1] desc
        # clips.sort(key=lambda clip: (clip[0] << 7) - clip[1])

        # start = -1
        # bound = 0
        # idx, clipCnt = 0, len(clips)
        # stack = []
        # while idx < clipCnt and bound < T:
        #     if clips[idx][0] > bound: # 后一个片段跟前一个搭不上
        #         return -1
        #     if clips[idx][0] == start:
        #         idx += 1
        #         continue
        #     start = clips[idx][0]
        #     if not stack:
        #         stack.append(clips[idx])
        #     elif clips[idx][1] > bound:
        #         while len(stack) > 1 and stack[-2][1] >= start:
        #             stack.pop()

        #         stack.append(clips[idx])
        #     else:
        #         idx += 1
        #         continue
        #     bound = stack[-1][1]
        #     idx += 1
        
        # if bound < T:
        #     return -1
        
        # return len(stack)

        # 方法2：动态规划
        # 记dp[i]为用提供的clips覆盖区间[0, i)需要的最少clip数目
        # 那么题目即为要求dp[T]
        # dp存在如下关系
        # dp[i] = min(dp[clip[j][0]] + 1 for j in range(len(clips) if clip[j][0] < i <= clip[j][1]))
        # dp[0] = 0
        # dp = [0] + [float('inf')] * T

        # for i in range(1, T+1):
        #     for start, end in clips:
        #         if start < i <= end:
        #             dp[i] = min(dp[i], dp[start] + 1)
        # return -1 if dp[T] == float('inf') else dp[T]

        # 方法3：贪心算法
        # maxn[i] 代表左边界为i的clip中最大的右边界
        maxn = [0] * T
        for start, end in clips:
            if start < T:
                maxn[start] = max(maxn[start], end)

        # last 就代表了当前能覆盖到的最远的右端点。
        # prev 代表了上一个最远的右端点
        last = prev = 0
        res = 0
        for i in range(T):
            last = max(last, maxn[i])
            if last == i:
                return -1 # 找不出能覆盖全部的方案
            if prev == i:
                res += 1
                prev = last

        return res

        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.videoStitching(
        [[0, 2], [4, 6], [8, 10], [1, 9], [1, 5], [5, 9]], 10))
    print(solution.videoStitching(
        [[5, 7], [1, 8], [0, 0], [2, 3], [4, 5], [0, 6], [5, 10], [7, 10]], 5))
    print(solution.videoStitching(
        [[0, 1], [1, 2]], 5))
    print(solution.videoStitching(
        [[0, 1], [6, 8], [0, 2], [5, 6], [0, 4], [0, 3], [6, 7], [1, 3], [4, 7], [1, 4], [2, 5], [2, 6], [3, 4], [4, 5], [5, 7], [6, 9]], 9))
    print(solution.videoStitching(
        [[0, 4], [2, 8]], 5))
