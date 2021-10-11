#
# @lc app=leetcode.cn id=352 lang=python3
#
# [352] 将数据流变为多个不相交区间
#
# 给你一个由非负整数 a1, a2, ..., an 组成的数据流输入，请你将到目前为止看到的数字总结为不相交的区间列表。

# 实现 SummaryRanges 类：

# SummaryRanges() 使用一个空数据流初始化对象。
# void addNum(int val) 向数据流中加入整数 val 。
# int[][] getIntervals() 以不相交区间[starti, endi] 的列表形式返回对数据流中整数的总结。


# 示例：
# 输入：
# ["SummaryRanges", "addNum", "getIntervals", "addNum", "getIntervals",
#     "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals"]
# [[], [1], [], [3], [], [7], [], [2], [], [6], []]
# 输出：
# [null, null, [[1, 1]], null, [[1, 1], [3, 3]], null, [
#     [1, 1], [3, 3], [7, 7]], null, [[1, 3], [7, 7]], null, [[1, 3], [6, 7]]]

# 解释：
# SummaryRanges summaryRanges = new SummaryRanges()
# summaryRanges.addNum(1)
# // arr = [1]
# summaryRanges.getIntervals()
# // 返回[[1, 1]]
# summaryRanges.addNum(3)
# // arr = [1, 3]
# summaryRanges.getIntervals()
# // 返回[[1, 1], [3, 3]]
# summaryRanges.addNum(7)
# // arr = [1, 3, 7]
# summaryRanges.getIntervals()
# // 返回[[1, 1], [3, 3], [7, 7]]
# summaryRanges.addNum(2)
# // arr = [1, 2, 3, 7]
# summaryRanges.getIntervals()
# // 返回[[1, 3], [7, 7]]
# summaryRanges.addNum(6)
# // arr = [1, 2, 3, 6, 7]
# summaryRanges.getIntervals()
# // 返回[[1, 3], [6, 7]]


# 提示：
# 0 <= val <= 10^4
# 最多调用 addNum 和 getIntervals 方法 3 * 10^4 次


# 进阶：如果存在大量合并，并且与数据流的大小相比，不相交区间的数量很小，该怎么办?

from typing import List
# @lc code=start
from sortedcontainers import SortedDict


class SummaryRanges:

    def __init__(self):
        self.intervals = SortedDict()  # key为区间左边界，value为区间右边界

    def addNum(self, val: int) -> None:
        len_ = len(self.intervals)
        keys_ = self.intervals.keys()
        values_ = self.intervals.values()

        # 比val大的最小区间：val < keys[r1] if r1 != len_
        r1 = self.intervals.bisect_right(val)
        l1 = len_ if r1 == 0 else (r1 - 1)

        if l1 != len_ and keys_[l1] <= val <= values_[l1]:
            return  # val已经被l1对应的区间包含

        lconnect = l1 != len_ and (values_[l1] + 1 == val)  # 和左边区间挨上了
        rconnect = r1 != len_ and (keys_[r1] - 1 == val)  # 和右边区间挨上了
        if lconnect and rconnect:
            begin, end = keys_[l1], values_[r1]
            del self.intervals[keys_[r1]]
            self.intervals[begin] = end
        elif lconnect:
            begin = keys_[l1]
            self.intervals[begin] = val
        elif rconnect:
            end = values_[r1]
            del self.intervals[keys_[r1]]
            self.intervals[val] = end
        else:
            self.intervals[val] = val

    def getIntervals(self) -> List[List[int]]:
        return list(self.intervals.items())


        # Your SummaryRanges object will be instantiated and called as such:
        # obj = SummaryRanges()
        # obj.addNum(val)
        # param_2 = obj.getIntervals()
        # @lc code=end
if __name__ == "__main__":
    summaryRanges = SummaryRanges()
    summaryRanges.addNum(1)
    # // arr = [1]
    print(summaryRanges.getIntervals())
    # // 返回[[1, 1]]
    summaryRanges.addNum(3)
    # // arr = [1, 3]
    print(summaryRanges.getIntervals())
    # // 返回[[1, 1], [3, 3]]
    summaryRanges.addNum(7)
    # // arr = [1, 3, 7]
    print(summaryRanges.getIntervals())
    # // 返回[[1, 1], [3, 3], [7, 7]]
    summaryRanges.addNum(2)
    # // arr = [1, 2, 3, 7]
    print(summaryRanges.getIntervals())
    # // 返回[[1, 3], [7, 7]]
    summaryRanges.addNum(6)
    # // arr = [1, 2, 3, 6, 7]
    print(summaryRanges.getIntervals())
    # // 返回[[1, 3], [6, 7]]
