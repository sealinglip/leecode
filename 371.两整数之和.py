#
# @lc app=leetcode.cn id=371 lang=python3
#
# [371] 两整数之和
#
# 给你两个整数 a 和 b ，不使用 运算符 + 和 - ​​​​​​​，计算并返回两整数之和。

# 示例 1：
# 输入：a = 1, b = 2
# 输出：3
# 示例 2：

# 输入：a = 2, b = 3
# 输出：5

# 提示：
# -1000 <= a, b <= 1000

# @lc code=start

class Solution:
    def getSum(self, a: int, b: int) -> int:
        # MAX UNSIGNED INT
        MAX_UINT = 1 << 32
        # MAX_INT
        MAX_INT = (1 << 31) - 1
        # NEGATIVE FLAG
        NEG_FLAG = 1 << 31
        while b:
            a, b = (a ^ b) % MAX_UINT, ((a & b) << 1) % MAX_UINT

        if a & NEG_FLAG:
            a = ~((a ^ NEG_FLAG) ^ MAX_INT)
        return a
# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    print(solution.getSum(-1, 1))  # 0
    print(solution.getSum(1, 2))  # 3
    print(solution.getSum(2, 3))  # 5
