#
# @lc app=leetcode.cn id=357 lang=python3
#
# [357] 计算各个位数不同的数字个数
#
# 给你一个整数 n ，统计并返回各位数字都不同的数字 x 的个数，其中 0 <= x < 10n 。


# 示例 1：
# 输入：n = 2
# 输出：91
# 解释：答案应为除去 11、22、33、44、55、66、77、88、99 外，在 0 ≤ x < 100 范围内的所有数字。

# 示例 2：
# 输入：n = 0
# 输出：1


# 提示：
# 0 <= n <= 8


# @lc code=start
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        elif n == 1:
            return 10
        res = 10
        cur = 9
        for i in range(n - 1):
            cur *= 9 - i
            res += cur
        return res
# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    print(solution.countNumbersWithUniqueDigits(2))  # 91
    print(solution.countNumbersWithUniqueDigits(0))  # 1
