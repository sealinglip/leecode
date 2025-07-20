#
# @lc app=leetcode.cn id=1353 lang=python3
#
# [1353] 最多可以参加的会议数目
#
# https://leetcode.cn/problems/maximum-number-of-events-that-can-be-attended/description/
#
# algorithms
# Medium (30.62%)
# Likes:    314
# Dislikes: 0
# Total Accepted:    27.1K
# Total Submissions: 83.6K
# Testcase Example:  '[[1,2],[2,3],[3,4]]'
#
# 给你一个数组 events，其中 events[i] = [startDayi, endDayi] ，表示会议 i 开始于 startDayi ，结束于 endDayi 。
# 
# 你可以在满足 startDayi <= d <= endDayi 中的任意一天 d 参加会议 i 。在任意一天 d 中只能参加一场会议。
# 请你返回你可以参加的 最大 会议数目。
# 
# 
# 示例 1：
# 输入：events = [[1,2],[2,3],[3,4]]
# 输出：3
# 解释：你可以参加所有的三个会议。
# 安排会议的一种方案如上图。
# 第 1 天参加第一个会议。
# 第 2 天参加第二个会议。
# 第 3 天参加第三个会议。
# 
# 示例 2：
# 输入：events= [[1,2],[2,3],[3,4],[1,2]]
# 输出：4
# 
# 
# 提示：​​​​​​
# 1 <= events.length <= 10^5
# events[i].length == 2
# 1 <= startDayi <= endDayi <= 10^5
# 
# 复习
#

from heapq import heappop, heappush
from typing import List
# @lc code=start
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        # 贪心
        # 先排序
        n = len(events)
        events.sort() # 先按startDay，再按endDay排序
        maxDay = max(e[1] for e in events)

        pq = []
        res = j = 0
        for i in range(1, maxDay+1):
            while j < n and events[j][0] <= i:
                heappush(pq, events[j][1])
                j += 1
            while pq and pq[0] < i:
                heappop(pq)
            if pq:
                heappop(pq)
                res += 1
        
        return res
        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.maxEvents([[1,5],[1,5],[1,5],[2,3],[2,3]])) # 5
    print(solution.maxEvents([[1,2],[1,2],[3,3],[1,5],[1,5]])) # 5
    print(solution.maxEvents([[1,2],[2,3],[3,4]])) # 3
    print(solution.maxEvents([[1,2],[2,3],[3,4],[1,2]])) # 4
