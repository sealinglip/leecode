#
# @lc app=leetcode.cn id=2276 lang=python3
#
# [2276] 统计区间中的整数数目
#
# 给你区间的 空 集，请你设计并实现满足要求的数据结构：
#   新增：添加一个区间到这个区间集合中。
#   统计：计算出现在 至少一个 区间中的整数个数。

# 实现 CountIntervals 类：
#   CountIntervals() 使用区间的空集初始化对象
#   void add(int left, int right) 添加区间 [left, right] 到区间集合之中。
#   int count() 返回出现在 至少一个 区间中的整数个数。

# 注意：区间 [left, right] 表示满足 left <= x <= right 的所有整数 x 。

# 示例 1：
# 输入
# ["CountIntervals", "add", "add", "count", "add", "count"]
# [[], [2, 3], [7, 10], [], [5, 8], []]
# 输出
# [null, null, null, 6, null, 8]
# 解释
# CountIntervals countIntervals = new CountIntervals(); // 用一个区间空集初始化对象
# countIntervals.add(2, 3);  // 将 [2, 3] 添加到区间集合中
# countIntervals.add(7, 10); // 将 [7, 10] 添加到区间集合中
# countIntervals.count();    // 返回 6
#                            // 整数 2 和 3 出现在区间 [2, 3] 中
#                            // 整数 7、8、9、10 出现在区间 [7, 10] 中
# countIntervals.add(5, 8);  // 将 [5, 8] 添加到区间集合中
# countIntervals.count();    // 返回 8
#                            // 整数 2 和 3 出现在区间 [2, 3] 中
#                            // 整数 5 和 6 出现在区间 [5, 8] 中
#                            // 整数 7 和 8 出现在区间 [5, 8] 和区间 [7, 10] 中
#                            // 整数 9 和 10 出现在区间 [7, 10] 中
 

# 提示：
# 1 <= left <= right <= 10^9
# 最多调用  add 和 count 方法 总计 10^5 次
# 调用 count 方法至少一次

# Hard
# 线段树

# 动态开点

# @lc code=start
from collections import defaultdict


class CountIntervals:

    def __init__(self):
        self.tree = defaultdict(int)

    def update(self, start: int, end: int, l: int, r: int, idx: int) -> bool:
        if r < start or end < l or self.tree[idx] == (r - l + 1):  # 区间不相交 或者 本区间所有数已经全部点亮了
            return False
        if start <= l and r <= end:
            # [start, end] 完全覆盖 [l, r]
            self.tree[idx] = r - l + 1 # 本区间所有数都点亮了
            return True
        else:
            # 求[l, r)的中值
            mid = (l + r) >> 1
            lu = self.update(start, end, l, mid, idx << 1)
            ru = self.update(start, end, mid + 1, r, 1 + (idx << 1))
            if lu or ru:
                self.tree[idx] = self.tree[idx << 1] + self.tree[1 + (idx << 1)]
                return True
            return False

    def add(self, left: int, right: int) -> None:
        self.update(left, right, 1, (10 ** 9), 1)

    def count(self) -> int:
        return self.tree[1]



# Your CountIntervals object will be instantiated and called as such:
# obj = CountIntervals()
# obj.add(left,right)
# param_2 = obj.count()
# @lc code=end

if __name__ == "__main__":
    countIntervals = CountIntervals()
    countIntervals.add(2, 3)
    countIntervals.add(7, 10)
    print(countIntervals.count()) # 6
    countIntervals.add(5, 8)
    print(countIntervals.count()) # 8

    countIntervals = CountIntervals()
    countIntervals.add(8,43)
    print(countIntervals.count()) # 36
    countIntervals.add(13,16)
    countIntervals.add(26,33)
    countIntervals.add(28,36)
    countIntervals.add(28,36)
    countIntervals.add(29,37)
    print(countIntervals.count()) # 36
    countIntervals.add(34,46)
    countIntervals.add(10,23)
    print(countIntervals.count()) # 39