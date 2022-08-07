#
# @lc app=leetcode.cn id=1622 lang=python3
#
# [1622] 奇妙序列
#
# 请你实现三个 API append，addAll 和 multAll 来实现奇妙序列。

# 请实现 Fancy 类 ：

# Fancy() 初始化一个空序列对象。
# void append(val) 将整数 val 添加在序列末尾。
# void addAll(inc) 将所有序列中的现有数值都增加 inc 。
# void multAll(m) 将序列中的所有现有数值都乘以整数 m 。
# int getIndex(idx) 得到下标为 idx 处的数值（下标从 0 开始），并将结果对 10^9 + 7 取余。如果下标大于等于序列的长度，请返回 - 1 。


# 示例：
# 输入：
# ["Fancy", "append", "addAll", "append", "multAll", "getIndex",
#     "addAll", "append", "multAll", "getIndex", "getIndex", "getIndex"]
# [[], [2], [3], [7], [2], [0], [3], [10], [2], [0], [1], [2]]
# 输出：
# [null, null, null, null, null, 10, null, null, null, 26, 34, 20]

# 解释：
# Fancy fancy = new Fancy()
# fancy.append(2)
# // 奇妙序列：[2]
# fancy.addAll(3)
# // 奇妙序列：[2+3] -> [5]
# fancy.append(7)
# // 奇妙序列：[5, 7]
# fancy.multAll(2)
# // 奇妙序列：[5*2, 7*2] -> [10, 14]
# fancy.getIndex(0)
# // 返回 10
# fancy.addAll(3)
# // 奇妙序列：[10+3, 14+3] -> [13, 17]
# fancy.append(10)
# // 奇妙序列：[13, 17, 10]
# fancy.multAll(2)
# // 奇妙序列：[13*2, 17*2, 10*2] -> [26, 34, 20]
# fancy.getIndex(0)
# // 返回 26
# fancy.getIndex(1)
# // 返回 34
# fancy.getIndex(2)
# // 返回 20


# 提示：
# 1 <= val, inc, m <= 100
# 0 <= idx <= 10^5
# 总共最多会有 10^5 次对 append，addAll，multAll 和 getIndex 的调用。

# Hard

# 直接按题意实现会TLE
# class Fancy:

#     def __init__(self):
#         self._arr = []

#     def append(self, val: int) -> None:
#         self._arr.append(val)

#     def addAll(self, inc: int) -> None:
#         for i in range(len(self._arr)):
#             self._arr[i] += inc

#     def multAll(self, m: int) -> None:
#         for i in range(len(self._arr)):
#             self._arr[i] *= m

#     def getIndex(self, idx: int) -> int:
#         if idx >= len(self._arr):
#             return -1
#         else:
#             return self._arr[idx] % MOD

# 简化addAll和multAll运算
# 线段树
# @lc code=start


MOD = 10 ** 9 + 7


class SegTree:
    def __init__(self, l: int, r: int):
        self.add = 0
        self.mul = 1
        self.left = self.right = None
        self.l = l  # 本段左边界（包含）
        self.r = r  # 本段右边界（包含）
        self.value = 0  # 非叶子节点（r > l）不用算这个值

    @property
    def _mid(self) -> int:
        return (self.l + self.r) >> 1

    @property
    def _leaf(self) -> bool:
        return self.l == self.r

    @property
    def _left(self) -> 'SegTree':
        if self._leaf:
            return None
        if self.left is None:
            self.left = SegTree(self.l, self._mid)
        return self.left

    @property
    def _right(self) -> 'SegTree':
        if self._leaf:
            return None
        if self.right is None:
            self.right = SegTree(self._mid + 1, self.r)
        return self.right

    def addUpdate(self, lb: int, ub: int, val: int) -> None:
        if lb <= self.l and self.r <= ub:  # 更新区间完全覆盖本节点
            self.add += val
            return

        self.lazyPushDown()

        if lb <= self._mid:  # 和左节点可能有重叠
            self._left.addUpdate(lb, ub, val)
        if self._mid + 1 <= ub:
            self._right.addUpdate(lb, ub, val)

    def mulUpdate(self, lb: int, ub: int, val: int) -> None:
        if lb <= self.l and self.r <= ub:  # 更新区间完全覆盖本节点
            self.add *= val
            self.mul *= val
            self.add %= MOD
            self.mul %= MOD
            return

        self.lazyPushDown()

        if lb <= self._mid:  # 和左节点可能有重叠
            self._left.mulUpdate(lb, ub, val)
        if self._mid + 1 <= ub:
            self._right.mulUpdate(lb, ub, val)

    def lazyPushDown(self) -> None:
        if self.add != 0 or self.mul != 1:
            if self._leaf:
                self.value = self.value * self.mul + self.add
                self.value %= MOD
            else:
                if self.left:
                    self._left.mul *= self.mul
                    self._left.add = self._left.add * self.mul + self.add
                    self._left.mul %= MOD
                    self._left.add %= MOD

                if self.right:
                    self._right.mul *= self.mul
                    self._right.add = self._right.add * self.mul + self.add
                    self._right.mul %= MOD
                    self._right.add %= MOD

            self.mul = 1
            self.add = 0

    def query(self, idx: int) -> int:
        if idx < self.l or self.r < idx:
            return 0  # 不搭界
        if self._leaf and idx == self.l:
            self.lazyPushDown()
            return self.value

        self.lazyPushDown()
        return self._left.query(idx) if idx <= self._mid else self._right.query(idx)


class Fancy:

    def __init__(self):
        self.ub = -1
        self.segTree = SegTree(0, 10 ** 5)

    def append(self, val: int) -> None:
        # 这是一种特殊形式的addUpdate
        self.ub += 1
        self.segTree.addUpdate(self.ub, self.ub, val)

    def addAll(self, inc: int) -> None:
        if self.ub >= 0:
            self.segTree.addUpdate(0, self.ub, inc)

    def multAll(self, m: int) -> None:
        if self.ub >= 0:
            self.segTree.mulUpdate(0, self.ub, m)

    def getIndex(self, idx: int) -> int:
        return self.segTree.query(idx) if idx <= self.ub else -1

        # Your Fancy object will be instantiated and called as such:
        # obj = Fancy()
        # obj.append(val)
        # obj.addAll(inc)
        # obj.multAll(m)
        # param_4 = obj.getIndex(idx)
        # @lc code=end
if __name__ == "__main__":
    fancy = Fancy()
    fancy.append(2)
    fancy.addAll(3)
    fancy.append(7)
    fancy.multAll(2)
    print(fancy.getIndex(0))  # 10
    fancy.addAll(3)
    fancy.append(10)
    fancy.multAll(2)

    print(fancy.getIndex(0))  # 26
    print(fancy.getIndex(1))  # 34
    print(fancy.getIndex(2))  # 20
    print(fancy.getIndex(3))  # -1
