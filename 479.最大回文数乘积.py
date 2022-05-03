#
# @lc app=leetcode.cn id=479 lang=python3
#
# [479] 最大回文数乘积
#
# 给定一个整数 n ，返回 可表示为两个 n 位整数乘积的 最大回文整数 。因为答案可能非常大，所以返回它对 1337 取余 。


# 示例 1:
# 输入：n = 2
# 输出：987
# 解释：99 x 91 = 9009, 9009 % 1337 = 987

# 示例 2:
# 输入： n = 1
# 输出： 9


# 提示:
# 1 <= n <= 8

# Hard

# @lc code=start
from math import ceil, sqrt

MOD = 1337


class Solution:
    def largestPalindrome(self, n: int) -> int:
        if n == 1:
            return 9
        upper = 10 ** n - 1  # 最大尝试数
        for i in range(upper, upper // 10, -1):
            left = str(i)
            p = int(left + left[::-1])
            root = ceil(sqrt(p))
            x = upper
            while x >= root:
                if p % x == 0:
                    return p % MOD
                x -= 1
# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    print(solution.largestPalindrome(2))  # 987
    print(solution.largestPalindrome(1))  # 9
