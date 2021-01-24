#
# @lc app=leetcode.cn id=1319 lang=python3
#
# [1319] 连通网络的操作次数
#

from typing import List
# @lc code=start


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1

        group = list(range(n))

        def find(idx: int) -> int:
            if idx != group[idx]:
                group[idx] = find(group[idx])
            return group[idx]

        def connect(idx1: int, idx2: int):
            g1, g2 = find(idx1), find(idx2)
            if g1 != g2:
                group[g1] = g2

        for i1, i2 in connections:
            connect(i1, i2)

        return len(set([find(i) for i in range(n)])) - 1
        # @lc code=end


if __name__ == "__main__":
    solution = Solution()
    print(solution.makeConnected(4, [[0, 1], [0, 2], [1, 2]]))
    print(solution.makeConnected(6, [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3]]))
    print(solution.makeConnected(6, [[0, 1], [0, 2], [0, 3], [1, 2]]))
    print(solution.makeConnected(5, [[0, 1], [0, 2], [3, 4], [2, 3]]))
