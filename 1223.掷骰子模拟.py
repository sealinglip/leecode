#
# @lc app=leetcode.cn id=1223 lang=python3
#
# [1223] 掷骰子模拟
#
# 有一个骰子模拟器会每次投掷的时候生成一个 1 到 6 的随机数。

# 不过我们在使用它时有个约束，就是使得投掷骰子时，连续 掷出数字 i 的次数不能超过 rollMax[i]（i 从 1 开始编号）。

# 现在，给你一个整数数组 rollMax 和一个整数 n，请你来计算掷 n 次骰子可得到的不同点数序列的数量。

# 假如两个序列中至少存在一个元素不同，就认为这两个序列是不同的。由于答案可能很大，所以请返回 模 10 ^ 9 + 7 之后的结果。


# 示例 1：
# 输入：n = 2, rollMax = [1, 1, 2, 2, 2, 3]
# 输出：34
# 解释：我们掷 2 次骰子，如果没有约束的话，共有 6 * 6 = 36 种可能的组合。但是根据 rollMax 数组，数字 1 和 2 最多连续出现一次，所以不会出现序列(1, 1) 和(2, 2)。因此，最终答案是 36-2 = 34。

# 示例 2：
# 输入：n = 2, rollMax = [1, 1, 1, 1, 1, 1]
# 输出：30

# 示例 3：
# 输入：n = 3, rollMax = [1, 1, 1, 2, 2, 3]
# 输出：181


# 提示：
# 1 <= n <= 5000
# rollMax.length == 6
# 1 <= rollMax[i] <= 15

# Hard
# 复习

from collections import deque
from typing import List
# @lc code=start


class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        MOD = 10 ** 9 + 7
        ROLLMAX = 16  # important：这个不能是15
        dp = deque([[1] * 6])

        for _ in range(n-1):
            newDp = [sum(dp[0])] * 6
            # 减掉不合规的
            depth = len(dp)
            for j in range(6):
                if depth == rollMax[j]:
                    newDp[j] -= dp[rollMax[j] - 1][j]
                elif depth > rollMax[j]:
                    newDp[j] -= sum(dp[rollMax[j]]) - dp[rollMax[j]][j]

            dp.appendleft([d % MOD for d in newDp])
            if len(dp) > ROLLMAX:
                dp.pop()

        return sum(dp[0]) % MOD


        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.dieSimulator(100, [7, 5, 15, 5, 1, 7]))  # 797209093
    print(solution.dieSimulator(4, [2, 1, 1, 3, 3, 2]))  # 1082
    print(solution.dieSimulator(2, [1, 1, 2, 2, 2, 3]))  # 34
    print(solution.dieSimulator(2, [1, 1, 1, 1, 1, 1]))  # 30
    print(solution.dieSimulator(3, [1, 1, 1, 2, 2, 3]))  # 181
