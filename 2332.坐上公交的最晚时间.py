#
# @lc app=leetcode.cn id=2332 lang=python3
#
# [2332] 坐上公交的最晚时间
#
# 给你一个下标从 0 开始长度为 n 的整数数组 buses ，其中 buses[i] 表示第 i 辆公交车的出发时间。同时给你一个下标从 0 开始长度为 m 的整数数组 passengers ，其中 passengers[j] 表示第 j 位乘客的到达时间。所有公交车出发的时间互不相同，所有乘客到达的时间也互不相同。

# 给你一个整数 capacity ，表示每辆公交车 最多 能容纳的乘客数目。

# 每位乘客都会搭乘下一辆有座位的公交车。如果你在 y 时刻到达，公交在 x 时刻出发，满足 y <= x  且公交没有满，那么你可以搭乘这一辆公交。最早 到达的乘客优先上车。

# 返回你可以搭乘公交车的最晚到达公交站时间。你 不能 跟别的乘客同时刻到达。

# 注意：数组 buses 和 passengers 不一定是有序的。


# 示例 1：
# 输入：buses = [10,20], passengers = [2,17,18,19], capacity = 2
# 输出：16
# 解释：
# 第 1 辆公交车载着第 1 位乘客。
# 第 2 辆公交车载着你和第 2 位乘客。
# 注意你不能跟其他乘客同一时间到达，所以你必须在第二位乘客之前到达。

# 示例 2：
# 输入：buses = [20,30,10], passengers = [19,13,26,4,25,11,21], capacity = 2
# 输出：20
# 解释：
# 第 1 辆公交车载着第 4 位乘客。
# 第 2 辆公交车载着第 6 位和第 2 位乘客。
# 第 3 辆公交车载着第 1 位乘客和你。
 

# 提示：
# n == buses.length
# m == passengers.length
# 1 <= n, m, capacity <= 10^5
# 2 <= buses[i], passengers[i] <= 10^9
# buses 中的元素 互不相同 。
# passengers 中的元素 互不相同 。

from typing import List
# @lc code=start
class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        buses.sort()
        passengers.sort()
        n, m = len(buses), len(passengers)

        pi = 0 # 指针
        t = -1
        for i, b in enumerate(buses):
            cnt = 0
            while cnt < capacity and pi < m and passengers[pi] <= b:
                pi += 1
                cnt += 1
            if pi == m and (i < (n-1) or cnt < capacity):
                t = buses[-1]
                break
            if i == n-1:
                # 最后一辆车了，必须安排一下了
                if cnt == capacity:
                    t = passengers[pi-1]-1
                else:
                    t = b
                break

        # 不能和其他乘客同时到，要错开时间
        s = set(passengers)
        while t in s:
            t -= 1
        return t

# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.latestTimeCatchTheBus([3], [2,4], 2)) # 3
    print(solution.latestTimeCatchTheBus([3], [2,3,4], 2)) # 1
    print(solution.latestTimeCatchTheBus([10,20], [2,17,18,19], 2)) # 16
    print(solution.latestTimeCatchTheBus([20,30,10], [19,13,26,4,25,11,21], 2)) # 20
