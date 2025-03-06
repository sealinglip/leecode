#
# @lc app=leetcode.cn id=2080 lang=python3
#
# [2080] 区间内查询数字的频率
#
# 请你设计一个数据结构，它能求出给定子数组内一个给定值的 频率 。

# 子数组中一个值的 频率 指的是这个子数组中这个值的出现次数。

# 请你实现 RangeFreqQuery 类：

# RangeFreqQuery(int[] arr) 用下标从 0 开始的整数数组 arr 构造一个类的实例。
# int query(int left, int right, int value) 返回子数组 arr[left...right] 中 value 的 频率 。
# 一个 子数组 指的是数组中一段连续的元素。arr[left...right] 指的是 nums 中包含下标 left 和 right 在内 的中间一段连续元素。


# 示例 1：
# 输入：
# ["RangeFreqQuery", "query", "query"]
# [[[12, 33, 4, 56, 22, 2, 34, 33, 22, 12, 34, 56]], [1, 2, 4], [0, 11, 33]]
# 输出：
# [null, 1, 2]
# 解释：
# RangeFreqQuery rangeFreqQuery = new RangeFreqQuery([12, 33, 4, 56, 22, 2, 34, 33, 22, 12, 34, 56]);
# rangeFreqQuery.query(1, 2, 4); // 返回 1 。4 在子数组 [33, 4] 中出现 1 次。
# rangeFreqQuery.query(0, 11, 33); // 返回 2 。33 在整个子数组中出现 2 次。
 

# 提示：
# 1 <= arr.length <= 10^5
# 1 <= arr[i], value <= 10^4
# 0 <= left <= right < arr.length
# 调用 query 不超过 105 次。

from bisect import bisect_left, bisect_right
from collections import defaultdict
from typing import List
# @lc code=start
class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.stat = defaultdict(list)
        for i, x in enumerate(arr):
            self.stat[x].append(i)

    def query(self, left: int, right: int, value: int) -> int:
        if value in self.stat:
            return bisect_right(self.stat[value], right) - bisect_left(self.stat[value], left)
        else:
            return 0
        


# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)
# @lc code=end

if __name__ == "__main__":
    rangeFreqQuery = RangeFreqQuery([12, 33, 4, 56, 22, 2, 34, 33, 22, 12, 34, 56])
    print(rangeFreqQuery.query(1, 2, 4)) # 1
    print(rangeFreqQuery.query(0, 11, 33)) # 2
    print(rangeFreqQuery.query(1, 7, 33)) # 2
