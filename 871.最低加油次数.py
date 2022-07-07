#
# @lc app=leetcode.cn id=871 lang=python3
#
# [871] 最低加油次数
#
# 汽车从起点出发驶向目的地，该目的地位于出发位置东面 target 英里处。

# 沿途有加油站，每个 station[i] 代表一个加油站，它位于出发位置东面 station[i][0] 英里处，并且有 station[i][1] 升汽油。

# 假设汽车油箱的容量是无限的，其中最初有 startFuel 升燃料。它每行驶 1 英里就会用掉 1 升汽油。

# 当汽车到达加油站时，它可能停下来加油，将所有汽油从加油站转移到汽车中。

# 为了到达目的地，汽车所必要的最低加油次数是多少？如果无法到达目的地，则返回 - 1 。

# 注意：如果汽车到达加油站时剩余燃料为 0，它仍然可以在那里加油。如果汽车到达目的地时剩余燃料为 0，仍然认为它已经到达目的地。


# 示例 1：
# 输入：target = 1, startFuel = 1, stations = []
# 输出：0
# 解释：我们可以在不加油的情况下到达目的地。

# 示例 2：
# 输入：target = 100, startFuel = 1, stations = [[10, 100]]
# 输出：- 1
# 解释：我们无法抵达目的地，甚至无法到达第一个加油站。

# 示例 3：
# 输入：target = 100, startFuel = 10, stations = [[10, 60], [20, 30], [30, 30], [60, 40]]
# 输出：2
# 解释：
# 我们出发时有 10 升燃料。
# 我们开车来到距起点 10 英里处的加油站，消耗 10 升燃料。将汽油从 0 升加到 60 升。
# 然后，我们从 10 英里处的加油站开到 60 英里处的加油站（消耗 50 升燃料），
# 并将汽油从 10 升加到 50 升。然后我们开车抵达目的地。
# 我们沿途在1两个加油站停靠，所以返回 2 。


# 提示：
# 1 <= target, startFuel, stations[i][1] <= 10 ^ 9
# 0 <= stations.length <= 500
# 0 < stations[0][0] < stations[1][0] < ... < stations[stations.length-1][0] < target

# Hard
# 复习
from functools import cache
from typing import List
import heapq
# @lc code=start


class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        SL = len(stations)
        if SL == 0:
            return -1 if target > startFuel else 0

        # 动规
        # 下面的解法会TLE
        # 汽车到达某加油站时，要么加油，要么不加油；加油的话要加满
        # 记dp(s, i)为当汽车到达第i个加油站，油为s时，后续最少加油次数
        # 则有 dp(s, i) = min(dp(s - stations[i+1][0] + stations[i][0], i + 1), dp(s - stations[i+1][0] + stations[i][0] + stations[i][1], i + 1) + 1)
        # dp(s, stations.length-1) = INF if s + stations[stations.length-1][1] < target - stations[stations.length-1][0] else (1 if s < target - stations[stations.length-1][0] else 0)

        # INF = float('inf')
        # @cache
        # def dp(s, i) -> int:
        #     print("df(%d, %d)" % (s, i))
        #     if s < 0:
        #         return INF
        #     elif i == SL - 1:
        #         distance = target - stations[SL - 1][0]
        #         if s + stations[SL - 1][1] < distance:
        #             return INF
        #         elif s < distance:
        #             return 1
        #         else:
        #             return 0
        #     else:
        #         distance = stations[i+1][0] - stations[i][0]
        #         return min(dp(s - distance, i + 1), dp(s - distance + stations[i][1], i + 1) + 1)

        # cnt = dp(startFuel-stations[0][0], 0)
        # return -1 if cnt == INF else cnt

        # 优先队列
        hq = []
        remainFuel = startFuel  # 当前剩余油
        pos = 0
        cnt = 0
        while remainFuel < target:
            for i in range(pos, SL):
                if remainFuel >= stations[i][0]:  # 够得到这个站
                    # 把油拿上
                    heapq.heappush(hq, -stations[i][1])  # 小顶堆，所以转成负数
                    pos += 1
                else:
                    break
            if remainFuel < target:
                if not hq:  # 没油可加
                    return -1
                fuel = -heapq.heappop(hq)
                remainFuel += fuel
                cnt += 1

        return cnt

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    # 最早写的动规算法算下面这个case，耗时长（本地能算出来，但提交判不过），验证不通过
    print(solution.minRefuelStops(1000000, 80302, [[52821, 311929], [57329, 447457], [106585, 431610], [404402, 328190], [424591, 285021], [425838, 372155], [434324, 103429], [492839, 9269], [493388, 343058], [502052, 196352], [522295, 202890], [
          555617, 76688], [593726, 98030], [617465, 280095], [634894, 205270], [647642, 477117], [658775, 277494], [659802, 153477], [673423, 168675], [738516, 10001], [907525, 399694], [916595, 1215], [930008, 373854], [946106, 32543], [969696, 70443]]))  # 3
    print(solution.minRefuelStops(1, 1, []))  # 0
    print(solution.minRefuelStops(100, 1, [[10, 100]]))  # -1
    print(solution.minRefuelStops(100, 50, [[25, 30]]))  # -1
