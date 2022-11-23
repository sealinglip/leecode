#
# @lc app=leetcode.cn id=808 lang=python3
#
# [808] 分汤
#
# 有 A 和 B 两种类型 的汤。一开始每种类型的汤有 n 毫升。有四种分配操作：

# 提供 100ml 的 汤A 和 0ml 的 汤B 。
# 提供 75ml 的 汤A 和 25ml 的 汤B 。
# 提供 50ml 的 汤A 和 50ml 的 汤B 。
# 提供 25ml 的 汤A 和 75ml 的 汤B 。
# 每个回合，我们将从四种概率同为 0.25 的操作中进行分配选择。如果汤的剩余量不足以完成某次操作，我们将尽可能分配。当两种类型的汤都分配完时，停止操作。

# 注意 不存在先分配 100 ml 汤B 的操作。

# 需要返回的值： 汤A 先分配完的概率 + 汤A和汤B 同时分配完的概率 / 2。返回值在正确答案 10^-5 的范围内将被认为是正确的。


# 示例 1:
# 输入: n = 50
# 输出: 0.62500
# 解释: 如果我们选择前两个操作，A 首先将变为空。
# 对于第三个操作，A 和 B 会同时变为空。
# 对于第四个操作，B 首先将变为空。
# 所以 A 变为空的总概率加上 A 和 B 同时变为空的概率的一半是 0.25 * (1 + 1 + 0.5 + 0) = 0.625。

# 示例 2:
# 输入: n = 100
# 输出: 0.71875

# 提示:
# 0 <= n <= 10^9

# 复习

# @lc code=start
from functools import cache


class Solution:
    def soupServings(self, n: int) -> float:
        n = (n + 24) // 25  # 以25为一单位
        if n >= 179:
            # 每次分配操作有 (4, 0),(3, 1),(2, 2),(1, 3) 四种，那么在一次分配中，
            # 汤 A 平均会被分配的份数期望为 E(A)=(4+3+2+1)×0.25=2.5 ，
            # 汤 B 平均会被分配的份数期望为 E(B)=(0+1+2+3)×0.25=1.5。
            # 因此在 n 非常大的时候，汤 A 会有很大的概率比 B 先分配完，汤 A 被先取完的概率应该非常接近 1。
            # 实际计算可以发现，当 n ≥ 4475 时，概率大于 0.99999 了。
            return 1

        @cache
        def dfs(a: int, b: int) -> float:
            '''
            dfs(a, b) 为 A 剩 a单位，B 剩 b单位时的概率
            '''
            if a <= 0:
                if b <= 0:
                    return 0.5
                return 1
            if b <= 0:
                return 0
            return (dfs(a-4, b) + dfs(a-3, b-1) + dfs(a-2, b-2) + dfs(a-1, b-3)) / 4

        return dfs(n, n)

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.soupServings(50))  # 0.62500
    print(solution.soupServings(100))  # 0.71875
