#
# @lc app=leetcode.cn id=2286 lang=python3
#
# [2286] 以组为单位订音乐会的门票
#
# 一个音乐会总共有 n 排座位，编号从 0 到 n - 1 ，每一排有 m 个座椅，编号为 0 到 m - 1 。你需要设计一个买票系统，针对以下情况进行座位安排：

# 同一组的 k 位观众坐在 同一排座位，且座位连续 。
# k 位观众中 每一位 都有座位坐，但他们 不一定 坐在一起。
# 由于观众非常挑剔，所以：

# 只有当一个组里所有成员座位的排数都 小于等于 maxRow ，这个组才能订座位。每一组的 maxRow 可能 不同 。
# 如果有多排座位可以选择，优先选择 最小 的排数。如果同一排中有多个座位可以坐，优先选择号码 最小 的。
# 请你实现 BookMyShow 类：

# BookMyShow(int n, int m) ，初始化对象，n 是排数，m 是每一排的座位数。
# int[] gather(int k, int maxRow) 返回长度为 2 的数组，表示 k 个成员中 第一个座位 的排数和座位编号，这 k 位成员必须坐在 同一排座位，且座位连续 。换言之，返回最小可能的 r 和 c 满足第 r 排中 [c, c + k - 1] 的座位都是空的，且 r <= maxRow 。如果 无法 安排座位，返回 [] 。
# boolean scatter(int k, int maxRow) 如果组里所有 k 个成员 不一定 要坐在一起的前提下，都能在第 0 排到第 maxRow 排之间找到座位，那么请返回 true 。这种情况下，每个成员都优先找排数 最小 ，然后是座位编号最小的座位。如果不能安排所有 k 个成员的座位，请返回 false 。
 

# 示例 1：
# 输入：
# ["BookMyShow", "gather", "gather", "scatter", "scatter"]
# [[2, 5], [4, 0], [2, 0], [5, 1], [5, 1]]
# 输出：
# [null, [0, 0], [], true, false]
# 解释：
# BookMyShow bms = new BookMyShow(2, 5); // 总共有 2 排，每排 5 个座位。
# bms.gather(4, 0); // 返回 [0, 0]
#                   // 这一组安排第 0 排 [0, 3] 的座位。
# bms.gather(2, 0); // 返回 []
#                   // 第 0 排只剩下 1 个座位。
#                   // 所以无法安排 2 个连续座位。
# bms.scatter(5, 1); // 返回 True
#                    // 这一组安排第 0 排第 4 个座位和第 1 排 [0, 3] 的座位。
# bms.scatter(5, 1); // 返回 False
#                    // 总共只剩下 1 个座位。
 
# 提示：
# 1 <= n <= 5 * 10^4
# 1 <= m, k <= 10^9
# 0 <= maxRow <= n - 1
# gather 和 scatter 总 调用次数不超过 5 * 10^4 次。

# Hard

from typing import List
# @lc code=start

# 线段树

class BookMyShow:

    def __init__(self, n: int, m: int):
        # 维护区间
        self.n = n
        self.m = m
        self.min = [0] * (2 << n.bit_length())
        self.sum = [0] * (2 << n.bit_length())

    def update(self, o: int, l: int, r: int, i: int, val: int) -> None:
        if l == r: # 找到🍃节点
            self.min[o] += val
            self.sum[o] += val
            return
        m = (l + r) >> 1
        if i <= m:
            self.update(o << 1, l, m, i, val)
        else:
            self.update((o << 1) + 1, m + 1, r, i, val)
        self.min[o] = min(self.min[o << 1], self.min[(o << 1) + 1])
        self.sum[o] = self.sum[o << 1] + self.sum[(o << 1) + 1]

    # 返回区间[L, R]内的元素和
    def querySum(self, o: int, l: int, r: int, L: int, R: int) -> int:
        if L <= l and r <= R: # 全区间覆盖
            return self.sum[o]
        res = 0
        m = (l + r) >> 1
        if L <= m:
            res = self.querySum(o << 1, l, m, L, R)
        if R > m:
            res += self.querySum((o << 1) + 1, m + 1, r, L, R)
        return res
    
    # 返回区间[0, R]中 <= val的最靠左的位置，不存在时返回-1
    def findFirst(self, o: int, l: int, r: int, R: int, val: int) -> int:
        if self.min[o] > val:
            return -1
        if l == r:
            return l
        m = (l + r) >> 1
        if self.min[o << 1] <= val:
            return self.findFirst(o << 1, l, m, R, val)
        elif R > m:
            return self.findFirst((o << 1) + 1, m + 1, r, R, val)
        return -1

    def gather(self, k: int, maxRow: int) -> List[int]:
        r = self.findFirst(1, 0, self.n - 1, maxRow, self.m - k)
        if r < 0:
            return []
        c = self.querySum(1, 0, self.n - 1, r, r)
        self.update(1, 0, self.n - 1, r, k) # 占座
        return [r, c]

    def scatter(self, k: int, maxRow: int) -> bool:
        s = self.querySum(1, 0, self.n - 1, 0, maxRow)
        if s > self.m * (maxRow + 1) - k:
            # 空位不够了
            return False
        # 从第一个没坐满的行开始
        i = self.findFirst(1, 0, self.n - 1, maxRow, self.m - 1)
        while k:
            left = min(self.m - self.querySum(1, 0, self.n - 1, i, i), k)
            self.update(1, 0, self.n - 1, i, left) # 占座
            k -= left
            i += 1
        return True

# Your BookMyShow object will be instantiated and called as such:
# obj = BookMyShow(n, m)
# param_1 = obj.gather(k,maxRow)
# param_2 = obj.scatter(k,maxRow)
# @lc code=end

if __name__ == "__main__":
    bms = BookMyShow(2, 5)
    print(bms.gather(4, 0)) # [0,0]
    print(bms.gather(2, 0)) # []
    print(bms.scatter(5, 1)) # True
    print(bms.scatter(5, 1)) # False
