#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2020-11-18 09:00:53
LastEditors: Thomas Young
LastEditTime: 2020-11-19 09:19:55
'''
#
# @lc app=leetcode.cn id=134 lang=python3
#
# [134] 加油站
#
# 在一条环路上有 N 个加油站，其中第 i 个加油站有汽油 gas[i] 升。
# 你有一辆油箱容量无限的的汽车，从第 i 个加油站开往第 i+1 个加油站需要消耗汽油 cost[i] 升。
# 你从其中的一个加油站出发，开始时油箱为空。
# 如果你可以绕环路行驶一周，则返回出发时加油站的编号，否则返回 - 1。

# 说明:
# 如果题目有解，该答案即为唯一答案。
# 输入数组均为非空数组，且长度相同。
# 输入数组中的元素均为非负数。

# 示例 1:
# 输入:
# gas = [1, 2, 3, 4, 5]
# cost = [3, 4, 5, 1, 2]
# 输出: 3
# 解释:
# 从 3 号加油站(索引为 3 处)出发，可获得 4 升汽油。此时油箱有 = 0 + 4 = 4 升汽油
# 开往 4 号加油站，此时油箱有 4 - 1 + 5 = 8 升汽油
# 开往 0 号加油站，此时油箱有 8 - 2 + 1 = 7 升汽油
# 开往 1 号加油站，此时油箱有 7 - 3 + 2 = 6 升汽油
# 开往 2 号加油站，此时油箱有 6 - 4 + 3 = 5 升汽油
# 开往 3 号加油站，你需要消耗 5 升汽油，正好足够你返回到 3 号加油站。
# 因此，3 可为起始索引。

# 示例 2:
# 输入:
# gas = [2, 3, 4]
# cost = [3, 4, 3]
# 输出: -1
# 解释:
# 你不能从 0 号或 1 号加油站出发，因为没有足够的汽油可以让你行驶到下一个加油站。
# 我们从 2 号加油站出发，可以获得 4 升汽油。 此时油箱有 = 0 + 4 = 4 升汽油
# 开往 0 号加油站，此时油箱有 4 - 3 + 2 = 3 升汽油
# 开往 1 号加油站，此时油箱有 3 - 3 + 3 = 3 升汽油
# 你无法返回 2 号加油站，因为返程需要消耗 4 升汽油，但是你的油箱只有 3 升汽油。
# 因此，无论怎样，你都不可能绕环路行驶一周。

from typing import List
# @lc code=start
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # if sum(gas) < sum(cost):
        #     return -1
        # else:
        #     N = len(gas)
        #     delta = [gas[i] - cost[i] for i in range(N)]
        #     # 需要找出有没有一个位置，从该位置开始，往后累积的delta都不小于0
        #     # 从第一个非零的delta开始累计
        #     accum = 0
        #     start = 0
        #     for i, v in enumerate(delta):
        #         if v >= 0:
        #             start = i
        #             break
        #     # 从start开始累计
        #     block = None
        #     tryStart, tryEnd = start, start + N
        #     while tryStart < tryEnd:
        #         for i in range(tryStart, tryEnd):
        #             if i >= N:
        #                 i -= N
        #             accum = accum + delta[i]
        #             if accum < 0:
        #                 # 到i位置受阻了
        #                 block = i
        #                 break
        #         else:
        #             return start
                    
        #         # 阻塞在block位置，从start往前找，看是否有合适的起点
        #         backAccum = 0
        #         for i in range(start - 1, block - N, -1):
        #             if i < 0:
        #                 i += N
        #             backAccum += delta[i]
        #             if delta[i] > 0 and (backAccum + accum) >= 0:
        #                 start = i # 新尝试起点
        #                 accum += backAccum
        #                 break
        #         else:
        #             return -1 # 找不到合适的新起点
        #         tryStart, tryEnd = block + 1, start if start > block else start + N
        #     else:
        #         return start

        # 如果从i站开始，不能通过j站（设j > i），那么从[i+1:j-1]区间的站开始，也都不能通过j站
        # 要测试是否能绕一周，从0号站开始，尝试，如果到x站通不过，换成从x站开始尝试
        start = 0
        n = len(gas)
        while start < n:
            totalGas = totalCost = cnt = 0
            while cnt < n:
                i = (start + cnt) % n
                totalGas += gas[i]
                totalCost += cost[i]
                if totalCost > totalGas:
                    start += cnt + 1
                    break
                cnt += 1

            if cnt == n:
                return start
        
        return -1
                

# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.canCompleteCircuit([5, 8, 2, 8], [6, 5, 6, 6])) # 3
    print(solution.canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2])) # 3
    print(solution.canCompleteCircuit([2, 3, 4], [3, 4, 3])) # -1
