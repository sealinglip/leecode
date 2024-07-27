#
# @lc app=leetcode.cn id=2589 lang=python3
#
# [2589] 完成所有任务的最少时间
#
# 你有一台电脑，它可以 同时 运行无数个任务。给你一个二维整数数组 tasks ，
# 其中 tasks[i] = [starti, endi, durationi] 表示第 i 个任务需要在 闭区间 
# 时间段 [starti, endi] 内运行 durationi 个整数时间点（但不需要连续）。
# 当电脑需要运行任务时，你可以打开电脑，如果空闲时，你可以将电脑关闭。
# 请你返回完成所有任务的情况下，电脑最少需要运行多少秒。


# 示例 1：
# 输入：tasks = [[2,3,1],[4,5,1],[1,5,2]]
# 输出：2
# 解释：
# - 第一个任务在闭区间 [2, 2] 运行。
# - 第二个任务在闭区间 [5, 5] 运行。
# - 第三个任务在闭区间 [2, 2] 和 [5, 5] 运行。
# 电脑总共运行 2 个整数时间点。

# 示例 2：
# 输入：tasks = [[1,3,2],[2,5,3],[5,6,2]]
# 输出：4
# 解释：
# - 第一个任务在闭区间 [2, 3] 运行
# - 第二个任务在闭区间 [2, 3] 和 [5, 5] 运行。
# - 第三个任务在闭区间 [5, 6] 运行。
# 电脑总共运行 4 个整数时间点。
 

# 提示：
# 1 <= tasks.length <= 2000
# tasks[i].length == 3
# 1 <= starti, endi <= 2000
# 1 <= durationi <= endi - starti + 1 

# Hard
# 复习

from typing import List
# @lc code=start
class Solution:
    def findMinimumTime(self, tasks: List[List[int]]) -> int:
        # 贪心
        # 将任务按结束时间升序排列
        tasks.sort(key=lambda t: t[1])
        runs = [0] * (tasks[-1][1] + 1) # 记录整点安不安排运行，0不运行，1运行
        res = 0
        for s, e, d in tasks:
            d -= sum(runs[s:e+1]) # 减掉已经安排运行的整点
            if d > 0:
                res += d # 不够的得安排，策略是从后往前，找还没安排的点
                for i in range(e, s-1, -1):
                    if d <= 0:
                        break
                    if runs[i] == 0:
                        runs[i] = 1
                        d -= 1

        return res
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.findMinimumTime([[2,3,1],[4,5,1],[1,5,2]])) # 2
    print(solution.findMinimumTime([[1,3,2],[2,5,3],[5,6,2]])) # 4