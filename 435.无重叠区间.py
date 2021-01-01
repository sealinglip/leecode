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

from typing import List
# @lc code=start


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        # 排序：按起点升序，终点降序
        intervals.sort(key=lambda interval: (interval[0] << 16) - interval[1])
        removal = 0
        rb = intervals[0][0]  # 初始右界
        prevRb = rb
        for interval in intervals:
            if rb <= interval[0]:
                prevRb = rb
                rb = interval[1]
            else:  # 删掉上一个或当前这个
                rb = min(rb, interval[1])
                removal += 1

        return removal

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]]))
    print(solution.eraseOverlapIntervals([[1, 2], [1, 2], [1, 2]]))
    print(solution.eraseOverlapIntervals([[1, 2], [2, 3]]))
