#
# @lc app=leetcode.cn id=1751 lang=python3
#
# [1751] 最多可以参加的会议数目 II
#
# https://leetcode.cn/problems/maximum-number-of-events-that-can-be-attended-ii/description/
#
# algorithms
# Hard (55.62%)
# Likes:    113
# Dislikes: 0
# Total Accepted:    10.6K
# Total Submissions: 18.3K
# Testcase Example:  '[[1,2,4],[3,4,3],[2,3,1]]\n2'
#
# 给你一个 events 数组，其中 events[i] = [startDayi, endDayi, valuei] ，表示第 i 个会议在
# startDayi 天开始，第 endDayi 天结束，如果你参加这个会议，你能得到价值 valuei 。同时给你一个整数 k
# 表示你能参加的最多会议数目。
# 
# 你同一时间只能参加一个会议。如果你选择参加某个会议，那么你必须 完整
# 地参加完这个会议。会议结束日期是包含在会议内的，也就是说你不能同时参加一个开始日期与另一个结束日期相同的两个会议。
# 
# 请你返回能得到的会议价值 最大和 。
# 
# 
# 示例 1：
# 输入：events = [[1,2,4],[3,4,3],[2,3,1]], k = 2
# 输出：7
# 解释：选择绿色的活动会议 0 和 1，得到总价值和为 4 + 3 = 7 。
# 
# 示例 2：
# 输入：events = [[1,2,4],[3,4,3],[2,3,10]], k = 2
# 输出：10
# 解释：参加会议 2 ，得到价值和为 10 。
# 你没法再参加别的会议了，因为跟会议 2 有重叠。你 不 需要参加满 k 个会议。
# 
# 示例 3：
# 输入：events = [[1,1,1],[2,2,2],[3,3,3],[4,4,4]], k = 3
# 输出：9
# 解释：尽管会议互不重叠，你只能参加 3 个会议，所以选择价值最大的 3 个会议。
# 
# 
# 提示：
# 1 <= k <= events.length
# 1 <= k * events.length <= 10^6 
# 1 <= startDayi <= endDayi <= 10^9
# 1 <= valuei <= 10^6
# 
# 复习
#

from bisect import bisect_left
from typing import List
# @lc code=start
class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        # 动规，🎒问题
        events.sort(key=lambda e: e[1]) # 按结束时间排序
        n = len(events)
        # 记dp(i,j) 为前i个会议中选j个参加能获得的最大价值
        # dp(i, 0) = 0
        # dp(i, j) = max(dp(i-1, j) + dp(l,j-1) + valuei)
        dp = [[0] * (k+1) for _ in range(n+1)]
        for i in range(n):
            s, _, v = events[i]
            l = bisect_left(events, s, hi = n - 1, key=lambda e: e[1]) # 在events[i]开始时间之前结束的会议有k个
            for j in range(1, k+1):
                dp[i+1][j] = max(dp[i][j], dp[l][j-1] + v)
        
        return dp[n][k]
        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.maxValue([[1,2,4],[3,4,3],[2,3,1]], 2)) # 7
    print(solution.maxValue([[1,2,4],[3,4,3],[2,3,10]], 2)) # 10
    print(solution.maxValue([[1,1,1],[2,2,2],[3,3,3],[4,4,4]], 3)) # 9
