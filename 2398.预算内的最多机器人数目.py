#
# @lc app=leetcode.cn id=2398 lang=python3
#
# [2398] 预算内的最多机器人数目
#
# 你有 n 个机器人，给你两个下标从 0 开始的整数数组 chargeTimes 和 runningCosts ，两者长度都为 n 。第 i 个机器人充电时间为 chargeTimes[i] 单位时间，花费 runningCosts[i] 单位时间运行。再给你一个整数 budget 。

# 运行 k 个机器人 总开销 是 max(chargeTimes) + k * sum(runningCosts) ，其中 max(chargeTimes) 是这 k 个机器人中最大充电时间，sum(runningCosts) 是这 k 个机器人的运行时间之和。

# 请你返回在 不超过 budget 的前提下，你 最多 可以 连续 运行的机器人数目为多少。


# 示例 1：
# 输入：chargeTimes = [3,6,1,3,4], runningCosts = [2,1,3,4,5], budget = 25
# 输出：3
# 解释：
# 可以在 budget 以内运行所有单个机器人或者连续运行 2 个机器人。
# 选择前 3 个机器人，可以得到答案最大值 3 。总开销是 max(3,6,1) + 3 * sum(2,1,3) = 6 + 3 * 6 = 24 ，小于 25 。
# 可以看出无法在 budget 以内连续运行超过 3 个机器人，所以我们返回 3 。

# 示例 2：
# 输入：chargeTimes = [11,12,19], runningCosts = [10,8,7], budget = 19
# 输出：0
# 解释：即使运行任何一个单个机器人，还是会超出 budget，所以我们返回 0 。
 
# 提示：
# chargeTimes.length == runningCosts.length == n
# 1 <= n <= 5 * 10^4
# 1 <= chargeTimes[i], runningCosts[i] <= 10^5
# 1 <= budget <= 10^15

# Hard
# 注：不是随意挑选机器人，要求是连续的机器人
# 复习

from collections import deque
from typing import List
# @lc code=start
class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        n = len(chargeTimes)
        runningCostSum = res = 0
        # 双指针 + 单调队列
        q, j = deque(), 0 # q为单调栈记录区间内最大chargeTimes，j记录区间左边界（初始为0）
        for i in range(n):
            runningCostSum += runningCosts[i]
            while q and chargeTimes[q[-1]] <= chargeTimes[i]:
                q.pop()
            q.append(i)
            while j <= i and (i-j+1) * runningCostSum + chargeTimes[q[0]] > budget:
                if q and q[0] == j:
                    q.popleft()
                runningCostSum -= runningCosts[j]
                j += 1
            res = max(res, i-j+1)

        return res

        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.maximumRobots([3,6,1,3,4], [2,1,3,4,5], 25)) # 3
    print(solution.maximumRobots([11,12,19], [10,8,7], 19)) # 0
