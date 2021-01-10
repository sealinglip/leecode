#
# @lc app=leetcode.cn id=547 lang=python3
#
# [547] 省份数量
#
# 有 n 个城市，其中一些彼此相连，另一些没有相连。如果城市 a 与城市 b 直接相连，且城市 b 与城市 c 直接相连，那么城市 a 与城市 c 间接相连。
# 省份 是一组直接或间接相连的城市，组内不含其他没有相连的城市。
# 给你一个 n x n 的矩阵 isConnected ，其中 isConnected[i][j] = 1 表示第 i 个城市和第 j 个城市直接相连，而 isConnected[i][j] = 0 表示二者不直接相连。
# 返回矩阵中 省份 的数量。

# 示例 1：
# 输入：isConnected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
# 输出：2

# 示例 2：
# 输入：isConnected = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
# 输出：3

# 提示：
# 1 <= n <= 200
# n == isConnected.length
# n == isConnected[i].length
# isConnected[i][j] 为 1 或 0
# isConnected[i][i] == 1
# isConnected[i][j] == isConnected[j][i]

from typing import List
# @lc code=start


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        N = len(isConnected)  # 维度
        # 土法

        def getGroup(i: int) -> int:
            if groups[i] != i:
                groups[i] = getGroup(groups[i])
            return groups[i]

        def group(a: int, b: int):
            groups[getGroup(a)] = getGroup(b)

        groups = list(range(N))  # 标记第i个城市归属于哪个组
        for a in range(N):
            for b in range(a + 1, N):
                if isConnected[a][b] == 1:
                    group(a, b)

        return sum(groups[i] == i for i in range(N))

        # 深度优先
        # def dfs(i: int):
        #     for j in range(N):
        #         if isConnected[i][j] == 1 and j not in visited:
        #             visited.add(j)
        #             dfs(j)

        # visited = set()
        # circles = 0

        # for i in range(N):
        #     if i not in visited:
        #         dfs(i)
        #         circles += 1

        # return circles
# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    print(solution.findCircleNum(
        [[1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]]))
    print(solution.findCircleNum(
        [[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 1, 1]]))
    print(solution.findCircleNum([[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
    print(solution.findCircleNum([[1, 1, 1], [1, 1, 1], [1, 1, 1]]))
    print(solution.findCircleNum([[1, 0, 0], [0, 1, 0], [0, 0, 1]]))
