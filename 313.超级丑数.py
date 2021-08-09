#
# @lc app=leetcode.cn id=313 lang=python3
#
# [313] 超级丑数
#
# 超级丑数 是一个正整数，并满足其所有质因数都出现在质数数组 primes 中。
# 给你一个整数 n 和一个整数数组 primes ，返回第 n 个 超级丑数 。
# 题目数据保证第 n 个 超级丑数 在 32-bit 带符号整数范围内。


# 示例 1：
# 输入：n = 12, primes = [2,7,13,19]
# 输出：32
# 解释：给定长度为 4 的质数数组 primes = [2,7,13,19]，前 12 个超级丑数序列为：[1,2,4,7,8,13,14,16,19,26,28,32] 。

# 示例 2：
# 输入：n = 1, primes = [2,3,5]
# 输出：1
# 解释：1 不含质因数，因此它的所有质因数都在质数数组 primes = [2,3,5] 中。

# 提示：
# 1 <= n <= 106
# 1 <= primes.length <= 100
# 2 <= primes[i] <= 1000
# 题目数据 保证 primes[i] 是一个质数
# primes 中的所有值都 互不相同 ，且按 递增顺序 排列


from typing import List
# @lc code=start
from bisect import bisect_left
from math import ceil


class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        if n == 1:
            return 1  # 第一个数总是1

        res = [1]

        # 下面这个方法比较低效
        # for i in range(1, n):
        #     next = float('inf')
        #     for p in primes:
        #         factor = ceil((res[-1] + 1) / p)
        #         factor = res[bisect_left(res, factor)]
        #         test = factor * p
        #         if test < next:
        #             next = test
        #     res.append(next)

        pointer = [0] * len(primes)
        for i in range(1, n):
            next = min([res[pointer[j]] * p for j, p in enumerate(primes)])
            # 能计算得到next的方式可能不止一种，都要将指针后移
            for j, p in enumerate(primes):
                test = res[pointer[j]] * p
                if test == next:
                    pointer[j] += 1
            res.append(next)

        return res[-1]

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.nthSuperUglyNumber(
        45, [2, 3, 7, 13, 17, 23, 31, 41, 43, 47]))  # 82
    print(solution.nthSuperUglyNumber(
        15, [3, 5, 7, 11, 19, 23, 29, 41, 43, 47]))  # 35
    print(solution.nthSuperUglyNumber(12, [2, 7, 13, 19]))  # 32
    print(solution.nthSuperUglyNumber(1, [2, 3, 5]))  # 1
