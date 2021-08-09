#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2021-07-13 21:33:04
LastEditors: Thomas Young
LastEditTime: 2021-07-13 21:33:55
'''
#
# @lc app=leetcode.cn id=1711 lang=python3
#
# [1711] 大餐计数
#
# 大餐 是指 恰好包含两道不同餐品 的一餐，其美味程度之和等于 2 的幂。
# 你可以搭配 任意 两道餐品做一顿大餐。
# 给你一个整数数组 deliciousness ，其中 deliciousness[i] 是第 i​​​​​​​​​​​​​​ 道餐品的美味程度，返回你可以用数组中的餐品做出的不同 大餐 的数量。结果需要对 109 + 7 取余。
# 注意，只要餐品下标不同，就可以认为是不同的餐品，即便它们的美味程度相同。

# 示例 1：
# 输入：deliciousness = [1, 3, 5, 7, 9]
# 输出：4
# 解释：大餐的美味程度组合为(1, 3) 、(1, 7) 、(3, 5) 和(7, 9) 。
# 它们各自的美味程度之和分别为 4 、8 、8 和 16 ，都是 2 的幂。

# 示例 2：
# 输入：deliciousness = [1, 1, 1, 3, 3, 3, 7]
# 输出：15
# 解释：大餐的美味程度组合为 3 种(1, 1) ，9 种(1, 3) ，和 3 种(1, 7) 。

# 提示：
# 1 <= deliciousness.length <= 10^5
# 0 <= deliciousness[i] <= 2^20

from typing import List
from collections import Counter
# @lc code=start


class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        MOD = (10 ** 9) + 7
        stat = Counter(deliciousness)
        cnt = 0

        def closest2n(x: int) -> int:
            x = x | (x >> 1)
            x = x | (x >> 2)
            x = x | (x >> 4)
            x = x | (x >> 8)
            x = x | (x >> 16)
            return x + 1

        for key in sorted(stat.keys(), reverse=True):  # 从大到小
            if key > 0:
                complement = closest2n(key) - key
                if complement == key:
                    cnt += stat[key] * (stat[key] - 1) // 2
                    cnt += stat[key] * stat[0]
                elif complement in stat:
                    cnt += stat[key] * stat[complement]

        return cnt % MOD
        # @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.countPairs([32, 32, 32, 32, 32, 32, 32, 32]))
    print(solution.countPairs([149, 107, 1, 63, 0, 1, 6867,
                               1325, 5611, 2581, 39, 89, 46, 18, 12, 20, 22, 234]))
    print(solution.countPairs([2160, 1936, 3, 29, 27, 5, 2503, 1593, 2, 0, 16, 0, 3860, 28908, 6, 2, 15, 49,
                               6246, 1946, 23, 105, 7996, 196, 0, 2, 55, 457, 5, 3, 924, 7268, 16, 48, 4, 0, 12, 116, 2628, 1468]))
    print(solution.countPairs([1, 3, 5, 7, 9]))
    print(solution.countPairs([1, 1, 1, 3, 3, 3, 7]))
