#
# @lc app=leetcode.cn id=794 lang=python3
#
# [794] 有效的井字游戏
#
# 给你一个字符串数组 board 表示井字游戏的棋盘。当且仅当在井字游戏过程中，棋盘有可能达到 board 所显示的状态时，才返回 true 。

# 井字游戏的棋盘是一个 3 x 3 数组，由字符 ' '，'X' 和 'O' 组成。字符 ' ' 代表一个空位。

# 以下是井字游戏的规则：

# 玩家轮流将字符放入空位（' '）中。
# 玩家 1 总是放字符 'X' ，而玩家 2 总是放字符 'O' 。
# 'X' 和 'O' 只允许放置在空位中，不允许对已放有字符的位置进行填充。
# 当有 3 个相同（且非空）的字符填充任何行、列或对角线时，游戏结束。
# 当所有位置非空时，也算为游戏结束。
# 如果游戏结束，玩家不允许再放置字符。


# 示例 1：
# 输入：board = ["O  ", "   ", "   "]
# 输出：false
# 解释：玩家 1 总是放字符 "X" 。

# 示例 2：
# 输入：board = ["XOX", " X ", "   "]
# 输出：false
# 解释：玩家应该轮流放字符。

# 示例 3：
# 输入：board = ["XXX", "   ", "OOO"]
# 输出：false

# 示例 4:
# 输入：board = ["XOX", "O O", "XOX"]
# 输出：true

# 提示：
# board.length == 3
# board[i].length == 3
# board[i][j] 为 'X'、'O' 或 ' '

from typing import List
# @lc code=start


class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        # 判断条件，
        # 1、count('X') == count('O') [+ 1]
        # 2、如果有胜者，胜者为X，则X数要多1；如果胜者为O，则两数相等，不能有两个胜者
        countX = sum([x.count('X') for x in board])
        countO = sum([x.count('O') for x in board])

        # 条件1判断
        if not (countX == countO or countX == (countO + 1)):
            return False

        # 条件2判断
        def win(p: str) -> bool:
            '''
            判定是否指定字符胜出
            '''
            return any((board[i][0] == p and board[i][1] == p and board[i][2] == p) or
                       (board[0][i] == p and board[1][i] == p and board[2][i] == p) for i in range(3)) or \
                (board[0][0] == p and board[1][1] == p and board[2][2] == p) or \
                (board[0][2] == p and board[1][1] == p and board[2][0] == p)

        if win('X'):
            return (not win('O')) and (countX == (countO + 1))
        elif win('O'):
            return countX == countO

        return True
# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    print(solution.validTicTacToe(["OOO", "XXO", "XXX"]))  # False
    print(solution.validTicTacToe(["O  ", "   ", "   "]))  # False
    print(solution.validTicTacToe(["XOX", " X ", "   "]))  # False
    print(solution.validTicTacToe(["XXX", "   ", "OOO"]))  # False
    print(solution.validTicTacToe(["XOX", "O O", "XOX"]))  # True
