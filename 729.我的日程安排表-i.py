#
# @lc app=leetcode.cn id=729 lang=python3
#
# [729] 我的日程安排表 I
#
# 实现一个 MyCalendar 类来存放你的日程安排。如果要添加的日程安排不会造成 重复预订 ，则可以存储这个新的日程安排。

# 当两个日程安排有一些时间上的交叉时（例如两个日程安排都在同一时间内），就会产生 重复预订 。

# 日程可以用一对整数 start 和 end 表示，这里的时间是半开区间，即[start, end), 实数 x 的范围为，  start <= x < end 。

# 实现 MyCalendar 类：

# MyCalendar() 初始化日历对象。
# boolean book(int start, int end) 如果可以将日程安排成功添加到日历中而不会导致重复预订，返回 true 。否则，返回 false 并且不要将该日程安排添加到日历中。


# 示例：
# 输入：
# ["MyCalendar", "book", "book", "book"]
# [[], [10, 20], [15, 25], [20, 30]]
# 输出：
# [null, true, false, true]

# 解释：
# MyCalendar myCalendar = new MyCalendar()
# myCalendar.book(10, 20)
# // return True
# myCalendar.book(15, 25)
# // return False ，这个日程安排不能添加到日历中，因为时间 15 已经被另一个日程安排预订了。
# myCalendar.book(20, 30)
# // return True ，这个日程安排可以添加到日历中，因为第一个日程安排预订的每个时间都小于 20 ，且不包含时间 20 。


# 提示：
# 0 <= start < end <= 10^9
# 每个测试用例，调用 book 方法的次数最多不超过 1000 次。

from collections import defaultdict
from typing import List
# @lc code=start


class MyCalendar:

    def __init__(self):
        self.occupied = defaultdict(bool)  # 标记区间[l, r]作为叶子节点是否被占
        self.notLeaf = defaultdict(bool)  # 标记区间是不是非叶子节点

    def check(self, start: int, end: int, l: int, r: int, idx: int, needOccupy: List[int]) -> bool:
        if r < start or end < l:  # 两个区间不重叠
            return True  # 不相干，返回True
        if self.occupied[idx]:
            return False
        if (not self.notLeaf[idx]) and start <= l and r <= end:
            # [start, end) 完全覆盖 [l, r)
            # 不能在这里直接改，如果update 整体不成功，那么状态就不一致了
            # self.occupied[idx] = True
            needOccupy.append(idx)
            return True
        else:
            self.notLeaf[idx] = True
            # 区间有重叠
            # 求[l, r)的中值
            mid = (l + r) >> 1
            # 更新当前节点的子节点
            return self.check(start, end, l, mid, idx << 1, needOccupy) and \
                self.check(start, end, mid + 1, r, 1 + (idx << 1), needOccupy)

    def book(self, start: int, end: int) -> bool:
        needOccupy = []
        res = self.check(start, end - 1, 0, 10 ** 9, 1, needOccupy)
        if res and needOccupy:
            for i in needOccupy:
                self.occupied[i] = True
        return res

        # Your MyCalendar object will be instantiated and called as such:
        # obj = MyCalendar()
        # param_1 = obj.book(start,end)
        # @lc code=end
if __name__ == "__main__":
    # myCalendar = MyCalendar()
    # print(myCalendar.book(10, 20))  # True
    # print(myCalendar.book(15, 25))  # False
    # print(myCalendar.book(20, 30))  # True

    myCalendar = MyCalendar()
    print(myCalendar.book(20, 29))  # True
    print(myCalendar.book(13, 22))  # False 此处添加失败不能影响最终状态
    print(myCalendar.book(44, 50))  # True
    print(myCalendar.book(1, 7))  # True
    print(myCalendar.book(2, 10))  # False
    print(myCalendar.book(14, 20))  # True
