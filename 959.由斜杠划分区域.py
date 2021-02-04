#
# @lc app=leetcode.cn id=959 lang=python3
#
# [959] 由斜杠划分区域
#

from typing import List, Tuple
# @lc code=start


class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        if not grid:
            return 0

        # 每个格的上右下左，分别标记为0，1，2，3
        # 并查集
        group = {}

        def find(e: Tuple) -> Tuple:
            g = group.get(e, e)
            if g != e:
                g = find(g)
                group[e] = g
            elif e not in group:
                group[e] = g
            return g

        def union(e1: Tuple, e2: Tuple):
            g1, g2 = find(e1), find(e2)
            group[g1] = g2

        N = len(grid)
        for row, line in enumerate(grid):
            for col, cell in enumerate(line):
                if cell == " ":
                    union((row, col, 0), (row, col, 1))
                    union((row, col, 0), (row, col, 2))
                    union((row, col, 0), (row, col, 3))
                elif cell == "/":
                    union((row, col, 0), (row, col, 3))
                    union((row, col, 1), (row, col, 2))
                else:
                    union((row, col, 0), (row, col, 1))
                    union((row, col, 2), (row, col, 3))

                if row > 0:
                    union((row, col, 0), (row-1, col, 2))
                if row < N - 1:
                    union((row, col, 2), (row+1, col, 0))
                if col > 0:
                    union((row, col, 3), (row, col-1, 1))
                if col < N - 1:
                    union((row, col, 1), (row, col+1, 3))

        return len(set([find(e) for e in group]))

        # @lc code=end


if __name__ == "__main__":
    solution = Solution()
    print(solution.regionsBySlashes([" /",
                                     "/ "]))
    print(solution.regionsBySlashes([" /",
                                     "  "]))
    print(solution.regionsBySlashes(["\\/",
                                     "/\\"]))
    print(solution.regionsBySlashes(["/\\",
                                     "\\/"]))
    print(solution.regionsBySlashes(["//",
                                     "/ "]))
