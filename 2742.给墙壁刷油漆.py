#
# @lc app=leetcode.cn id=2742 lang=python3
#
# [2742] 给墙壁刷油漆
#
# 给你两个长度为 n 下标从 0 开始的整数数组 cost 和 time ，分别表示给 n 堵不同的墙刷油漆需要的开销和时间。你有两名油漆匠：

# 一位需要 付费 的油漆匠，刷第 i 堵墙需要花费 time[i] 单位的时间，开销为 cost[i] 单位的钱。
# 一位 免费 的油漆匠，刷 任意 一堵墙的时间为 1 单位，开销为 0 。但是必须在付费油漆匠 工作 时，免费油漆匠才会工作。
# 请你返回刷完 n 堵墙最少开销为多少。


# 示例 1：
# 输入：cost = [1,2,3,2], time = [1,2,3,2]
# 输出：3
# 解释：下标为 0 和 1 的墙由付费油漆匠来刷，需要 3 单位时间。同时，免费油漆匠刷下标为 2 和 3 的墙，需要 2 单位时间，开销为 0 。总开销为 1 + 2 = 3 。

# 示例 2：
# 输入：cost = [2,3,4,2], time = [1,1,1,1]
# 输出：4
# 解释：下标为 0 和 3 的墙由付费油漆匠来刷，需要 2 单位时间。同时，免费油漆匠刷下标为 1 和 2 的墙，需要 2 单位时间，开销为 0 。总开销为 2 + 2 = 4 。
 

# 提示：
# 1 <= cost.length <= 500
# cost.length == time.length
# 1 <= cost[i] <= 10^6
# 1 <= time[i] <= 500

# Hard

# 贪心（不对，不保证求出最优解）
        # pairs = sorted(zip(cost, time), key=lambda i: (i[0] / i[1])) # 按单位成本升序排列
        # l = 0
        # r = n
        # res = 0
        # freeTimes = 0 # 可以使用免费油漆匠的次数
        # while l < r:
        #     if freeTimes > 0:
        #         r -= freeTimes
        #         if r <= l:
        #             break
        #         freeTimes = 0
        #     res += pairs[l][0]
        #     freeTimes += pairs[l][1]
        #     l += 1
        # return res

from math import inf
from typing import List
# @lc code=start
class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(cost)
        # 动规
        f = [0] + [inf] * (n + 1)
        for (c, t) in zip(cost, time):
            for j in range(n+1, -1, -1):
                f[min(j + t, n) + 1] = min(f[min(j + t, n) + 1], f[j] + c)
        return min(f[n], f[n + 1])
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.paintWalls([26,53,10,24,25,20,63,51], [1,1,1,1,2,2,2,1])) # 55
    print(solution.paintWalls([42,8,28,35,21,13,21,35], [2,1,1,1,2,1,1,2])) # 63
    print(solution.paintWalls([1,2,3,2], [1,2,3,2])) # 3
    print(solution.paintWalls([2,3,4,2], [1,1,1,1])) # 4