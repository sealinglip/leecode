#
# @lc app=leetcode.cn id=1802 lang=python3
#
# [1802] 有界数组中指定下标处的最大值
#
# 给你三个正整数 n、index 和 maxSum 。你需要构造一个同时满足下述所有条件的数组 nums（下标 从 0 开始 计数）：

# nums.length == n
# nums[i] 是 正整数 ，其中 0 <= i < n
# abs(nums[i] - nums[i+1]) <= 1 ，其中 0 <= i < n-1
# nums 中所有元素之和不超过 maxSum
# nums[index] 的值被 最大化
# 返回你所构造的数组中的 nums[index] 。

# 注意：abs(x) 等于 x 的前提是 x >= 0 ；否则，abs(x) 等于 - x 。


# 示例 1：

# 输入：n = 4, index = 2,  maxSum = 6
# 输出：2
# 解释：数组[1, 1, 2, 1] 和[1, 2, 2, 1] 满足所有条件。不存在其他在指定下标处具有更大值的有效数组。
# 示例 2：

# 输入：n = 6, index = 1,  maxSum = 10
# 输出：3


# 提示：
# 1 <= n <= maxSum <= 10^9
# 0 <= index < n

# @lc code=start
from math import sqrt


class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        # 刨掉每个数都必须有的1之后，设 nums[index] 最大能到x
        # 它两边的位置依次递减到边界或到0
        # 所有的数加起来要 <= maxSum - n
        a, b = index, n - index - 1  # 前后的位置数
        if a > b:
            a, b = b, a

        maxSum -= n
        # 如果x够大，>= b，那边两边都能铺满
        # (a+b+1)x - (a^2+b^2+a+b) // 2 <= maxSum - n
        x = (maxSum + (a ** 2 + b ** 2 + a + b) // 2) / (a + b + 1)
        if x >= b:
            return int(x) + 1

        # 否则，假设不成立。a <= x < b
        # (x^2+(2a+1)x-a-a^2) // 2 <= maxSum - n
        delta = (2*a+1) ** 2 + 4 * (a + a ** 2 + 2 * maxSum)  # b^2-4ac
        if delta > 0:
            # 方程有解，要大的
            x = (-1-2*a + sqrt(delta)) / 2
            if a <= x < b:
                return int(x) + 1

        # x 够小 <a
        # x^2 <= maxSum - n
        return int(sqrt(maxSum)) + 1

        # @lc code=end


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxValue(4, 2, 6))  # 2
    print(solution.maxValue(6, 1, 10))  # 3
