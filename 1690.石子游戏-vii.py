#
# @lc app=leetcode.cn id=1690 lang=python3
#
# [1690] 石子游戏 VII
#
# 石子游戏中，爱丽丝和鲍勃轮流进行自己的回合，爱丽丝先开始 。

# 有 n 块石子排成一排。每个玩家的回合中，可以从行中 移除 最左边的石头或最右边的石头，并获得与该行中剩余石头值之 和 相等的得分。当没有石头可移除时，得分较高者获胜。

# 鲍勃发现他总是输掉游戏（可怜的鲍勃，他总是输），所以他决定尽力 减小得分的差值 。爱丽丝的目标是最大限度地 扩大得分的差值 。

# 给你一个整数数组 stones ，其中 stones[i] 表示 从左边开始 的第 i 个石头的值，如果爱丽丝和鲍勃都 发挥出最佳水平 ，请返回他们 得分的差值 。


# 示例 1：
# 输入：stones = [5,3,1,4,2]
# 输出：6
# 解释：
# - 爱丽丝移除 2 ，得分 5 + 3 + 1 + 4 = 13 。游戏情况：爱丽丝 = 13 ，鲍勃 = 0 ，石子 = [5,3,1,4] 。
# - 鲍勃移除 5 ，得分 3 + 1 + 4 = 8 。游戏情况：爱丽丝 = 13 ，鲍勃 = 8 ，石子 = [3,1,4] 。
# - 爱丽丝移除 3 ，得分 1 + 4 = 5 。游戏情况：爱丽丝 = 18 ，鲍勃 = 8 ，石子 = [1,4] 。
# - 鲍勃移除 1 ，得分 4 。游戏情况：爱丽丝 = 18 ，鲍勃 = 12 ，石子 = [4] 。
# - 爱丽丝移除 4 ，得分 0 。游戏情况：爱丽丝 = 18 ，鲍勃 = 12 ，石子 = [] 。
# 得分的差值 18 - 12 = 6 。

# 示例 2：
# 输入：stones = [7,90,5,1,100,10,10,2]
# 输出：122

# 提示：
# n == stones.length
# 2 <= n <= 1000
# 1 <= stones[i] <= 1000

from itertools import accumulate
from typing import List
# @lc code=start
class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        # 动规
        preSum = [0] + list(accumulate(stones)) # 前缀和，方便求任意区间的合
        n = len(stones)
        # 记dp(i,j) 为剩余为stones[i:i+j]时，先手能拿到的最大差值，1 <= j <= n，
        # 有dp(i,1) = 0
        # 由dp(i,j) = max(preSum[i+j] - preSum[i+1] - dp(i+1, j-1), preSum[i+j-1] - preSum[i] - dp(i, j-1))
        # dp(*,j)只依赖dp（*,j-1)，状态可以压缩，dp(i, _)只后向依赖，迭代更新dp时可以从前往后更新
        dp = [0] * n # make a copy，完成dp(*, 1)的初始化
        for j in range(2, n+1):
            for i in range(n+1-j):
                dp[i] = max(preSum[i+j] - preSum[i+1] - dp[i+1], preSum[i+j-1] - preSum[i] - dp[i])

        return dp[0]
        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.stoneGameVII([5,3,1,4,2])) # 6
    print(solution.stoneGameVII([7,90,5,1,100,10,10,2])) # 122