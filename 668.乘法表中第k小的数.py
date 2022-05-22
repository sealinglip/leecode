#
# @lc app=leetcode.cn id=668 lang=python3
#
# [668] 乘法表中第k小的数
#

# 几乎每一个人都用 乘法表。但是你能在乘法表中快速找到第k小的数字吗？

# 给定高度m 、宽度n 的一张 m * n的乘法表，以及正整数k，你需要返回表中第k 小的数字。

# 例 1：
# 输入: m = 3, n = 3, k = 5
# 输出: 3
# 解释:
# 乘法表:
# 1	2	3
# 2	4	6
# 3	6	9

# 第5小的数字是 3 (1, 2, 2, 3, 3).

# 例 2：
# 输入: m = 2, n = 3, k = 6
# 输出: 6
# 解释:
# 乘法表:
# 1	2	3
# 2	4	6

# 第6小的数字是 6 (1, 2, 2, 3, 4, 6).
# 注意：
# m 和 n 的范围在[1, 30000] 之间。
# k 的范围在[1, m * n] 之间。

# Hard

from bisect import bisect_left
# @lc code=start


class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        # 无理手
        return bisect_left(range(m * n), k, key=lambda x: x // n * n + sum(x // i for i in range(x // n + 1, m + 1)))
        # @lc code=end


if __name__ == "__main__":
    solution = Solution()
    print(solution.findKthNumber(3, 3, 5))
    print(solution.findKthNumber(2, 3, 6))
