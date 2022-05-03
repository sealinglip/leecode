#
# @lc app=leetcode.cn id=295 lang=python3
#
# [295] 数据流的中位数
#
# 中位数是有序列表中间的数。如果列表长度是偶数，中位数则是中间两个数的平均值。

# 例如，

# [2, 3, 4] 的中位数是 3
# [2, 3] 的中位数是(2 + 3) / 2 = 2.5
# 设计一个支持以下两种操作的数据结构：

# void addNum(int num) - 从数据流中添加一个整数到数据结构中。
# double findMedian() - 返回目前所有元素的中位数。

# 示例：
# addNum(1)
# addNum(2)
# findMedian() -> 1.5
# addNum(3)
# findMedian() -> 2
# 进阶:

# 如果数据流中所有整数都在 0 到 100 范围内，你将如何优化你的算法？
# 如果数据流中 99 % 的整数都在 0 到 100 范围内，你将如何优化你的算法？

# Hard

# @lc code=start
import heapq


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        # self.data = []
        self.numLow = []
        self.numHigh = []

    def addNum(self, num: int) -> None:
        # insort(self.data, num)
        if not self.numLow or num > -self.numLow[0]:
            heapq.heappush(self.numHigh, num)
            if len(self.numHigh) > len(self.numLow) + 1:
                heapq.heappush(self.numLow, -heapq.heappop(self.numHigh))
        else:
            heapq.heappush(self.numLow, -num)
            if len(self.numLow) > len(self.numHigh):
                heapq.heappush(self.numHigh, -heapq.heappop(self.numLow))

    def findMedian(self) -> float:
        # N = len(self.data)
        # if (N & 1):
        #     return self.data[(N >> 1)]
        # else:
        #     return (self.data[(N >> 1)] + self.data[(N >> 1) - 1]) / 2
        if len(self.numHigh) > len(self.numLow):
            return self.numHigh[0]
        elif len(self.numHigh) == 0:
            return None
        else:
            return (self.numHigh[0] - self.numLow[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end
if __name__ == "__main__":
    medianFinder = MedianFinder()
    medianFinder.addNum(1)
    medianFinder.addNum(2)
    print(medianFinder.findMedian())
    medianFinder.addNum(3)
    print(medianFinder.findMedian())
