#
# @lc app=leetcode.cn id=233 lang=python3
#
# [233] 数字 1 的个数
#
# 给定一个整数 n，计算所有小于等于 n 的非负整数中数字 1 出现的个数。

# 示例 1：
# 输入：n = 13
# 输出：6

# 示例 2：
# 输入：n = 0
# 输出：0

# 提示：
# 0 <= n <= 2 * 10^9

# Hard

# @lc code=start
class Solution:
    def countDigitOne(self, n: int) -> int:
        ns = str(n)[::-1]

        res = 0
        factor = 0
        accum = 0
        for i, d in enumerate(ns):
            magnitude = 10 ** i
            if d >= '1':
                digit = int(d)
                if digit == 1:
                    res += accum + 1
                else:
                    res += magnitude
                accum += digit * magnitude
                res += digit * factor

            factor += magnitude + factor * 9

        return res
# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    print(solution.countDigitOne(999))
    print(solution.countDigitOne(99))
    print(solution.countDigitOne(13))
    print(solution.countDigitOne(0))
