#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2020-11-11 08:42:12
LastEditors: Thomas Young
LastEditTime: 2020-11-11 10:13:32
'''
#
# @lc app=leetcode.cn id=514 lang=python3
#
# [514] 自由之路
#
# 视频游戏“辐射4”中，任务“通向自由”要求玩家到达名为“Freedom Trail Ring”的金属表盘，并使用表盘拼写特定关键词才能开门。
# 给定一个字符串 ring，表示刻在外环上的编码；给定另一个字符串 key，表示需要拼写的关键词。您需要算出能够拼写关键词中所有字符的最少步数。
# 最初，ring 的第一个字符与12: 00方向对齐。您需要顺时针或逆时针旋转 ring 以使 key 的一个字符在 12: 00 方向对齐，然后按下中心按钮，以此逐个拼写完 key 中的所有字符。

# 旋转 ring 拼出 key 字符 key[i] 的阶段中：
# 您可以将 ring 顺时针或逆时针旋转一个位置，计为1步。旋转的最终目的是将字符串 ring 的一个字符与 12: 00 方向对齐，并且这个字符必须等于字符 key[i] 。
# 如果字符 key[i] 已经对齐到12: 00方向，您需要按下中心按钮进行拼写，这也将算作 1 步。按完之后，您可以开始拼写 key 的下一个字符（下一阶段）, 直至完成所有拼写。

# 示例：
# 输入: ring = "godding", key = "gd"
# 输出: 4
# 解释:
#  对于 key 的第一个字符 'g'，已经在正确的位置, 我们只需要1步来拼写这个字符。
#  对于 key 的第二个字符 'd'，我们需要逆时针旋转 ring "godding" 2步使它变成 "ddinggo"。
#  当然, 我们还需要1步进行拼写。
#  因此最终的输出是 4。

# 提示：
# ring 和 key 的字符串长度取值范围均为 1 至 100；
# 两个字符串中都只有小写字符，并且均可能存在重复字符；
# 字符串 key 一定可以由字符串 ring 旋转拼出。

# Hard

# @lc code=start
from collections import defaultdict


class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        if not ring or not key:
            return -1

        N = len(ring)
        M = len(key)
        # 记录字符在ring中出现的位置
        pos = defaultdict(list)
        for i, c in enumerate(ring):
            pos[c].append(i)

        # 记dp[i][j]为从前往后拼写出key的第i个字符，ring的第j个字符对齐12点方向的最小步数，易知一定有key[i] == ring[j]
        # 则一定有dp[i][j] = min(dp[i-1][k] + min(abs(j - k), N - abs(j - k)) + 1 for k in pos[key[i-1]]) if i > 0
        #       dp[0][j] = min(j, N - j) + 1
        # 我们要求的是min(dp[M-1][j] for j in pos[key[M-1]])
        dp = [float('inf')] * N
        for j in pos[key[0]]:
            dp[j] = min(j, N - j) + 1

        for i in range(1, M):
            newDp = dp[:]  # make a copy first
            for j in pos[key[i]]:
                newDp[j] = min(
                    [dp[k] + min(abs(j - k), N - abs(j - k)) + 1 for k in pos[key[i-1]]])
            dp = newDp

        return min([dp[j] for j in pos[key[-1]]])


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.findRotateSteps("godding", "gd"))
