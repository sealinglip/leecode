#
# @lc app=leetcode.cn id=289 lang=python3
#
# [289] 生命游戏
#
# 根据 百度百科 ， 生命游戏 ，简称为 生命 ，是英国数学家约翰·何顿·康威在 1970 年发明的细胞自动机。

# 给定一个包含 m × n 个格子的面板，每一个格子都可以看成是一个细胞。每个细胞都具有一个初始状态： 1 即为 活细胞 （live），或 0 即为 死细胞 （dead）。每个细胞与其八个相邻位置（水平，垂直，对角线）的细胞都遵循以下四条生存定律：

# 如果活细胞周围八个位置的活细胞数少于两个，则该位置活细胞死亡；
# 如果活细胞周围八个位置有两个或三个活细胞，则该位置活细胞仍然存活；
# 如果活细胞周围八个位置有超过三个活细胞，则该位置活细胞死亡；
# 如果死细胞周围正好有三个活细胞，则该位置死细胞复活；
# 下一个状态是通过将上述规则同时应用于当前状态下的每个细胞所形成的，其中细胞的出生和死亡是同时发生的。给你 m x n 网格面板 board 的当前状态，返回下一个状态。


# 示例 1：
# 输入：board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
# 输出：[[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]]

# 示例 2：
# 输入：board = [[1, 1], [1, 0]]
# 输出：[[1, 1], [1, 1]]

# 提示：
# m == board.length
# n == board[i].length
# 1 <= m, n <= 25
# board[i][j] 为 0 或 1


# 进阶：
# 你可以使用原地算法解决本题吗？请注意，面板上所有格子需要同时被更新：你不能先更新某些格子，然后使用它们的更新后的值再更新其他格子。
# 本题中，我们使用二维数组来表示面板。原则上，面板是无限的，但当活细胞侵占了面板边界时会造成问题。你将如何解决这些问题？


from typing import List
# @lc code=start


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        preSum = [[0] * (n + 1) for _ in range(m + 1)]  # 保存以该点为右下角的区域中活细胞数量
        for r in range(m):
            for c in range(n):
                preSum[r+1][c+1] = board[r][c] + \
                    preSum[r][c+1] + preSum[r+1][c] - preSum[r][c]

        for r in range(m):
            for c in range(n):
                surrounding = preSum[min(r+2, m)][min(c+2, n)] - preSum[min(r+2, m)
                                                                        ][max(c-1, 0)] - preSum[max(r-1, 0)][min(c+2, n)] + preSum[max(r-1, 0)][max(c-1, 0)] - board[r][c]
                if board[r][c]:
                    if surrounding > 3 or surrounding < 2:
                        board[r][c] = 0
                elif surrounding == 3:
                    board[r][c] = 1

                # @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
    board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
    solution.gameOfLife(board)
    print(board)
    board = [[1, 1], [1, 0]]
    solution.gameOfLife(board)
    print(board)  # [[1,1],[1,1]]
