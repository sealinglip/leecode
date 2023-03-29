#
# @lc app=leetcode.cn id=1012 lang=python3
#
# [1012] 至少有 1 位重复的数字
#
# 给定正整数 n，返回在[1, n] 范围内具有 至少 1 位 重复数字的正整数的个数。

# 示例 1：
# 输入：n = 20
# 输出：1
# 解释：具有至少 1 位重复数字的正数（<= 20）只有 11 。

# 示例 2：
# 输入：n = 100
# 输出：10
# 解释：具有至少 1 位重复数字的正数（<= 100）有 11，22，33，44，55，66，77，88，99 和 100 。

# 示例 3：
# 输入：n = 1000
# 输出：262

# 提示：
# 1 <= n <= 10^9


# Hard
# @lc code=start
from math import perm


class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        # 总的数字数 减去 没有重复数字的数 ，就是答案
        # 所以我们可以先求出不重复数字的个数
        limit, s = list(map(int, str(n + 1))), set()
        l, res = len(limit), sum(9 * perm(9, i) for i in range(len(limit) - 1))

        for i, x in enumerate(limit):
            for y in range(i == 0, x):
                if y not in s:
                    res += perm(9 - i, l - i - 1)
            if x in s:
                break
            s.add(x)

        return n - res

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.numDupDigitsAtMostN(20))  # 1
    print(solution.numDupDigitsAtMostN(100))  # 10
    print(solution.numDupDigitsAtMostN(1000))  # 262
