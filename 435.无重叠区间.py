#
# @lc app=leetcode.cn id=435 lang=python3
#
# [435] 无重叠区间
#
# 给定一个区间的集合，找到需要移除区间的最小数量，使剩余区间互不重叠。

# 注意:
# 可以认为区间的终点总是大于它的起点。
# 区间[1, 2] 和[2, 3] 的边界相互“接触”，但没有相互重叠。

# 示例 1:
# 输入: [[1, 2], [2, 3], [3, 4], [1, 3]]
# 输出: 1
# 解释: 移除[1, 3] 后，剩下的区间没有重叠。

# 示例 2:
# 输入: [[1, 2], [1, 2], [1, 2]]
# 输出: 2
# 解释: 你需要移除两个[1, 2] 来使剩下的区间没有重叠。

# 示例 3:
# 输入: [[1, 2], [2, 3]]
# 输出: 0
# 解释: 你不需要移除任何区间，因为它们已经是无重叠的了。

# 提示:
# 1 <= intervals.length <= 10^5
# intervals[i].length == 2
# -5 * 10^4 <= starti < endi <= 5 * 10^4

# 复习
from typing import List
# @lc code=start


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        # 排序：按起点升序，终点降序
        # intervals.sort(key=lambda interval: (interval[0] << 16) - interval[1])
        # removal = 0
        # rb = intervals[0][0]  # 以最小起点当初始右界
        # prevRb = rb
        # for interval in intervals:
        #     if rb <= interval[0]:
        #         prevRb = rb
        #         rb = interval[1]
        #     else:  # 删掉上一个或当前这个
        #         rb = min(rb, interval[1])  # 肯定删跨度大的
        #         removal += 1

        # return removal

        # 上面算法不够间接，可以用更精准的贪心
        intervals.sort(key=lambda interval: interval[1])  # 按终点升序
        chain = 1  # chain记录最长的不重叠区间序列
        rb = intervals[0][1]
        n = len(intervals)

        for i in range(1, n):
            if intervals[i][0] >= rb:  # 可以拼到不重叠区间序列中
                rb = intervals[i][1]
                chain += 1

        return n - chain

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    # print(solution.eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]]))
    # print(solution.eraseOverlapIntervals([[1, 2], [1, 2], [1, 2]]))
    print(solution.eraseOverlapIntervals([[1, 2], [2, 3]]))
