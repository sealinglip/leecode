#
# @lc app=leetcode.cn id=397 lang=python3
#
# [397] 整数替换
#
# 给定一个正整数 n ，你可以做如下操作：

# 如果 n 是偶数，则用 n / 2替换 n 。
# 如果 n 是奇数，则可以用 n + 1或n - 1替换 n 。
# n 变为 1 所需的最小替换次数是多少？


# 示例 1：
# 输入：n = 8
# 输出：3
# 解释：8 -> 4 -> 2 -> 1

# 示例 2：
# 输入：n = 7
# 输出：4
# 解释：7 -> 8 -> 4 -> 2 -> 1
# 或 7 -> 6 -> 3 -> 2 -> 1

# 示例 3：
# 输入：n = 4
# 输出：2


# 提示：
# 1 <= n <= 2^31 - 1

# @lc code=start
from functools import lru_cache


class Solution:
    def integerReplacement(self, n: int) -> int:
        @lru_cache(None)
        def minStep(num: int) -> int:
            if num & 1:
                if num == 1:
                    return 0
                else:
                    return 1 + min(minStep(num + 1), minStep(num - 1))
            else:
                return 1 + minStep(num >> 1)

        return minStep(n)

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.integerReplacement(8))  # 3
    print(solution.integerReplacement(7))  # 4
    print(solution.integerReplacement(4))  # 2
