#
# @lc app=leetcode.cn id=507 lang=python3
#
# [507] 完美数
#
# 对于一个 正整数，如果它和除了它自身以外的所有 正因子 之和相等，我们称它为 「完美数」。
# 给定一个 整数 n， 如果是完美数，返回 true，否则返回 false


# 示例 1：
# 输入：num = 28
# 输出：true
# 解释：28 = 1 + 2 + 4 + 7 + 14
# 1, 2, 4, 7, 和 14 是 28 的所有正因子。

# 示例 2：
# 输入：num = 6
# 输出：true

# 示例 3：
# 输入：num = 496
# 输出：true

# 示例 4：
# 输入：num = 8128
# 输出：true

# 示例 5：
# 输入：num = 2
# 输出：false


# 提示：
# 1 <= num <= 10^8

# @lc code=start
from math import sqrt


class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False
        s = 1
        r = sqrt(num)
        for i in range(2, int(r) + 1):
            if num % i == 0:
                s += i
                if i < r:
                    s += num // i
        return s == num

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.checkPerfectNumber(28))  # True
    print(solution.checkPerfectNumber(6))  # True
    print(solution.checkPerfectNumber(496))  # True
    print(solution.checkPerfectNumber(8128))  # True
    print(solution.checkPerfectNumber(2))  # False
    print(solution.checkPerfectNumber(1))  # False
