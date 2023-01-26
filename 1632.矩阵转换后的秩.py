#
# @lc app=leetcode.cn id=1632 lang=python3
#
# [1632] 矩阵转换后的秩
#
# 给你一个 m x n 的矩阵 matrix ，请你返回一个新的矩阵 answer ，其中 answer[row][col] 是 matrix[row][col] 的秩。

# 每个元素的 秩 是一个整数，表示这个元素相对于其他元素的大小关系，它按照如下规则计算：

# 秩是从 1 开始的一个整数。
# 如果两个元素 p 和 q 在 同一行 或者 同一列 ，那么：
# 如果 p < q ，那么 rank(p) < rank(q)
# 如果 p == q ，那么 rank(p) == rank(q)
# 如果 p > q ，那么 rank(p) > rank(q)
# 秩 需要越 小 越好。
# 题目保证按照上面规则 answer 数组是唯一的。


# 示例 1：
# 输入：matrix = [[1,2],[3,4]]
# 输出：[[1,2],[2,3]]
# 解释：
# matrix[0][0] 的秩为 1 ，因为它是所在行和列的最小整数。
# matrix[0][1] 的秩为 2 ，因为 matrix[0][1] > matrix[0][0] 且 matrix[0][0] 的秩为 1 。
# matrix[1][0] 的秩为 2 ，因为 matrix[1][0] > matrix[0][0] 且 matrix[0][0] 的秩为 1 。
# matrix[1][1] 的秩为 3 ，因为 matrix[1][1] > matrix[0][1]， matrix[1][1] > matrix[1][0] 且 matrix[0][1] 和 matrix[1][0] 的秩都为 2 。

# 示例 2：
# 输入：matrix = [[7,7],[7,7]]
# 输出：[[1,1],[1,1]]

# 示例 3：
# 输入：matrix = [[20,-21,14],[-19,4,19],[22,-47,24],[-19,4,19]]
# 输出：[[4,2,3],[1,3,4],[5,1,6],[1,3,4]]

# 示例 4：
# 输入：matrix = [[7,3,6],[1,4,5],[9,8,2]]
# 输出：[[5,1,4],[1,2,3],[6,3,1]]


# 提示：
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 500
# -10 ^ 9 <= matrix[row][col] <= 10 ^ 9

# Hard
# 并查集

from collections import Counter, defaultdict, deque
from typing import List
# @lc code=start


class Solution:
    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        uf = UnionFind(m, n)
        for i, row in enumerate(matrix):
            num2indexList = defaultdict(list)
            for j, num in enumerate(row):
                num2indexList[num].append([i, j])
            for indexList in num2indexList.values():
                i1, j1 = indexList[0]
                for k in range(1, len(indexList)):
                    i2, j2 = indexList[k]
                    uf.union(i1, j1, i2, j2)
        for j in range(n):
            num2indexList = defaultdict(list)
            for i in range(m):
                num2indexList[matrix[i][j]].append([i, j])
            for indexList in num2indexList.values():
                i1, j1 = indexList[0]
                for k in range(1, len(indexList)):
                    i2, j2 = indexList[k]
                    uf.union(i1, j1, i2, j2)

        degree = Counter()
        adj = defaultdict(list)
        for i, row in enumerate(matrix):
            num2index = {}
            for j, num in enumerate(row):
                num2index[num] = (i, j)
            sortedArray = sorted(num2index.keys())
            for k in range(1, len(sortedArray)):
                i1, j1 = num2index[sortedArray[k - 1]]
                i2, j2 = num2index[sortedArray[k]]
                ri1, rj1 = uf.find(i1, j1)
                ri2, rj2 = uf.find(i2, j2)
                degree[(ri2, rj2)] += 1
                adj[(ri1, rj1)].append([ri2, rj2])
        for j in range(n):
            num2index = {}
            for i in range(m):
                num = matrix[i][j]
                num2index[num] = (i, j)
            sortedArray = sorted(num2index.keys())
            for k in range(1, len(sortedArray)):
                i1, j1 = num2index[sortedArray[k - 1]]
                i2, j2 = num2index[sortedArray[k]]
                ri1, rj1 = uf.find(i1, j1)
                ri2, rj2 = uf.find(i2, j2)
                degree[(ri2, rj2)] += 1
                adj[(ri1, rj1)].append([ri2, rj2])

        rootSet = set()
        ranks = {}
        for i in range(m):
            for j in range(n):
                ri, rj = uf.find(i, j)
                rootSet.add((ri, rj))
                ranks[(ri, rj)] = 1
        q = deque([[i, j] for i, j in rootSet if degree[(i, j)] == 0])
        while q:
            i, j = q.popleft()
            for ui, uj in adj[(i, j)]:
                degree[(ui, uj)] -= 1
                if degree[(ui, uj)] == 0:
                    q.append([ui, uj])
                ranks[(ui, uj)] = max(ranks[(ui, uj)], ranks[(i, j)] + 1)
        res = [[1] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                ri, rj = uf.find(i, j)
                res[i][j] = ranks[(ri, rj)]
        return res


class UnionFind:
    def __init__(self, m, n):
        self.m = m
        self.n = n
        self.root = [[[i, j] for j in range(n)] for i in range(m)]
        self.size = [[1] * n for _ in range(m)]

    def find(self, i, j):
        ri, rj = self.root[i][j]
        if [ri, rj] == [i, j]:
            return [i, j]
        self.root[i][j] = self.find(ri, rj)
        return self.root[i][j]

    def union(self, i1, j1, i2, j2):
        ri1, rj1 = self.find(i1, j1)
        ri2, rj2 = self.find(i2, j2)
        if [ri1, rj1] != [ri2, rj2]:
            if self.size[ri1][rj1] >= self.size[ri2][rj2]:
                self.root[ri2][rj2] = [ri1, rj1]
                self.size[ri1][rj1] += self.size[ri2][rj2]
            else:
                self.root[ri1][rj1] = [ri2, rj2]
                self.size[ri2][rj2] += self.size[ri1][rj1]
        # @lc code=end


if __name__ == "__main__":
    solution = Solution()
    print(solution.matrixRankTransform([[1, 2], [3, 4]]))  # [[1,2],[2,3]]
    print(solution.matrixRankTransform([[7, 7], [7, 7]]))  # [[1,1],[1,1]]
    # [[4,2,3],[1,3,4],[5,1,6],[1,3,4]]
    print(solution.matrixRankTransform(
        [[20, -21, 14], [-19, 4, 19], [22, -47, 24], [-19, 4, 19]]))
    # [[5,1,4],[1,2,3],[6,3,1]]
    print(solution.matrixRankTransform([[7, 3, 6], [1, 4, 5], [9, 8, 2]]))
