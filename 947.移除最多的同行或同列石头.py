#
# @lc app=leetcode.cn id=947 lang=python3
#
# [947] 移除最多的同行或同列石头
#
# n 块石头放置在二维平面中的一些整数坐标点上。每个坐标点上最多只能有一块石头。
# 如果一块石头的 同行或者同列 上有其他石头存在，那么就可以移除这块石头。
# 给你一个长度为 n 的数组 stones ，其中 stones[i] = [xi, yi] 表示第 i 块石头的位置，返回
# 可以移除的石子 的最大数量。

# 示例 1：
# 输入：stones = [[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]
# 输出：5
# 解释：一种移除 5 块石头的方法如下所示：
# 1. 移除石头[2, 2] ，因为它和[2, 1] 同行。
# 2. 移除石头[2, 1] ，因为它和[0, 1] 同列。
# 3. 移除石头[1, 2] ，因为它和[1, 0] 同行。
# 4. 移除石头[1, 0] ，因为它和[0, 0] 同列。
# 5. 移除石头[0, 1] ，因为它和[0, 0] 同行。
# 石头[0, 0] 不能移除，因为它没有与另一块石头同行/列。

# 示例 2：
# 输入：stones = [[0, 0], [0, 2], [1, 1], [2, 0], [2, 2]]
# 输出：3
# 解释：一种移除 3 块石头的方法如下所示：
# 1. 移除石头[2, 2] ，因为它和[2, 0] 同行。
# 2. 移除石头[2, 0] ，因为它和[0, 0] 同列。
# 3. 移除石头[0, 2] ，因为它和[0, 0] 同行。
# 石头[0, 0] 和[1, 1] 不能移除，因为它们没有与另一块石头同行/列。

# 示例 3：
# 输入：stones = [[0, 0]]
# 输出：0
# 解释：[0, 0] 是平面上唯一一块石头，所以不可以移除它。

# 提示：
# 1 <= stones.length <= 1000
# 0 <= xi, yi <= 10^4
# 不会有两块石头放在同一个坐标点上

from typing import List
# @lc code=start

# 并查集


class UnionFind:
    def __init__(self, N):
        self.father = {i: i for i in range(N)}

    def find(self, x):
        root = self.father[x]
        if root == x:
            return root
        else:
            f = self.father[root]
            if root != f:
                while self.father[f] != f:
                    f = self.father[f]
                root = f

                # 路径压缩
                while x != root:
                    original_father = self.father[x]
                    self.father[x] = root
                    x = original_father

            return root

    def merge(self, x, y):
        root_x, root_y = self.find(x), self.find(y)

        if root_x != root_y:
            self.father[root_x] = root_y


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        if not stones:
            return 0

        # 构建并查集
        ufs = UnionFind(20000)
        for x, y in stones:
            ufs.merge(x, y+10000)
        return len(stones)-len({ufs.find(x) for x, y in stones})
# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    print(solution.removeStones(
        [[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]))
    print(solution.removeStones([[0, 0], [0, 2], [1, 1], [2, 0], [2, 2]]))
    print(solution.removeStones([[0, 0]]))
