#
# @lc app=leetcode.cn id=1155 lang=python3
#
# [1155] 掷骰子等于目标和的方法数
#
# 这里有 n 个一样的骰子，每个骰子上都有 k 个面，分别标号为 1 到 k 。

# 给定三个整数 n,  k 和 target ，返回可能的方式(从总共 kn 种方式中)滚动骰子的数量，使正面朝上的数字之和等于 target 。

# 答案可能很大，你需要对 10^9 + 7 取模 。


# 示例 1：
# 输入：n = 1, k = 6, target = 3
# 输出：1
# 解释：你扔一个有 6 个面的骰子。
# 得到 3 的和只有一种方法。

# 示例 2：
# 输入：n = 2, k = 6, target = 7
# 输出：6
# 解释：你扔两个骰子，每个骰子有 6 个面。
# 得到 7 的和有 6 种方法：1+6 2+5 3+4 4+3 5+2 6+1。

# 示例 3：
# 输入：n = 30, k = 30, target = 500
# 输出：222616187
# 解释：返回的结果必须是对 10^9 + 7 取模。


# 提示：
# 1 <= n, k <= 30
# 1 <= target <= 1000


# @lc code=start
from functools import cache


class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10 ** 9 + 7

        @cache
        def dfs(num: int, target: int) -> int:
            '''
            返回num个骰子，向上数字和为target的可能数，按MOD取模
            '''
            if num > target or (num == 1 and target > k):
                return 0
            elif num == target or num == 1:
                return 1
            else:
                res = 0
                for i in range(1, min(k+1, target-num+2)):
                    res += dfs(num - 1, target - i)
                return res % MOD

        return dfs(n, target)
# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    print(solution.numRollsToTarget(1, 6, 3))  # 1
    print(solution.numRollsToTarget(2, 6, 7))  # 6
    print(solution.numRollsToTarget(30, 30, 500))  # 222616187
