#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2021-12-15 22:13:40
LastEditors: Thomas Young
LastEditTime: 2021-12-15 22:49:27
'''
#
# @lc app=leetcode.cn id=851 lang=python3
#
# [851] 喧闹和富有
#
# 有一组 n 个人作为实验对象，从 0 到 n - 1 编号，其中每个人都有不同数目的钱，以及不同程度的安静值（quietness）。为了方便起见，我们将编号为 x 的人简称为 "person x "。
# 给你一个数组 richer ，其中 richer[i] = [ai, bi] 表示 person ai 比 person bi 更有钱。另给你一个整数数组 quiet ，其中 quiet[i] 是 person i 的安静值。
# richer 中所给出的数据 逻辑自恰（也就是说，在 person x 比 person y 更有钱的同时，不会出现 person y 比 person x 更有钱的情况 ）。
# 现在，返回一个整数数组 answer 作为答案，其中 answer[x] = y 的前提是，在所有拥有的钱肯定不少于 person x 的人中，person y 是最安静的人（也就是安静值 quiet[y] 最小的人）。


# 示例 1：
# 输入：richer = [[1, 0], [2, 1], [3, 1], [3, 7], [4, 3], [5, 3], [6, 3]], quiet = [3, 2, 5, 4, 6, 1, 7, 0]
# 输出：[5, 5, 2, 5, 4, 5, 6, 7]
# 解释：
# answer[0] = 5，
# person 5 比 person 3 有更多的钱，person 3 比 person 1 有更多的钱，person 1 比 person 0 有更多的钱。
# 唯一较为安静（有较低的安静值 quiet[x]）的人是 person 7，
# 但是目前还不清楚他是否比 person 0 更有钱。
# answer[7] = 7，
# 在所有拥有的钱肯定不少于 person 7 的人中（这可能包括 person 3，4，5，6 以及 7），
# 最安静（有较低安静值 quiet[x]）的人是 person 7。
# 其他的答案也可以用类似的推理来解释。


# 示例 2：
# 输入：richer = [], quiet = [0]
# 输出：[0]


# 提示：
# n == quiet.length
# 1 <= n <= 500
# 0 <= quiet[i] < n
# quiet 的所有值 互不相同
# 0 <= richer.length <= n * (n - 1) / 2
# 0 <= ai, bi < n
# ai != bi
# richer 中的所有数对 互不相同
# 对 richer 的观察在逻辑上是一致的

from typing import List
# @lc code=start
from collections import deque
class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        N = len(quiet)
        g = [[] for _ in range(N)] # g[i]存放比i小的所有
        inDeg = [0] * N # 存放入度
        for a, b in richer:
            g[a].append(b)
            inDeg[b] += 1

        ans = list(range(N)) # 初始化ans[i] = i
        # 从入度为0的节点开始处理
        deq = deque(i for i, deg in enumerate(inDeg) if deg == 0)
        while deq:
            a = deq.popleft()
            for b in g[a]:
                if quiet[ans[a]] < quiet[ans[b]]:
                    ans[b] = ans[a]
                inDeg[b] -= 1
                if inDeg[b] == 0:
                    deq.append(b)

        return ans
        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.loudAndRich([[1, 0], [2, 1], [3, 1], [3, 7], [
          4, 3], [5, 3], [6, 3]], [3, 2, 5, 4, 6, 1, 7, 0]))  # [5, 5, 2, 5, 4, 5, 6, 7]
    print(solution.loudAndRich([], [0]))  # [0]
