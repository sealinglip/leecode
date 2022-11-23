#
# @lc app=leetcode.cn id=878 lang=python3
#
# [878] 第 N 个神奇数字
#
# 一个正整数如果能被 a 或 b 整除，那么它是神奇的。

# 给定三个整数 n, a, b ，返回第 n 个神奇的数字。因为答案可能很大，所以返回答案 对 10^9 + 7 取模 后的值。


# 示例 1：
# 输入：n = 1, a = 2, b = 3
# 输出：2

# 示例 2：
# 输入：n = 4, a = 2, b = 3
# 输出：6


# 提示：
# 1 <= n <= 10^9
# 2 <= a, b <= 4 * 10^4

# Hard

# @lc code=start
from math import lcm


class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        MOD = 10 ** 9 + 7

        def gcd(x, y):
            '''
            最小公约数
            '''
            while (y):
                x, y = y, x % y
            return abs(x)

        c = lcm(a, b)  # lcm为最小公倍数
        # 每个 lcm 就有 ( lcm // a + lcm // b - 1) 个神奇数
        g = c // a + c // b - 1
        times, rest = divmod(n, g)
        base = (c * times) % MOD
        if rest == 0:
            return base
        # 变成求第rest个神奇数，再加上base，对MOD求余
        guess = int((rest + 1) / g * c)
        cur = guess // a + guess // b
        an, bn = (guess // a * a), (guess // b * b)
        guess = max(an, bn)
        if cur != rest:
            dir = 1 if cur < rest else -1  # 逼近方向
            while cur > rest:
                cur += dir
                if guess == bn:
                    bn += dir * b
                else:
                    an += dir * a
                guess = max(an, bn)

        return (base + guess) % MOD


        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.nthMagicalNumber(1, 2, 3))  # 2
    print(solution.nthMagicalNumber(4, 2, 3))  # 6
