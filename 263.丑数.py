#
# @lc app=leetcode.cn id=263 lang=python3
#
# [263] 丑数
#
# 给你一个整数 n ，请你判断 n 是否为 丑数 。如果是，返回 true ；否则，返回 false 。
# 丑数 就是只包含质因数 2、3 和/或 5 的正整数。

# 示例 1：
# 输入：n = 6
# 输出：true
# 解释：6 = 2 × 3

# 示例 2：
# 输入：n = 8
# 输出：true
# 解释：8 = 2 × 2 × 2

# 示例 3：
# 输入：n = 14
# 输出：false
# 解释：14 不是丑数，因为它包含了另外一个质因数 7 。

# 示例 4：
# 输入：n = 1
# 输出：true
# 解释：1 通常被视为丑数。

# 提示：
# -2^31 <= n <= 2^31 - 1

# @lc code=start
class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        elif n == 1:
            return True
        else:
            # 先消除2的因子
            while not (n & 1):
                n >>= 1
            # 再消除3的因子
            while (n % 3) == 0:
                n /= 3
            # 再消除5的因子
            while (n % 5) == 0:
                n /= 5
            return n == 1

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.isUgly(6))
    print(solution.isUgly(8))
    print(solution.isUgly(14))
    print(solution.isUgly(1))
