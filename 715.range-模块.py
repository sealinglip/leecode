#
# @lc app=leetcode.cn id=715 lang=python3
#
# [715] Range 模块
#
# Range模块是跟踪数字范围的模块。设计一个数据结构来跟踪表示为 半开区间 的范围并查询它们。

# 半开区间[left, right) 表示所有 left <= x < right 的实数 x 。

# 实现 RangeModule 类:

# RangeModule() 初始化数据结构的对象。
# void addRange(int left, int right) 添加 半开区间[left, right)，跟踪该区间中的每个实数。添加与当前跟踪的数字部分重叠的区间时，应当添加在区间[left, right) 中尚未跟踪的任何数字到该区间中。
# boolean queryRange(int left, int right) 只有在当前正在跟踪区间[left, right) 中的每一个实数时，才返回 true ，否则返回 false 。
# void removeRange(int left, int right) 停止跟踪 半开区间[left, right) 中当前正在跟踪的每个实数。


# 示例 1：
# 输入
# ["RangeModule", "addRange", "removeRange",
#     "queryRange", "queryRange", "queryRange"]
# [[], [10, 20], [14, 16], [10, 14], [13, 15], [16, 17]]
# 输出
# [null, null, null, true, false, true]

# 解释
# RangeModule rangeModule = new RangeModule()
# rangeModule.addRange(10, 20)
# rangeModule.removeRange(14, 16)
# rangeModule.queryRange(10, 14)
# 返回 true （区间[10, 14) 中的每个数都正在被跟踪）
# rangeModule.queryRange(13, 15)
# 返回 false（未跟踪区间[13, 15) 中像 14, 14.03, 14.17 这样的数字）
# rangeModule.queryRange(16, 17)
# 返回 true （尽管执行了删除操作，区间[16, 17) 中的数字 16 仍然会被跟踪）


# 提示：
# 1 <= left < right <= 10^9
# 在单个测试用例中，对 addRange 、  queryRange 和 removeRange 的调用总数不超过 10^4 次

# Hard

# @lc code=start
from sortedcontainers import SortedDict


class RangeModule:

    def __init__(self):
        self.ranges = SortedDict()

    def addRange(self, left: int, right: int) -> None:
        x = self.ranges.bisect_right(left)  # 找到插入点
        if x != 0:
            tmp = x - 1
            if self.ranges.values()[tmp] >= right:
                # 当前范围包含待添加的范围
                return
            if self.ranges.values()[tmp] >= left:
                # 当前范围跟待添加范围有交集
                left = self.ranges.keys()[tmp]
                self.ranges.popitem(tmp)
                x = tmp

        while x < len(self.ranges) and self.ranges.keys()[x] <= right:
            right = max(right, self.ranges.values()[x])
            self.ranges.popitem(x)

        self.ranges[left] = right

    def queryRange(self, left: int, right: int) -> bool:
        x = self.ranges.bisect_right(left)
        if x == 0:
            return False

        return right <= self.ranges.values()[x - 1]

    def removeRange(self, left: int, right: int) -> None:
        x = self.ranges.bisect_right(left)
        if x != 0:
            tmp = x - 1
            if (r := self.ranges.values()[tmp]) >= right:
                # 找到的区间能完全覆盖待移除的区间
                if (l := self.ranges.keys()[tmp]) == left:
                    # 区间左边界一致
                    self.ranges.popitem(tmp)
                else:
                    self.ranges[l] = left  # 更新存在区间的右边界，等同于截去待移除区间
                if right != r:
                    self.ranges[right] = r  # 截去待移除部分时，把尾巴上多的部分再找回来
                return
            elif r > left:
                # 更新存在区间的右边界，等同于截去待移除区间
                self.ranges[self.ranges.keys()[tmp]] = left

        while x < len(self.ranges) and self.ranges.keys()[x] < right:
            if self.ranges.values()[x] <= right:
                self.ranges.popitem(x)
            else:
                self.ranges[right] = self.ranges.values()[x]
                self.ranges.popitem(x)
                break


        # Your RangeModule object will be instantiated and called as such:
        # obj = RangeModule()
        # obj.addRange(left,right)
        # param_2 = obj.queryRange(left,right)
        # obj.removeRange(left,right)
        # @lc code=end
if __name__ == "__main__":
    rangeModule = RangeModule()
    rangeModule.addRange(10, 20)
    rangeModule.removeRange(14, 16)
    print(rangeModule.queryRange(10, 14))  # True
    print(rangeModule.queryRange(13, 15))  # False
    print(rangeModule.queryRange(16, 17))  # True
