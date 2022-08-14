#
# @lc app=leetcode.cn id=473 lang=python3
#
# [473] 火柴拼正方形
#
# 你将得到一个整数数组 matchsticks ，其中 matchsticks[i] 是第 i 个火柴棒的长度。你要用 所有的火柴棍 拼成一个正方形。你 不能折断 任何一根火柴棒，但你可以把它们连在一起，而且每根火柴棒必须 使用一次 。
# 如果你能使这个正方形，则返回 true ，否则返回 false 。


# 示例 1:
# 输入: matchsticks = [1, 1, 2, 2, 2]
# 输出: true
# 解释: 能拼成一个边长为2的正方形，每边两根火柴。

# 示例 2:
# 输入: matchsticks = [3, 3, 3, 3, 4]
# 输出: false
# 解释: 不能用所有火柴拼成一个正方形。


# 提示:
# 1 <= matchsticks.length <= 15
# 1 <= matchsticks[i] <= 10^8

# 复习
from typing import List

# @lc code=start


class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        totalLen = sum(matchsticks)
        # totalLen必须是4的倍数
        if totalLen & 3:
            return False
        sideLen = totalLen >> 2  # 边长

        # 看这堆火柴棍能不能正好分四堆
        matchsticks.sort()
        if matchsticks[-1] > sideLen:  # 最长的超出边长
            return False

        # 记dp(x)
        # x的第i位代表第i根火柴有没有放置，放的话一根接一根绕着周长放
        # dp(x) 表示当前放置火柴的边的长度
        # 易知dp(0) = 0：什么都还没放，所以当前边长度为0
        # 如果 x1 &  (1 << k) == 0 (即第k根火柴还没放)
        # 且 dp(x1) + matchsticks[k] <= sideLen，那么
        # 有 dp(x1 | (1 << k)) = (dp(x1) + matchsticks[k]) % sideLen
        # 否则dp(x1 | (1 << k)) = -1 表示状态x | (1 << k)不成立
        # 如果dp((1 << len(matchsticks)) - 1) = 0，表示所有火柴都放下了，且刚好，则可以拼成正方形
        # 否则不行
        dp = [-1] * (1 << len(matchsticks))  # 初始都设为-1
        dp[0] = 0
        for x in range(1, len(dp)):
            for k, v in enumerate(matchsticks):
                if x & (1 << k) == 0:
                    continue
                x1 = x & ~(1 << k)  # 这等同于x1 加上第k根火柴为x
                if dp[x1] >= 0 and dp[x1] + v <= sideLen:
                    # 找到一种可行解
                    dp[x] = (dp[x1] + v) % sideLen
                    break

        return dp[-1] == 0

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.makesquare([1, 1, 2, 2, 2]))  # True
    print(solution.makesquare([3, 3, 3, 3, 4]))  # False
