#
# @lc app=leetcode.cn id=436 lang=python3
#
# [436] 寻找右区间
#
# 给你一个区间数组 intervals ，其中 intervals[i] = [starti, endi] ，且每个 starti 都 不同 。
# 区间 i 的 右侧区间 可以记作区间 j ，并满足 startj >= endi ，且 startj 最小化 。
# 返回一个由每个区间 i 的 右侧区间 的最小起始位置组成的数组。如果某个区间 i 不存在对应的 右侧区间 ，则下标 i 处的值设为 - 1 。


# 示例 1：
# 输入：intervals = [[1, 2]]
# 输出：[-1]
# 解释：集合中只有一个区间，所以输出-1。

# 示例 2：
# 输入：intervals = [[3, 4], [2, 3], [1, 2]]
# 输出：[-1, 0, 1]
# 解释：对于[3, 4] ，没有满足条件的“右侧”区间。
# 对于[2, 3] ，区间[3, 4]具有最小的“右”起点
# 对于[1, 2] ，区间[2, 3]具有最小的“右”起点。

# 示例 3：
# 输入：intervals = [[1, 4], [2, 3], [3, 4]]
# 输出：[-1, 2, -1]
# 解释：对于区间[1, 4] 和[3, 4] ，没有满足条件的“右侧”区间。
# 对于[2, 3] ，区间[3, 4] 有最小的“右”起点。


# 提示：
# 1 <= intervals.length <= 2 * 10^4
# intervals[i].length == 2
# -10^6 <= starti <= endi <= 10^6
# 每个间隔的起点都 不相同

from bisect import bisect_left
from typing import List
# @lc code=start


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        idx = sorted([(interval[0], i)
                      for i, interval in enumerate(intervals)])
        return [(idx[i][1] if (i := bisect_left(idx, (interval[1], 0))) != n else -1) for interval in intervals]


# @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.findRightInterval([[1, 2]]))  # [-1]
    print(solution.findRightInterval([[3, 4], [2, 3], [1, 2]]))  # [-1,0,1]
    print(solution.findRightInterval([[1, 4], [2, 3], [3, 4]]))  # [-1,2,-1]
