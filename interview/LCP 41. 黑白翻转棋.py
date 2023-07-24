# 在 n*m 大小的棋盘中，有黑白两种棋子，黑棋记作字母 "X", 白棋记作字母 "O"，空余位置记作 "."。
# 当落下的棋子与其他相同颜色的棋子在行、列或对角线完全包围（中间不存在空白位置）另一种颜色的棋子，则可以翻转这些棋子的颜色。

# 「力扣挑战赛」黑白翻转棋项目中，将提供给选手一个未形成可翻转棋子的棋盘残局，其状态记作 chessboard。
# 若下一步可放置一枚黑棋，请问选手最多能翻转多少枚白棋。

# 注意：
# 若翻转白棋成黑棋后，棋盘上仍存在可以翻转的白棋，将可以 继续 翻转白棋
# 输入数据保证初始棋盘状态无可以翻转的棋子且存在空余位置

# 示例 1：
# 输入：chessboard = ["....X.","....X.","XOOO..","......","......"]
# 输出：3
# 解释：
# 可以选择下在 [2,4] 处，能够翻转白方三枚棋子。

# 示例 2：
# 输入：chessboard = [".X.",".O.","XO."]
# 输出：2
# 解释：
# 可以选择下在 [2,2] 处，能够翻转白方两枚棋子。

# 示例 3：
# 输入：chessboard = [".......",".......",".......","X......",".O.....","..O....","....OOX"]
# 输出：4
# 解释：
# 可以选择下在 [6,3] 处，能够翻转白方四枚棋子。

# 提示：
# 1 <= chessboard.length, chessboard[i].length <= 8
# chessboard[i] 仅包含 "."、"O" 和 "X"

from collections import deque
from typing import List


class Solution:
    def flipChess(self, chessboard: List[str]) -> int:
        DIR = [-1, -1, 0, -1, 1, 1, 0, 1, -1]
        m, n = len(chessboard), len(chessboard[0])

        def check(chessboard: List[str], x: int, y: int, dx: int, dy: int) -> int:
            '''
            起点：[x, y]
            方向：[dx, dy]
            判断是否可以翻转白棋，如果能翻，可以走几步；不能翻，返回0
            '''
            step = 0
            x, y = x + dx, y + dy
            while 0 <= x < m and 0 <= y < n:
                if chessboard[x][y] == 'X':
                    return step
                elif chessboard[x][y] == '.':
                    return 0
                x, y = x + dx, y + dy
                step += 1
            return 0

        def tryPt(chessboard: List[str], x: int, y: int) -> int:
            # 深度拷贝
            chessboard = [list(row) for row in chessboard]
            cnt = 0
            q = deque([[x, y]])
            chessboard[x][y] = 'X'

            while q:
                tx, ty = q.popleft()
                for i in range(8):
                    dx, dy = DIR[i], DIR[i+1]
                    steps = check(chessboard, tx, ty, dx, dy)
                    for i in range(1, steps+1):
                        nx, ny = tx + dx * i, ty + dy * i
                        q.append([nx, ny])
                        chessboard[nx][ny] = 'X'
                    cnt += steps

            return cnt

        res = 0
        for i in range(m):
            for j in range(n):
                if chessboard[i][j] == '.':
                    res = max(res, tryPt(chessboard, i, j))
        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.flipChess(
        ["....X.", "....X.", "XOOO..", "......", "......"]))  # 3
    print(solution.flipChess([".X.", ".O.", "XO."]))  # 2
    print(solution.flipChess([".......", ".......", ".......",
          "X......", ".O.....", "..O....", "....OOX"]))  # 4
