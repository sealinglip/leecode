#
# @lc app=leetcode.cn id=1780 lang=python3
#
# [1780] 判断一个数字是否可以表示成三的幂的和
#
# 给你一个整数 n ，如果你可以将 n 表示成若干个不同的三的幂之和，请你返回 true ，否则请返回 false 。

# 对于一个整数 y ，如果存在整数 x 满足 y == 3x ，我们称这个整数 y 是三的幂。


# 示例 1：
# 输入：n = 12
# 输出：true
# 解释：12 = 3^1 + 3^2

# 示例 2：
# 输入：n = 91
# 输出：true
# 解释：91 = 3^0 + 3^2 + 3^4

# 示例 3：
# 输入：n = 21
# 输出：false


# 提示：
# 1 <= n <= 10^7

# @lc code=start


from bisect import bisect_left

# 3 ^ 14 < 10 ^ 7 < 3 ^ 15
TRI_POWER = [3 ** i for i in range(15)]


class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        # 要求不同的数字
        used = set()
        while n > 0:
            i = bisect_left(TRI_POWER, n)
            if i < len(TRI_POWER) and TRI_POWER[i] == n:
                return i not in used
            if i-1 in used:
                return False
            used.add(i-1)
            n -= TRI_POWER[i-1]
        return False


# @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.checkPowersOfThree(4782972))  # True
    print(solution.checkPowersOfThree(4852229))  # False
    print(solution.checkPowersOfThree(11))  # False
    print(solution.checkPowersOfThree(12))  # True
    print(solution.checkPowersOfThree(91))  # True
    print(solution.checkPowersOfThree(21))  # False
