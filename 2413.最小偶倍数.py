#
# @lc app=leetcode.cn id=2413 lang=python3
#
# [2413] 最小偶倍数
#
# 给你一个正整数 n ，返回 2 和 n 的最小公倍数（正整数）。


# 示例 1：
# 输入：n = 5
# 输出：10
# 解释：5 和 2 的最小公倍数是 10 。

# 示例 2：
# 输入：n = 6
# 输出：6
# 解释：6 和 2 的最小公倍数是 6 。注意数字会是它自身的倍数。


# 提示：
# 1 <= n <= 150

# @lc code=start
class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        return n if n & 1 == 0 else (n << 1)
        # @lc code=end


if __name__ == "__main__":
    solution = Solution()
    print(solution.smallestEvenMultiple(5))  # 10
    print(solution.smallestEvenMultiple(6))  # 6
