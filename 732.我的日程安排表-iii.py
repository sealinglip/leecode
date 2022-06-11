#
# @lc app=leetcode.cn id=732 lang=python3
#
# [732] 我的日程安排表 III
#
# 当 k 个日程安排有一些时间上的交叉时（例如 k 个日程安排都在同一时间内），就会产生 k 次预订。

# 给你一些日程安排[start, end) ，请你在每个日程安排添加后，返回一个整数 k ，表示所有先前日程安排会产生的最大 k 次预订。

# 实现一个 MyCalendarThree 类来存放你的日程安排，你可以一直添加新的日程安排。

# MyCalendarThree() 初始化对象。
# int book(int start, int end) 返回一个整数 k ，表示日历中存在的 k 次预订的最大值。


# 示例：
# 输入：
# ["MyCalendarThree", "book", "book", "book", "book", "book", "book"]
# [[], [10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]]
# 输出：
# [null, 1, 1, 2, 3, 3, 3]

# 解释：
# MyCalendarThree myCalendarThree = new MyCalendarThree()
# myCalendarThree.book(10, 20)
# // 返回 1 ，第一个日程安排可以预订并且不存在相交，所以最大 k 次预订是 1 次预订。
# myCalendarThree.book(50, 60)
# // 返回 1 ，第二个日程安排可以预订并且不存在相交，所以最大 k 次预订是 1 次预订。
# myCalendarThree.book(10, 40)
# // 返回 2 ，第三个日程安排[10, 40) 与第一个日程安排相交，所以最大 k 次预订是 2 次预订。
# myCalendarThree.book(5, 15)
# // 返回 3 ，剩下的日程安排的最大 k 次预订是 3 次预订。
# myCalendarThree.book(5, 10)
# // 返回 3
# myCalendarThree.book(25, 55)
# // 返回 3


# 提示：
# 0 <= start < end <= 10^9
# 每个测试用例，调用 book 函数最多不超过 400次

# Hard 复习 线段树
# @lc code=start
from collections import defaultdict


class MyCalendarThree:

    def __init__(self):
        self.tree = defaultdict(int)  # 记录区间[l, r]的最大值
        self.lazy = defaultdict(int)  # 标记区间[l, r]进行累计的次数

    def update(self, start: int, end: int, l: int, r: int, idx: int):
        if r < start or end < l:  # 两个区间不重叠
            return
        if start <= l and r <= end:
            self.tree[idx] += 1
            self.lazy[idx] += 1
        else:
            mid = (l + r) >> 1
            self.update(start, end, l, mid, idx << 1)
            self.update(start, end, mid + 1, r, 1 + (idx << 1))
            self.tree[idx] = self.lazy[idx] + \
                max(self.tree[idx << 1], self.tree[1 + (idx << 1)])

    def book(self, start: int, end: int) -> int:
        self.update(start, end - 1, 0, 10 ** 9, 1)
        return self.tree[1]


        # Your MyCalendarThree object will be instantiated and called as such:
        # obj = MyCalendarThree()
        # param_1 = obj.book(start,end)
        # @lc code=end
if __name__ == "__main__":
    myCalendarThree = MyCalendarThree()
    print(myCalendarThree.book(10, 20))  # 1
    print(myCalendarThree.book(50, 60))  # 1
    print(myCalendarThree.book(10, 40))  # 2
    print(myCalendarThree.book(5, 15))  # 3
    print(myCalendarThree.book(5, 10))  # 3
    print(myCalendarThree.book(25, 55))  # 3
