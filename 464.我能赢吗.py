#
# @lc app=leetcode.cn id=464 lang=python3
#
# [464] 我能赢吗
#
# 在 "100 game" 这个游戏中，两名玩家轮流选择从 1 到 10 的任意整数，累计整数和，先使得累计整数和 达到或超过  100 的玩家，即为胜者。

# 如果我们将游戏规则改为 “玩家 不能 重复使用整数” 呢？

# 例如，两个玩家可以轮流从公共整数池中抽取从 1 到 15 的整数（不放回），直到累计整数和 >= 100。

# 给定两个整数 maxChoosableInteger （整数池中可选择的最大数）和 desiredTotal（累计和），若先出手的玩家是否能稳赢则返回 true ，否则返回 false 。假设两位玩家游戏时都表现 最佳 。


# 示例 1：
# 输入：maxChoosableInteger = 10, desiredTotal = 11
# 输出：false
# 解释：
# 无论第一个玩家选择哪个整数，他都会失败。
# 第一个玩家可以选择从 1 到 10 的整数。
# 如果第一个玩家选择 1，那么第二个玩家只能选择从 2 到 10 的整数。
# 第二个玩家可以通过选择整数 10（那么累积和为 11 >= desiredTotal），从而取得胜利.
# 同样地，第一个玩家选择任意其他整数，第二个玩家都会赢。

# 示例 2:
# 输入：maxChoosableInteger = 10, desiredTotal = 0
# 输出：true

# 示例 3:
# 输入：maxChoosableInteger = 10, desiredTotal = 1
# 输出：true


# 提示:
# 1 <= maxChoosableInteger <= 20
# 0 <= desiredTotal <= 300

# @lc code=start
from functools import cache


class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        # 如果所有的数加起来都不能超过desiredTotal，直接返回False
        if desiredTotal > maxChoosableInteger * (maxChoosableInteger + 1) // 2:
            return False
        # 动态规划
        # 记ca为当前可选数字集
        # mask代表还有哪些数字可用
        # canIWin(mask, d) = any([not canIWin(mask', d-i-1) for i in range(maxChoosableInteger) if ((1 << i) & mask) != 0])
        # 其中：mask' = mask ^ (1 << i)
        # 边界条件是 canIWin(mask, d) = True if d <= 0, canIWin(mask, d) = False if mask == 0 and d > 0

        # 初始mask
        mask = (1 << maxChoosableInteger) - 1

        @cache
        def dp(m: int, d: int) -> bool:
            if d <= 0:
                return True
            else:
                if m == 0:
                    return False
                else:
                    for i in range(maxChoosableInteger-1, -1, -1):
                        t = 1 << i
                        if (m & t) != 0 and (i + 1 >= d or not dp(m ^ t, d - i - 1)):
                            return True
                    return False
        return dp(mask, desiredTotal)
# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    print(solution.canIWin(20, 189))  # False
    print(solution.canIWin(5, 50))  # False
    print(solution.canIWin(10, 11))  # False
    print(solution.canIWin(10, 30))  # True
    print(solution.canIWin(10, 0))  # True
    print(solution.canIWin(10, 1))  # True
