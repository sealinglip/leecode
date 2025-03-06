#
# @lc app=leetcode.cn id=2209 lang=python3
#
# [2209] 用地毯覆盖后的最少白色砖块
#
# 给你一个下标从 0 开始的 二进制 字符串 floor ，它表示地板上砖块的颜色。

# floor[i] = '0' 表示地板上第 i 块砖块的颜色是 黑色 。
# floor[i] = '1' 表示地板上第 i 块砖块的颜色是 白色 。
# 同时给你 numCarpets 和 carpetLen 。你有 numCarpets 条 黑色 的地毯，每一条 黑色 的地毯长度都为 carpetLen 块砖块。请你使用这些地毯去覆盖砖块，使得未被覆盖的剩余 白色 砖块的数目 最小 。地毯相互之间可以覆盖。

# 请你返回没被覆盖的白色砖块的 最少 数目。


# 示例 1：
# 输入：floor = "10110101", numCarpets = 2, carpetLen = 2
# 输出：2
# 解释：
# 上图展示了剩余 2 块白色砖块的方案。
# 没有其他方案可以使未被覆盖的白色砖块少于 2 块。

# 示例 2：
# 输入：floor = "11111", numCarpets = 2, carpetLen = 3
# 输出：0
# 解释：
# 上图展示了所有白色砖块都被覆盖的一种方案。
# 注意，地毯相互之间可以覆盖。
 

# 提示：
# 1 <= carpetLen <= floor.length <= 1000
# floor[i] 要么是 '0' ，要么是 '1' 。
# 1 <= numCarpets <= 1000


# Hard
# @lc code=start
from itertools import accumulate


class Solution:
    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        n = len(floor)
        # 动规
        #
        # 记dp[i][j]为floor[:i]用j块地毯覆盖，最少剩余白色砖块数目
        # 边界条件
        # dp[i][0] = count(floor[:i], '1')
        # dp[0][*] = 0
        # 转移方程
        # dp[i][j] = min(dp[i-1][j] + int(floor[i] == '1'), dp[i-carpetLen][j-1])

        n = len(floor)
        if numCarpets * carpetLen >= n:
            return 0

        floor = list(map(int, floor))
        dp = list(accumulate(floor))
        for i in range(1, numCarpets + 1):
            newDp = [0] * n
            for j in range(carpetLen * i, n):
                newDp[j] = min(newDp[j - 1] + floor[j], dp[j - carpetLen])
            dp = newDp
        return dp[-1]

        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.minimumWhiteTiles("10110101", 2, 2)) # 2
    print(solution.minimumWhiteTiles("11111", 2, 3)) # 0
