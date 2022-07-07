#
# @lc app=leetcode.cn id=1175 lang=python3
#
# [1175] 质数排列
#
# 请你帮忙给从 1 到 n 的数设计排列方案，使得所有的「质数」都应该被放在「质数索引」（索引从 1 开始）上；你需要返回可能的方案总数。

# 让我们一起来回顾一下「质数」：质数一定是大于 1 的，并且不能用两个小于它的正整数的乘积来表示。

# 由于答案可能会很大，所以请你返回答案 模 mod 10 ^ 9 + 7 之后的结果即可。


# 示例 1：
# 输入：n = 5
# 输出：12
# 解释：举个例子，[1, 2, 5, 4, 3] 是一个有效的排列，但[5, 2, 3, 4, 1] 不是，因为在第二种情况里质数 5 被错误地放在索引为 1 的位置上。

# 示例 2：
# 输入：n = 100
# 输出：682289015


# 提示：
# 1 <= n <= 100

# @lc code=start
from math import sqrt
from functools import reduce


class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        # 首先看1到n有多少个质数，剩下的数就是全排列

        def isPrime(num: int) -> bool:
            if num <= 1:
                return False
            for i in range(2, int(sqrt(num)) + 1):
                if num % i == 0:
                    return False
            return True

        def factorial(n: int) -> int:
            return reduce(lambda x, y: x*y, range(1, n+1)) if n > 1 else 1

        numPrimes = sum((1 if isPrime(i) else 0) for i in range(1, n + 1))

        return factorial(numPrimes) * factorial(n - numPrimes) % MOD

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.numPrimeArrangements(1))  # 1
    print(solution.numPrimeArrangements(100))  # 682289015
