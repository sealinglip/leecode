#
# @lc app=leetcode.cn id=850 lang=python3
#
# [850] 矩形面积 II
#
# 我们给出了一个（轴对齐的）二维矩形列表 rectangles 。 对于 rectangle[i] = [x1, y1, x2, y2]，其中（x1，y1）是矩形 i 左下角的坐标， (xi1, yi1) 是该矩形 左下角 的坐标， (xi2, yi2) 是该矩形 右上角 的坐标。

# 计算平面中所有 rectangles 所覆盖的 总面积 。任何被两个或多个矩形覆盖的区域应只计算 一次 。

# 返回 总面积 。因为答案可能太大，返回 10^9 + 7 的 模 。


# 示例 1：
# 输入：rectangles = [[0, 0, 2, 2], [1, 0, 2, 3], [1, 0, 3, 1]]
# 输出：6
# 解释：如图所示，三个矩形覆盖了总面积为6的区域。
# 从(1, 1)到(2, 2)，绿色矩形和红色矩形重叠。
# 从(1, 0)到(2, 1)，三个矩形都重叠。


# 示例 2：
# 输入：rectangles = [[0, 0, 1000000000, 1000000000]]
# 输出：49
# 解释：答案是 10^18 对(10^9 + 7) 取模的结果， 即 49 。


# 提示：
# 1 <= rectangles.length <= 200
# rectanges[i].length = 4
# 0 <= xi1, yi1, xi2, yi2 <= 10^9
# 矩形叠加覆盖后的总面积不会超越 2 ^ 63 - 1 ，这意味着可以用一个 64 位有符号整数来保存面积结果。

# Hard
# 复习
# 线段树

from typing import List
# @lc code=start


class Node:
    def __init__(self) -> None:
        self.l = self.r = 0  # 记录区间的左右边界[l, r]
        self.cnt = self.length = 0  # 记录区间被覆盖的次数和长度


class SegmentTree:
    def __init__(self, nums) -> None:
        n = len(nums) - 1
        self.nums = nums
        self.tr = [Node() for _ in range(n << 2)]
        self.build(1, 0, n - 1)

    def build(self, u, l, r):
        self.tr[u].l, self.tr[u].r = l, r
        if l != r:  # 非末级
            mid = (l + r) >> 1
            self.build(u << 1, l, mid)
            self.build(u << 1 | 1, mid + 1, r)

    def modify(self, u, l, r, k):
        if self.tr[u].l >= l and self.tr[u].r <= r:
            # 本区间被完整覆盖
            self.tr[u].cnt += k
        else:
            mid = (self.tr[u].l + self.tr[u].r) >> 1
            if l <= mid:
                self.modify(u << 1, l, r, k)
            if r > mid:
                self.modify(u << 1 | 1, l, r, k)
        self.pushup(u)

    def pushup(self, u):
        if self.tr[u].cnt:
            self.tr[u].length = self.nums[self.tr[u].r + 1] - \
                self.nums[self.tr[u].l]
        elif self.tr[u].l == self.tr[u].r:
            self.tr[u].length = 0
        else:
            self.tr[u].length = self.tr[u << 1].length + \
                self.tr[u << 1 | 1].length

    @property
    def length(self):
        return self.tr[1].length


class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7

        segs = []
        allYs = set()  # 记录所有出现过的y坐标
        for x1, y1, x2, y2 in rectangles:
            # 左侧线段
            segs.append((x1, y1, y2, 1))
            # 右侧线段
            segs.append((x2, y1, y2, -1))
            allYs.add(y1)
            allYs.add(y2)

        segs.sort()

        allYs = sorted(allYs)
        tree = SegmentTree(allYs)
        m = {v: i for i, v in enumerate(allYs)}
        ans = 0
        for i, (x, y1, y2, k) in enumerate(segs):
            if i:
                # Y 坐标被覆盖的长度 乘以 相邻横坐标之差
                ans += tree.length * (x - segs[i - 1][0])
            tree.modify(1, m[y1], m[y2] - 1, k)
        ans %= MOD
        return ans

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.rectangleArea(
        [[0, 0, 2, 2], [1, 0, 2, 3], [1, 0, 3, 1]]))  # 6
    print(solution.rectangleArea([[0, 0, 1000000000, 1000000000]]))  # 49
