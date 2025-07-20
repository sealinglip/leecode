#
# @lc app=leetcode.cn id=3439 lang=python3
#
# [3439] 重新安排会议得到最多空余时间 I
#
# https://leetcode.cn/problems/reschedule-meetings-for-maximum-free-time-i/description/
#
# algorithms
# Medium (50.39%)
# Likes:    32
# Dislikes: 0
# Total Accepted:    7.8K
# Total Submissions: 13.4K
# Testcase Example:  '5\n1\n[1,3]\n[2,5]'
#
# 给你一个整数 eventTime 表示一个活动的总时长，这个活动开始于 t = 0 ，结束于 t = eventTime 。
# 
# 同时给你两个长度为 n 的整数数组 startTime 和 endTime 。它们表示这次活动中 n 个时间 没有重叠 的会议，其中第 i 个会议的时间为[startTime[i], endTime[i]] 。
# 
# 你可以重新安排 至多 k 个会议，安排的规则是将会议时间平移，且保持原来的 会议时长 ，你的目的是移动会议后 最大化 相邻两个会议之间的 最长
# 连续空余时间。
# 
# 移动前后所有会议之间的 相对 顺序需要保持不变，而且会议时间也需要保持互不重叠。
# 
# 请你返回重新安排会议以后，可以得到的 最大 空余时间。
# 
# 注意，会议 不能 安排到整个活动的时间以外。
# 
# 
# 示例 1：
# 输入：eventTime = 5, k = 1, startTime = [1,3], endTime = [2,5]
# 输出：2
# 解释：
# 将 [1, 2] 的会议安排到 [2, 3] ，得到空余时间 [0, 2] 。
# 
# 示例 2：
# 输入：eventTime = 10, k = 1, startTime = [0,2,9], endTime = [1,4,10]
# 输出：6
# 解释：
# 将 [2, 4] 的会议安排到 [1, 3] ，得到空余时间 [3, 9] 。
# 
# 示例 3：
# 输入：eventTime = 5, k = 2, startTime = [0,1,2,3,4], endTime = [1,2,3,4,5]
# 输出：0
# 解释：
# 活动中的所有时间都被会议安排满了。
# 
# 
# 提示：
# 1 <= eventTime <= 10^9
# n == startTime.length == endTime.length
# 2 <= n <= 10^5
# 1 <= k <= n
# 0 <= startTime[i] < endTime[i] <= eventTime
# endTime[i] <= startTime[i + 1] 其中 i 在范围 [0, n - 2] 之间。
# 
#

from typing import List
# @lc code=start
class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        res = accumGap = startTime[0]
        j = k - 1
        for i in range(n):
            accumGap += (eventTime if i == n-1 else startTime[i+1]) - endTime[i]
            if i >= j:
                res = max(res, accumGap)
                accumGap -= startTime[i-j] - (0 if i==j else endTime[i-k])

        return res
        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.maxFreeTime(34, 2, [0,17], [14,19])) # 18
    print(solution.maxFreeTime(21, 2, [18,20], [20,21])) # 18
    print(solution.maxFreeTime(5, 1, [1,3], [2,5])) # 2
    print(solution.maxFreeTime(10, 1, [0,2,9], [1,4,10])) # 6
    print(solution.maxFreeTime(5, 2, [0,1,2,3,4], [1,2,3,4,5])) # 0
