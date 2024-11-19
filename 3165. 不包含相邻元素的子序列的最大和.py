# 给你一个整数数组 nums 和一个二维数组 queries，其中 queries[i] = [posi, xi]。

# 对于每个查询 i，首先将 nums[posi] 设置为 xi，然后计算查询 i 的答案，该答案为 nums 中 不包含相邻元素 的子序列 的 最大 和。

# 返回所有查询的答案之和。
# 由于最终答案可能非常大，返回其对 10^9 + 7 取余 的结果。
# 子序列 是指从另一个数组中删除一些或不删除元素而不改变剩余元素顺序得到的数组。


# 示例 1：
# 输入：nums = [3,5,9], queries = [[1,-2],[0,-3]]
# 输出：21
# 解释：
# 执行第 1 个查询后，nums = [3,-2,9]，不包含相邻元素的子序列的最大和为 3 + 9 = 12。
# 执行第 2 个查询后，nums = [-3,-2,9]，不包含相邻元素的子序列的最大和为 9 。

# 示例 2：
# 输入：nums = [0,-1], queries = [[0,-5]]
# 输出：0
# 解释：
# 执行第 1 个查询后，nums = [-5,-1]，不包含相邻元素的子序列的最大和为 0（选择空子序列）。


# 提示：
# 1 <= nums.length <= 5 * 10^4
# -10^5 <= nums[i] <= 10^5
# 1 <= queries.length <= 5 * 10^4
# queries[i] == [posi, xi]
# 0 <= posi <= nums.length - 1
# -10^5 <= xi <= 10^5

# Hard
# 复习
# 参考198

from typing import List

class SegNode:
    def __init__(self) -> None:
        # self.vxx代表本区间左右边界选择情况下能达到的最大值
        self.v00 = self.v01 = self.v10 = self.v11 = 0

    def setValue(self, v: int) -> None:
        self.v00 = self.v01 = self.v10 = 0
        self.v11 = max(v, 0)
    
    def best(self) -> int:
        return self.v11
    
class SegTree:
    def __init__(self, n: int) -> None:
        self.n = n
        self.tree = [SegNode() for _ in range(n * 4 + 1)]

    def init(self, nums: List[int]) -> None:
        def _internalInit(x: int, l: int, r: int) -> None:
            if l == r:
                self.tree[x].setValue(nums[l-1])
                return
            mid = (l + r) >> 1
            _internalInit(x << 1, l, mid)
            _internalInit(x << 1 | 1, mid + 1, r)
            self.pushup(x)
        _internalInit(1, 1, self.n)

    def update(self, x: int, v: int) -> None:
        def _internalUpdate(x: int, l: int, r: int, pos: int, v: int) -> None:
            if l > pos or r < pos:
                return
            if l == r:
                self.tree[x].setValue(v)
                return
            mid = (l + r) >> 1
            _internalUpdate(x << 1, l, mid, pos, v)
            _internalUpdate(x << 1 | 1, mid + 1, r, pos, v)
            self.pushup(x)
        _internalUpdate(1, 1, self.n, x + 1, v)

    def query(self) -> int:
        return self.tree[1].best()
    
    def pushup(self, x: int) -> None:
        _t = self.tree
        l, r = x << 1, x << 1 | 1
        _t[x].v00 = max(_t[l].v00 + _t[r].v10, _t[l].v01 + _t[r].v00)
        _t[x].v01 = max(_t[l].v00 + _t[r].v11, _t[l].v01 + _t[r].v01)
        _t[x].v10 = max(_t[l].v10 + _t[r].v10, _t[l].v11 + _t[r].v00)
        _t[x].v11 = max(_t[l].v10 + _t[r].v11, _t[l].v11 + _t[r].v01)

class Solution:
    def maximumSumSubsequence(self, nums: List[int], queries: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        # 如果没有修改操作，同198题情况，动规可解
        # 有修改的情况下，选当前元素和不选当前元素，都可以分解成左右两个子问题
        # 带修改操作的子问题，可以用线段树
        # 线段树每个节点四个属性：分别对应左右边界（闭区间），左右边界的选择情况
        # 0：代表边界元素未选；1：代表边界元素可能被选

        tree = SegTree(len(nums))
        tree.init(nums)

        res = 0
        for x, v in queries:
            tree.update(x, v)
            res += tree.query()

        return res % MOD

if __name__ == "__main__":
    solution = Solution()
    print(solution.maximumSumSubsequence([3,5,9], [[1,-2],[0,-3]])) # 21
    print(solution.maximumSumSubsequence([0,-1], [[0,-5]])) # 0
    