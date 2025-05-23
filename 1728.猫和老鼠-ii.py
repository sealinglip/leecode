#
# @lc app=leetcode.cn id=1728 lang=python3
#
# [1728] 猫和老鼠 II
#
# 一只猫和一只老鼠在玩一个叫做猫和老鼠的游戏。

# 它们所处的环境设定是一个 rows x cols 的方格 grid ，其中每个格子可能是一堵墙、一块地板、一位玩家（猫或者老鼠）或者食物。

# 玩家由字符 'C' （代表猫）和 'M' （代表老鼠）表示。
# 地板由字符 '.' 表示，玩家可以通过这个格子。
# 墙用字符 '#' 表示，玩家不能通过这个格子。
# 食物用字符 'F' 表示，玩家可以通过这个格子。
# 字符 'C' ， 'M' 和 'F' 在 grid 中都只会出现一次。
# 猫和老鼠按照如下规则移动：

# 老鼠 先移动 ，然后两名玩家轮流移动。
# 每一次操作时，猫和老鼠可以跳到上下左右四个方向之一的格子，他们不能跳过墙也不能跳出 grid 。
# catJump 和 mouseJump 是猫和老鼠分别跳一次能到达的最远距离，它们也可以跳小于最大距离的长度。
# 它们可以停留在原地。
# 老鼠可以跳跃过猫的位置。
# 游戏有 4 种方式会结束：

# 如果猫跟老鼠处在相同的位置，那么猫获胜。
# 如果猫先到达食物，那么猫获胜。
# 如果老鼠先到达食物，那么老鼠获胜。
# 如果老鼠不能在 1000 次操作以内到达食物，那么猫获胜。
# 给你 rows x cols 的矩阵 grid 和两个整数 catJump 和 mouseJump ，双方都采取最优策略，如果老鼠获胜，那么请你返回 true ，否则返回 false 。


# 示例 1：
# 输入：grid = ["####F", "#C...", "M...."], catJump = 1, mouseJump = 2
# 输出：true
# 解释：猫无法抓到老鼠，也没法比老鼠先到达食物。

# 示例 2：
# 输入：grid = ["M.C...F"], catJump = 1, mouseJump = 4
# 输出：true

# 示例 3：
# 输入：grid = ["M.C...F"], catJump = 1, mouseJump = 3
# 输出：false

# 示例 4：
# 输入：grid = ["C...#", "...#F", "....#", "M...."], catJump = 2, mouseJump = 5
# 输出：false

# 示例 5：
# 输入：grid = [".M...", "..#..", "#..#.", "C#.#.", "...#F"], catJump = 3, mouseJump = 1
# 输出：true


# 提示：
# rows == grid.length
# cols = grid[i].length
# 1 <= rows, cols <= 8
# grid[i][j] 只包含字符 'C' ，'M' ，'F' ，'.' 和 '#' 。
# grid 中只包含一个 'C' ，'M' 和 'F' 。
# 1 <= catJump, mouseJump <= 8

# Hard
# 复习
from functools import lru_cache
from typing import List, Tuple
# @lc code=start
DIRS = ((0, 1), (0, -1), (1, 0), (-1, 0))


class Solution:
    def canMouseWin(self, grid: List[str], catJump: int, mouseJump: int) -> bool:
        ROWS, COLS = len(grid), len(grid[0])
        WALLS = set()
        CELLS = ROWS * COLS  # 可到达的格子数，下面要遍历棋盘减掉墙
        cat = mouse = food = None
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 'F':
                    food = (i, j)
                elif grid[i][j] == 'M':
                    mouse = (i, j)
                elif grid[i][j] == 'C':
                    cat = (i, j)
                elif grid[i][j] == '#':
                    WALLS.add((i, j))
                    CELLS -= 1

        @lru_cache(None)
        def dfs(cat: Tuple[int, int], mouse: Tuple[int, int], turn: int) -> bool:
            '''返回值：🐭是否会赢'''
            if cat == food or cat == mouse or turn >= min(CELLS << 1, 1000):
                return False
            if mouse == food:
                return True

            # 轮到🐭移动
            if turn & 1 == 0:
                r, c = mouse
                for dr, dc in DIRS:
                    for j in range(mouseJump + 1):
                        nr, nc = r + j * dr, c + j * dc
                        if 0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in WALLS:
                            # 位置有效
                            if dfs(cat, (nr, nc), turn + 1):
                                return True
                        else:
                            break
                return False
            # 轮到🐱移动
            else:
                r, c = cat
                for dr, dc in DIRS:
                    for j in range(catJump + 1):
                        nr, nc = r + j * dr, c + j * dc
                        if 0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in WALLS:
                            # 位置有效
                            if not dfs((nr, nc), mouse, turn + 1):
                                return False
                        else:
                            break
                return True

        return dfs(cat, mouse, 0)

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.canMouseWin(
        ["####F", "#C...", "M...."], 1, 2))  # True
    print(solution.canMouseWin(
        ["M.C...F"], 1, 4))  # True
    print(solution.canMouseWin(
        ["M.C...F"], 1, 3))  # False
    print(solution.canMouseWin(
        ["C...#", "...#F", "....#", "M...."], 2, 5))  # False
    print(solution.canMouseWin(
        [".M...", "..#..", "#..#.", "C#.#.", "...#F"], 3, 1))  # True
