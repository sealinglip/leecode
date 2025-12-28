#
# @lc app=leetcode.cn id=2054 lang=python3
#
# [2054] 两个最好的不重叠活动
#
# https://leetcode.cn/problems/two-best-non-overlapping-events/description/
#
# algorithms
# Medium (41.41%)
# Likes:    71
# Dislikes: 0
# Total Accepted:    8.5K
# Total Submissions: 18.7K
# Testcase Example:  '[[1,3,2],[4,5,2],[2,4,3]]'
#
# 给你一个下标从 0 开始的二维整数数组 events ，其中 events[i] = [startTimei, endTimei, valuei] 。第
# i 个活动开始于 startTimei ，结束于 endTimei ，如果你参加这个活动，那么你可以得到价值 valuei 。你 最多 可以参加
# 两个时间不重叠 活动，使得它们的价值之和 最大 。
# 
# 请你返回价值之和的 最大值 。
# 
# 注意，活动的开始时间和结束时间是 包括在活动时间内的，也就是说，你不能参加两个活动且它们之一的开始时间等于另一个活动的结束时间。
# 更具体的，如果你参加一个活动，且结束时间为 t，那么下一个活动必须在 t + 1 或之后的时间开始。
# 
# 
# 示例 1:
# 输入：events = [[1,3,2],[4,5,2],[2,4,3]]
# 输出：4
# 解释：选择绿色的活动 0 和 1 ，价值之和为 2 + 2 = 4 。
# 
# 示例 2：
# 输入：events = [[1,3,2],[4,5,2],[1,5,5]]
# 输出：5
# 解释：选择活动 2 ，价值和为 5 。
# 
# 示例 3：
# 输入：events = [[1,5,3],[1,5,1],[6,6,5]]
# 输出：8
# 解释：选择活动 0 和 2 ，价值之和为 3 + 5 = 8 。
# 
# 
# 提示：
# 2 <= events.length <= 10^5
# events[i].length == 3
# 1 <= startTimei <= endTimei <= 10^9
# 1 <= valuei <= 10^6
# 
# 
#

from typing import List
# @lc code=start
class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        # 背包问题
        eArr = sorted((item for items in ([(e[0], 0, e[2]), (e[1], 1, e[2])] for e in events) for item in items), key=lambda e: (e[0], e[1]))
        res = bestFirst = 0
        for t, type, v in eArr:
            if type == 0:
                res = max(res, bestFirst + v)
            else:
                bestFirst = max(bestFirst, v)

        return res
        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.maxTwoEvents([[1,3,2],[4,5,2],[2,4,3]])) # 4
    print(solution.maxTwoEvents([[1,3,2],[4,5,2],[1,5,5]])) # 5
    print(solution.maxTwoEvents([[1,5,3],[1,5,1],[6,6,5]])) # 8
