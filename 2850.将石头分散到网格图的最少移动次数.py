#
# @lc app=leetcode.cn id=2850 lang=python3
#
# [2850] 将石头分散到网格图的最少移动次数
#
# 给你一个大小为 3 * 3 ，下标从 0 开始的二维整数矩阵 grid ，分别表示每一个格子里石头的数目。网格图中总共恰好有 9 个石头，一个格子里可能会有 多个 石头。

# 每一次操作中，你可以将一个石头从它当前所在格子移动到一个至少有一条公共边的相邻格子。

# 请你返回每个格子恰好有一个石头的 最少移动次数 。


# 示例 1：
# 输入：grid = [[1,1,0],[1,1,1],[1,2,1]]
# 输出：3
# 解释：让每个格子都有一个石头的一个操作序列为：
# 1 - 将一个石头从格子 (2,1) 移动到 (2,2) 。
# 2 - 将一个石头从格子 (2,2) 移动到 (1,2) 。
# 3 - 将一个石头从格子 (1,2) 移动到 (0,2) 。
# 总共需要 3 次操作让每个格子都有一个石头。
# 让每个格子都有一个石头的最少操作次数为 3 。

# 示例 2：
# 输入：grid = [[1,3,0],[1,0,0],[1,0,3]]
# 输出：4
# 解释：让每个格子都有一个石头的一个操作序列为：
# 1 - 将一个石头从格子 (0,1) 移动到 (0,2) 。
# 2 - 将一个石头从格子 (0,1) 移动到 (1,1) 。
# 3 - 将一个石头从格子 (2,2) 移动到 (1,2) 。
# 4 - 将一个石头从格子 (2,2) 移动到 (2,1) 。
# 总共需要 4 次操作让每个格子都有一个石头。
# 让每个格子都有一个石头的最少操作次数为 4 。
 

# 提示：
# grid.length == grid[i].length == 3
# 0 <= grid[i][j] <= 9
# grid 中元素之和为 9 。

# 复习

from itertools import permutations
from math import inf
from typing import List
# @lc code=start
class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        # 找出多于一个的格和没有石子的格
        empty = []
        more = []
        for i in range(3):
            for j in range(3):
                if grid[i][j] > 1:
                    more.extend([(i, j)] * (grid[i][j] - 1))
                elif grid[i][j] == 0:
                    empty.append((i, j))

        # 枚举empty的排列，跟more一一match之后算总步数
        res = inf
        for perm in permutations(empty):
            moves = 0
            for (u, v), (i, j) in zip(more, perm):
                moves += abs(u-i) + abs(v-j)
            res = min(res, moves)
        return res
            

# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.minimumMoves([[3,2,0],[0,1,0],[0,3,0]])) # 7
    print(solution.minimumMoves([[1,1,0],[1,1,1],[1,2,1]])) # 3
    print(solution.minimumMoves([[1,3,0],[1,0,0],[1,0,3]])) # 4
