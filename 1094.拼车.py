#
# @lc app=leetcode.cn id=1094 lang=python3
#
# [1094] 拼车
#
# 车上最初有 capacity 个空座位。车 只能 向一个方向行驶（也就是说，不允许掉头或改变方向）

# 给定整数 capacity 和一个数组 trips ,  trip[i] = [numPassengersi, fromi, toi] 表示第 i 次旅行有 numPassengersi 乘客，接他们和放他们的位置分别是 fromi 和 toi 。这些位置是从汽车的初始位置向东的公里数。

# 当且仅当你可以在所有给定的行程中接送所有乘客时，返回 true，否则请返回 false。

# 示例 1：
# 输入：trips = [[2,1,5],[3,3,7]], capacity = 4
# 输出：false

# 示例 2：
# 输入：trips = [[2,1,5],[3,3,7]], capacity = 5
# 输出：true
 

# 提示：
# 1 <= trips.length <= 1000
# trips[i].length == 3
# 1 <= numPassengersi <= 100
# 0 <= fromi < toi <= 1000
# 1 <= capacity <= 10^5

from typing import List
from heapq import *
# @lc code=start
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # 方法1
        # hq = []
        # trips.sort(key=lambda x: x[1]) # 按 from 排序
        # remaining = capacity # 剩余座位
        # for p, f, t in trips:
        #     while hq and hq[0][0] <= f:
        #         _, p1 = heappop(hq)
        #         remaining += p1
        #     if remaining < p:
        #         return False
        #     remaining -= p
        #     heappush(hq, (t, p))

        # return True
    
        # 方法2
        furthest = max(trip[2] for trip in trips)
        vacant = [0] * (furthest + 1)
        for p, f, t in trips:
            vacant[f] -= p
            vacant[t] += p

        remaining = capacity # 剩余座位
        for v in vacant:
            remaining += v
            if remaining < 0:
                return False
            
        return True
        

# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.carPooling([[3,2,8],[4,4,6],[10,8,9]], 11)) # True
    print(solution.carPooling([[2,1,5],[3,3,7]], 4)) # False
    print(solution.carPooling([[2,1,5],[3,3,7]], 5)) # True