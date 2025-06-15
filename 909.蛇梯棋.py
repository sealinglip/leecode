#
# @lc app=leetcode.cn id=909 lang=python3
#
# [909] 蛇梯棋
#
# N x N 的棋盘 board 上，按从 1 到 N*N 的数字给方格编号，编号 从左下角开始，每一行交替方向。
# 例如，一块 6 x 6 大小的棋盘，编号如下：


# r 行 c 列的棋盘，按前述方法编号，棋盘格中可能存在 “蛇” 或 “梯子”；如果 board[r][c] != -1，那个蛇或梯子的目的地将会是 board[r][c]。
# 玩家从棋盘上的方格 1 （总是在最后一行、第一列）开始出发。
# 每一回合，玩家需要从当前方格 x 开始出发，按下述要求前进：
# 选定目标方格：选择从编号 x+1，x+2，x+3，x+4，x+5，或者 x+6 的方格中选出一个目标方格 s ，目标方格的编号 <= N*N。
# 该选择模拟了掷骰子的情景，无论棋盘大小如何，你的目的地范围也只能处于区间[x+1, x+6] 之间。
# 传送玩家：如果目标方格 S 处存在蛇或梯子，那么玩家会传送到蛇或梯子的目的地。否则，玩家传送到目标方格 S。
# 注意，玩家在每回合的前进过程中最多只能爬过蛇或梯子一次：就算目的地是另一条蛇或梯子的起点，你也不会继续移动。

# 返回达到方格 N*N 所需的最少移动次数，如果不可能，则返回 - 1。

# 示例1：
# 输入：[
#     [-1, -1, -1, -1, -1, -1],
#     [-1, -1, -1, -1, -1, -1],
#     [-1, -1, -1, -1, -1, -1],
#     [-1, 35, -1, -1, 13, -1],
#     [-1, -1, -1, -1, -1, -1],
#     [-1, 15, -1, -1, -1, -1]]
# 输出：4
# 解释：
# 首先，从方格 1 [第 5 行，第 0 列] 开始。
# 你决定移动到方格 2，并必须爬过梯子移动到到方格 15。
# 然后你决定移动到方格 17 [第 3 行，第 5 列]，必须爬过蛇到方格 13。
# 然后你决定移动到方格 14，且必须通过梯子移动到方格 35。
# 然后你决定移动到方格 36, 游戏结束。
# 可以证明你需要至少 4 次移动才能到达第 N*N 个方格，所以答案是 4。

# 示例2：
# 输入：[[-1,-1],[-1,3]]
# 输出：1

# 提示：
# 2 <= board.length = board[0].length <= 20
# board[i][j] 介于 1 和 N*N 之间或者等于 - 1。
# 编号为 1 的方格上没有蛇或梯子。
# 编号为 1 和 N*N 的方格上没有蛇或梯子。

from typing import List
from collections import deque
# @lc code=start


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        # 行或列元素
        n = len(board)
        # 方便计算，先将二维list转成一维
        board_new = []
        for i in range(n - 1, -1, -1):
            if (n - 1 - i) % 2 == 0:
                board_new.extend(board[i])
            if (n - 1 - i) % 2 == 1:
                board_new.extend(board[i][::-1])
        # bfs
        # 辅助队列
        q = deque([(0, 0)])
        # visited用来判断是否被访问
        visited = set([0])
        while q:
            index, depth = q.popleft()
            if index == n*n - 1:
                return depth
            # 避免超出数组范围
            next = min(index + 7, n*n)
            for i in range(index + 1, next):
                # 有跳跃，将跳跃后的点入队
                if board_new[i] != -1:
                    new_i = board_new[i] - 1
                # 无跳跃
                else:
                    new_i = i
                # 再次被访问，无需将该点入队
                if new_i not in visited:
                    q.append((new_i, depth + 1))
                    visited.add(new_i)
        return -1

        # @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.snakesAndLadders([
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, 35, -1, -1, 13, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, 15, -1, -1, -1, -1]])) # 4
    print(solution.snakesAndLadders([[-1,-1],[-1,3]])) # 1
    