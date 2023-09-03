#
# @lc app=leetcode.cn id=2569 lang=python3
#
# [2569] 更新数组后处理求和查询
#
# 给你两个下标从 0 开始的数组 nums1 和 nums2 ，和一个二维数组 queries 表示一些操作。总共有 3 种类型的操作：

# 操作类型 1 为 queries[i] = [1, l, r] 。你需要将 nums1 从下标 l 到下标 r 的所有 0 反转成 1 或将 1 反转成 0 。l 和 r 下标都从 0 开始。
# 操作类型 2 为 queries[i] = [2, p, 0] 。对于 0 <= i < n 中的所有下标，令 nums2[i] = nums2[i] + nums1[i] * p 。
# 操作类型 3 为 queries[i] = [3, 0, 0] 。求 nums2 中所有元素的和。
# 请你返回一个数组，包含所有第三种操作类型的答案。


# 示例 1：
# 输入：nums1 = [1, 0, 1], nums2 = [0, 0, 0], queries = [[1, 1, 1], [2, 1, 0], [3, 0, 0]]
# 输出：[3]
# 解释：第一个操作后 nums1 变为[1, 1, 1] 。第二个操作后，nums2 变成[1, 1, 1] ，所以第三个操作的答案为 3 。所以返回[3] 。

# 示例 2：
# 输入：nums1 = [1], nums2 = [5], queries = [[2, 0, 0], [3, 0, 0]]
# 输出：[5]
# 解释：第一个操作后，nums2 保持不变为[5] ，所以第二个操作的答案是 5 。所以返回[5] 。


# 提示：
# 1 <= nums1.length, nums2.length <= 10^5
# nums1.length = nums2.length
# 1 <= queries.length <= 10^5
# queries[i].length = 3
# 0 <= l <= r <= nums1.length - 1
# 0 <= p <= 10^6
# 0 <= nums1[i] <= 1
# 0 <= nums2[i] <= 10^9

# Hard
# 线段树

from typing import List
# @lc code=start


class SegNode:
    def __init__(self) -> None:
        self.l = 0
        self.r = 0
        self.sum = 0
        self.lazy = False


class SegTree:
    def __init__(self, nums: List[int]) -> None:
        n = len(nums)
        self.arr = [SegNode() for _ in range((n << 2) + 1)]
        self.build(1, 0, n-1, nums)

    def build(self, id: int, l: int, r: int, nums: List[int]) -> None:
        self.arr[id] = SegNode()
        self.arr[id].l = l
        self.arr[id].r = r
        self.arr[id].lazy = False
        if l == r:
            self.arr[id].sum = nums[l]
            return
        mid = (l + r) >> 1
        self.build(id << 1, l, mid, nums)
        self.build((id << 1) + 1, mid + 1, r, nums)
        self.arr[id].sum = self.arr[id << 1].sum + self.arr[(id << 1) + 1].sum

    def sum_range(self, l: int, r: int) -> int:
        return self.query(1, l, r)

    def reverse_range(self, l: int, r: int) -> None:
        self.modify(1, l, r)

    def modify(self, id: int, l: int, r: int) -> None:
        if self.arr[id].l >= l and self.arr[id].r <= r:
            # 区间完全命中
            self.arr[id].sum = (
                self.arr[id].r - self.arr[id].l + 1) - self.arr[id].sum
            self.arr[id].lazy = not self.arr[id].lazy
            return

        self.pushdown(id)
        mid = (self.arr[id].l + self.arr[id].r) >> 1
        if self.arr[id << 1].r >= l:
            self.modify(id << 1, l, r)
        if self.arr[(id << 1) + 1].l <= r:
            self.modify((id << 1) + 1, l, r)
        self.arr[id].sum = self.arr[id << 1].sum + self.arr[(id << 1) + 1].sum

    def pushdown(self, id: int) -> None:
        if self.arr[id].lazy:
            self.arr[id << 1].lazy = not self.arr[id << 1].lazy
            self.arr[id << 1].sum = self.arr[id << 1].r - \
                self.arr[id << 1].l + 1 - self.arr[id << 1].sum
            self.arr[(id << 1) + 1].lazy = not self.arr[(id << 1) + 1].lazy
            self.arr[(id << 1) + 1].sum = self.arr[(id << 1) +
                                                   1].r - self.arr[(id << 1) + 1].l + 1 - self.arr[(id << 1) + 1].sum
            self.arr[id].lazy = False

    def query(self, id: int, l: int, r: int) -> int:
        if self.arr[id].l >= l and self.arr[id].r <= r:
            return self.arr[id].sum
        if self.arr[id].r < l or self.arr[id].l > r:
            return 0

        self.pushdown(id)
        mid = (self.arr[id].l + self.arr[id].r) >> 1
        res = 0
        if self.arr[id << 1].r >= l:
            res += self.query(id << 1, l, r)
        if self.arr[(id << 1) + 1].l <= r:
            res += self.query((id << 1) + 1, l, r)
        return res


class Solution:
    def handleQuery(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        m, n = len(queries), len(nums1)
        seg_tree = SegTree(nums1)

        total = sum(nums2)
        res = []
        for i in range(m):
            if queries[i][0] == 1:
                _, l, r = queries[i]
                seg_tree.reverse_range(l, r)
            elif queries[i][0] == 2:
                total += seg_tree.sum_range(0, n - 1) * queries[i][1]
            elif queries[i][0] == 3:
                res.append(total)

        return res

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.handleQuery([1, 0, 1], [0, 0, 0], [
          [1, 1, 1], [2, 1, 0], [3, 0, 0]]))  # [3]
    print(solution.handleQuery([1], [5], [[2, 0, 0], [3, 0, 0]]))  # [5]
