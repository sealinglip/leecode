#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2021-11-09 21:01:15
LastEditors: Thomas Young
LastEditTime: 2021-11-09 22:46:15
'''
#
# @lc app=leetcode.cn id=488 lang=python3
#
# [488] 祖玛游戏
#
# 你正在参与祖玛游戏的一个变种。

# 在这个祖玛游戏变体中，桌面上有 一排 彩球，每个球的颜色可能是：红色 'R'、黄色 'Y'、蓝色 'B'、绿色 'G' 或白色 'W' 。你的手中也有一些彩球。

# 你的目标是 清空 桌面上所有的球。每一回合：

# 从你手上的彩球中选出 任意一颗 ，然后将其插入桌面上那一排球中：两球之间或这一排球的任一端。
# 接着，如果有出现 三个或者三个以上 且 颜色相同 的球相连的话，就把它们移除掉。
# 如果这种移除操作同样导致出现三个或者三个以上且颜色相同的球相连，则可以继续移除这些球，直到不再满足移除条件。
# 如果桌面上所有球都被移除，则认为你赢得本场游戏。
# 重复这个过程，直到你赢了游戏或者手中没有更多的球。
# 给你一个字符串 board ，表示桌面上最开始的那排球。另给你一个字符串 hand ，表示手里的彩球。请你按上述操作步骤移除掉桌上所有球，计算并返回所需的 最少 球数。如果不能移除桌上所有的球，返回 - 1 。


# 示例 1：
# 输入：board = "WRRBBW", hand = "RB"
# 输出：-1
# 解释：无法移除桌面上的所有球。可以得到的最好局面是：
# - 插入一个 'R' ，使桌面变为 WRRRBBW 。WRRRBBW -> WBBW
# - 插入一个 'B' ，使桌面变为 WBBBW 。WBBBW -> WW
# 桌面上还剩着球，没有其他球可以插入。

# 示例 2：
# 输入：board = "WWRRBBWW", hand = "WRBRW"
# 输出：2
# 解释：要想清空桌面上的球，可以按下述步骤：
# - 插入一个 'R' ，使桌面变为 WWRRRBBWW 。WWRRRBBWW -> WWBBWW
# - 插入一个 'B' ，使桌面变为 WWBBBWW 。WWBBBWW -> WWWW -> empty
# 只需从手中出 2 个球就可以清空桌面。

# 示例 3：
# 输入：board = "G", hand = "GGGGG"
# 输出：2
# 解释：要想清空桌面上的球，可以按下述步骤：
# - 插入一个 'G' ，使桌面变为 GG 。
# - 插入一个 'G' ，使桌面变为 GGG 。GGG -> empty
# 只需从手中出 2 个球就可以清空桌面。

# 示例 4：
# 输入：board = "RBYYBBRRB", hand = "YRBGB"
# 输出：3
# 解释：要想清空桌面上的球，可以按下述步骤：
# - 插入一个 'Y' ，使桌面变为 RBYYYBBRRB 。RBYYYBBRRB -> RBBBRRB -> RRRB -> B
# - 插入一个 'B' ，使桌面变为 BB 。
# - 插入一个 'B' ，使桌面变为 BBB 。BBB -> empty
# 只需从手中出 3 个球就可以清空桌面。


# 提示：
# 1 <= board.length <= 16
# 1 <= hand.length <= 5
# board 和 hand 由字符 'R'、'Y'、'B'、'G' 和 'W' 组成
# 桌面上一开始的球中，不会有三个及三个以上颜色相同且连着的球

# Hard

# @lc code=start
from functools import lru_cache


class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        # 过滤掉hand中不在board中的字符
        l = list(hand)
        l.sort()
        hand = "".join(l)

        def eraze(s: str) -> str:
            '''
            根据消除规则，精简字符串
            '''
            slow = 0
            while slow < len(s):
                fast = slow
                while fast < len(s) and s[fast] == s[slow]:
                    fast += 1
                if fast > slow + 2:
                    return eraze(s[:slow] + s[fast:])
                slow = fast
            return s

        INF = float('inf')
        HLEN = len(hand)

        @lru_cache(None)
        def dfs(b: str, h: str) -> int:
            '''
            深度优先遍历解法
            '''
            if not b:
                # 有解，算用掉的字符数
                return HLEN - len(h)
            elif not h:
                # 无解的情况
                return INF

            r = INF
            for i in range(len(b)):
                if i == 0 or b[i] != b[i-1]:
                    # 只在字符左边插，只插同样的字符
                    j = h.find(b[i])
                    if j != -1:
                        r = min(
                            r, dfs(eraze(b[:i] + h[j] + b[i:]), h[:j] + h[j+1:]))
                else:
                    # 在两个相同字符中间插，插不一样的字符
                    slow = 0
                    while slow < len(h):
                        fast = slow
                        while fast < len(h) and h[fast] == h[slow]:
                            fast += 1
                        if h[slow] != b[i]:
                            r = min(
                                r, dfs(eraze(b[:i] + h[slow] + b[i:]), h[:slow] + h[slow+1:]))
                        slow = fast

            return r

        res = dfs(board, hand)
        return -1 if res == INF else res
# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 下面这个用例说明这个剪枝策略不行：“只在字符左边插，只插同样的字符”
    print(solution.findMinStep("RRWWRRBBRR", "WB"))  # 2
    print(solution.findMinStep("WRRBBW", "RB"))  # -1
    print(solution.findMinStep("WWRRBBWW", "WRBRW"))  # 2
    print(solution.findMinStep("G", "GGGGG"))  # 2
    print(solution.findMinStep("RBYYBBRRB", "YRBGB"))  # 3
    # 下面这个测试用例说明不能把不相关的字符先去了
    print(solution.findMinStep("RRYGGYYRRYYGGYRR", "GGBBB"))  # 5
