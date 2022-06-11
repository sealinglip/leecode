#
# @lc app=leetcode.cn id=829 lang=python3
#
# [829] 连续整数求和
#
# 给定一个正整数 n，返回 连续正整数满足所有数字之和为 n 的组数 。


# 示例 1:
# 输入: n = 5
# 输出: 2
# 解释: 5 = 2 + 3，共有两组连续整数([5], [2, 3])求和后为 5。

# 示例 2:
# 输入: n = 9
# 输出: 3
# 解释: 9 = 4 + 5 = 2 + 3 + 4

# 示例 3:
# 输入: n = 15
# 输出: 4
# 解释: 15 = 8 + 7 = 4 + 5 + 6 = 1 + 2 + 3 + 4 + 5


# 提示:
# 1 <= n <= 10^9

# Hard 有点水的难度
from math import sqrt

# @lc code=start


class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        # 组数
        # 自己肯定算一组
        # 如果是奇数，那么能拆成两个连续的数，偶数则不行
        # 能被3整除（大于3），能拆成三个数
        # 列式推理
        # 一个数能表达成i个连续的正整数的和
        # 它必须满足 n = i * x + i * (i - 1) / 2, x >= 1,

        return sum([0 if (n - ((i * (i-1)) >> 1)) %
                    i else 1 for i in range(2, int(sqrt((n << 1) + 0.25) - 0.5) + 1)], 1)

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.consecutiveNumbersSum(5))  # 2
    print(solution.consecutiveNumbersSum(9))  # 3
    print(solution.consecutiveNumbersSum(15))  # 4
