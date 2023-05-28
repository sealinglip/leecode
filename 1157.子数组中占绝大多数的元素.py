#
# @lc app=leetcode.cn id=1157 lang=python3
#
# [1157] 子数组中占绝大多数的元素
#
# 设计一个数据结构，有效地找到给定子数组的 多数元素 。

# 子数组的 多数元素 是在子数组中出现 threshold 次数或次数以上的元素。

# 实现 MajorityChecker 类:

# MajorityChecker(int[] arr) 会用给定的数组 arr 对 MajorityChecker 初始化。
# int query(int left, int right, int threshold) 返回子数组中的元素  arr[left...right] 至少出现 threshold 次数，如果不存在这样的元素则返回 - 1。


# 示例 1：
# 输入:
# ["MajorityChecker", "query", "query", "query"]
# [[[1, 1, 2, 2, 1, 1]], [0, 5, 4], [0, 3, 3], [2, 3, 2]]
# 输出：
# [null, 1, -1, 2]
# 解释：
# MajorityChecker majorityChecker = new MajorityChecker([1, 1, 2, 2, 1, 1])
# majorityChecker.query(0, 5, 4)
# // 返回 1
# majorityChecker.query(0, 3, 3)
# // 返回 - 1
# majorityChecker.query(2, 3, 2)
# // 返回 2


# 提示：
# 1 <= arr.length <= 2 * 10^4
# 1 <= arr[i] <= 2 * 10^4
# 0 <= left <= right < arr.length
# threshold <= right - left + 1
# 2 * threshold > right - left + 1
# 调用 query 的次数最多为 10^4

# Hard
# 线段树

from bisect import bisect_left, bisect_right
from collections import defaultdict
from typing import List
# @lc code=start


class Node:
    def __init__(self, x: int = 0, cnt: int = 0):
        self.x = x
        self.cnt = cnt

    def __iadd__(self, that: "Node") -> "Node":
        if self.x == that.x:
            self.cnt += that.cnt
        elif self.cnt >= that.cnt:
            self.cnt -= that.cnt
        else:
            self.x = that.x
            self.cnt = that.cnt - self.cnt
        return self


class MajorityChecker:

    def __init__(self, arr: List[int]):
        self.n = len(arr)
        self.arr = arr
        self.loc = defaultdict(list)

        for i, val in enumerate(arr):
            self.loc[val].append(i)

        self.tree = [Node() for _ in range(self.n * 4)]
        self.seg_build(0, 0, self.n - 1)

    def query(self, left: int, right: int, threshold: int) -> int:
        ans = Node()
        self.seg_query(0, 0, self.n - 1, left, right, ans)
        pos = self.loc[ans.x]
        occ = bisect_right(pos, right) - bisect_left(pos,
                                                     left)  # 在区间[left, right]中x出现的次数
        return ans.x if occ >= threshold else -1

    def seg_build(self, idx: int, l: int, r: int) -> None:
        print("idx: %d, l: %d, r: %d" % (idx, l, r))
        if l == r:
            self.tree[idx] = Node(self.arr[l], 1)
            return

        mid = (l + r) // 2
        self.seg_build(idx * 2 + 1, l, mid)
        self.seg_build(idx * 2 + 2, mid + 1, r)
        self.tree[idx] += self.tree[idx * 2 + 1]
        self.tree[idx] += self.tree[idx * 2 + 2]

    def seg_query(self, idx: int, l: int, r: int, ql: int, qr: int, ans: Node) -> None:
        if l > qr or r < ql:
            return

        if ql <= l and r <= qr:
            ans += self.tree[idx]
            return

        mid = (l + r) // 2
        self.seg_query(idx * 2 + 1, l, mid, ql, qr, ans)
        self.seg_query(idx * 2 + 2, mid + 1, r, ql, qr, ans)

        # Your MajorityChecker object will be instantiated and called as such:
        # obj = MajorityChecker(arr)
        # param_1 = obj.query(left,right,threshold)
        # @lc code=end
if __name__ == "__main__":
    obj = MajorityChecker([1, 1, 2, 2, 1, 1])
    print(obj.query(0, 5, 4))  # 1
    print(obj.query(0, 3, 3))  # -1
    print(obj.query(2, 3, 2))  # 2
