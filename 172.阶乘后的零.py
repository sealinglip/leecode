#
# @lc app=leetcode.cn id=172 lang=python3
#
# [172] 阶乘后的零
#
# 给定一个整数 n ，返回 n! 结果中尾随零的数量。

# 提示 n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1


# 示例 1：
# 输入：n = 3
# 输出：0
# 解释：3! = 6 ，不含尾随 0

# 示例 2：
# 输入：n = 5
# 输出：1
# 解释：5! = 120 ，有一个尾随 0

# 示例 3：
# 输入：n = 0
# 输出：0

# 提示：
# 0 <= n <= 10^4


# 进阶：你可以设计并实现对数时间复杂度的算法来解决此问题吗？


# @lc code=start
class Solution:
    def trailingZeroes(self, n: int) -> int:
        cnt = 0
        while n > 4:
            n //= 5
            cnt += n
        return cnt


        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.trailingZeroes(3))  # 6
    print(solution.trailingZeroes(5))  # 120
    print(solution.trailingZeroes(0))  # 0
