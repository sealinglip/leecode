#
# @lc app=leetcode.cn id=803 lang=python3
#
# [803] 打砖块
#
# 有一个 m x n 的二元网格，其中 1 表示砖块，0 表示空白。砖块 稳定（不会掉落）的前提是：
# 一块砖直接连接到网格的顶部，或者
# 至少有一块相邻（4 个方向之一）砖块 稳定 不会掉落时
# 给你一个数组 hits ，这是需要依次消除砖块的位置。每当消除 hits[i] = (rowi, coli) 位置上的砖块时，对应位置的砖块（若存在）会消失，
# 然后其他的砖块可能因为这一消除操作而掉落。一旦砖块掉落，它会立即从网格中消失（即，它不会落在其他稳定的砖块上）。

# 返回一个数组 result ，其中 result[i] 表示第 i 次消除操作对应掉落的砖块数目。
# 注意，消除可能指向是没有砖块的空白位置，如果发生这种情况，则没有砖块掉落。

# 示例 1：
# 输入：grid = [[1, 0, 0, 0], [1, 1, 1, 0]], hits = [[1, 0]]
# 输出：[2]
# 解释：
# 网格开始为：
# [[1, 0, 0, 0]，
#  [1, 1, 1, 0]]
# 消除(1, 0) 处加粗的砖块，得到网格：
# [[1, 0, 0, 0]
#  [0, 1, 1, 0]]
# 两个加粗的砖不再稳定，因为它们不再与顶部相连，也不再与另一个稳定的砖相邻，因此它们将掉落。得到网格：
# [[1, 0, 0, 0],
#  [0, 0, 0, 0]]
# 因此，结果为[2] 。

# 示例 2：
# 输入：grid = [[1, 0, 0, 0], [1, 1, 0, 0]], hits = [[1, 1], [1, 0]]
# 输出：[0, 0]
# 解释：
# 网格开始为：
# [[1, 0, 0, 0],
#  [1, 1, 0, 0]]
# 消除(1, 1) 处加粗的砖块，得到网格：
# [[1, 0, 0, 0],
#  [1, 0, 0, 0]]
# 剩下的砖都很稳定，所以不会掉落。网格保持不变：
# [[1, 0, 0, 0],
#  [1, 0, 0, 0]]
# 接下来消除(1, 0) 处加粗的砖块，得到网格：
# [[1, 0, 0, 0],
#  [0, 0, 0, 0]]
# 剩下的砖块仍然是稳定的，所以不会有砖块掉落。
# 因此，结果为[0, 0] 。


# 提示：
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 200
# grid[i][j] 为 0 或 1
# 1 <= hits.length <= 4 * 10^4
# hits[i].length == 2
# 0 <= xi <= m - 1
# 0 <= yi <= n - 1
# 所有(xi, yi) 互不相同

from typing import List
# @lc code=start

# 并查集


class UnionFind:
    def __init__(self):
        self.father = {}
        self.sizeOfSet = {}

    def getSize(self, x):
        return self.sizeOfSet[self.find(x)]

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

    def isConnected(self, x, y):
        return self.find(x) == self.find(y)

    def merge(self, x, y):
        root_x, root_y = self.find(x), self.find(y)

        if root_x != root_y:
            self.father[root_x] = root_y
            self.sizeOfSet[root_y] += self.sizeOfSet[root_x]
            del self.sizeOfSet[root_x]

    def add(self, x):
        if x not in self.father:
            self.father[x] = x
            self.sizeOfSet[x] = 1


class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        uf = UnionFind()
        m, n = len(grid), len(grid[0])

        DIRECTION = ((1, 0), (-1, 0), (0, 1), (0, -1))
        CEIL = (-1, -1)
        uf.add(CEIL)  # 添加天花板

        # 先假设hits命中的位置本来没有砖块
        for x, y in hits:
            grid[x][y] -= 1

        def brickInBound(x: int, y: int) -> bool:
            return 0 <= x < m and 0 <= y < n and grid[x][y] == 1

        # 连接，合并剩余的砖块，得到各连通集
        def mergeNeighbors(i: int, j: int):
            for dx, dy in DIRECTION:
                x, y = i + dx, j + dy
                if brickInBound(x, y):
                    uf.merge((x, y), (i, j))

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    uf.add((i, j))

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    mergeNeighbors(i, j)

        for j in range(n):
            if grid[0][j] == 1:
                uf.merge((0, j), CEIL)

        res = [0] * len(hits)
        for i in range(len(hits)-1, -1, -1):
            # 逆序撤销敲击
            x, y = hits[i][0], hits[i][1]

            grid[x][y] += 1
            if grid[x][y] == 1:
                # 敲击后与天花板连接的数量
                afterHit = uf.getSize(CEIL)

                uf.add((x, y))
                mergeNeighbors(x, y)
                if x == 0:
                    uf.merge((x, y), CEIL)

                # 撤销敲击，如果被敲的地方和天花板相连
                if uf.isConnected((x, y), CEIL):
                    beforeHit = uf.getSize(CEIL)
                    res[i] = beforeHit - afterHit - 1  # -1是砖块本身
        return res


        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.hitBricks([[1, 0, 0, 0], [1, 1, 1, 0]], [[1, 0]]))
    print(solution.hitBricks([[1, 0, 0, 0], [1, 1, 0, 0]], [[1, 1], [1, 0]]))
