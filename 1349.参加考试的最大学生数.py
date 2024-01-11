#
# @lc app=leetcode.cn id=1349 lang=python3
#
# [1349] 参加考试的最大学生数
#
# 给你一个 m * n 的矩阵 seats 表示教室中的座位分布。如果座位是坏的（不可用），就用 '#' 表示；否则，用 '.' 表示。

# 学生可以看到左侧、右侧、左上、右上这四个方向上紧邻他的学生的答卷，但是看不到直接坐在他前面或者后面的学生的答卷。请你计算并返回该考场可以容纳的同时参加考试且无法作弊的 最大 学生人数。

# 学生必须坐在状况良好的座位上。


# 示例 1：
# 输入：seats = [["#",".","#","#",".","#"],
#               [".","#","#","#","#","."],
#               ["#",".","#","#",".","#"]]
# 输出：4
# 解释：教师可以让 4 个学生坐在可用的座位上，这样他们就无法在考试中作弊。 

# 示例 2：
# 输入：seats = [[".","#"],
#               ["#","#"],
#               ["#","."],
#               ["#","#"],
#               [".","#"]]
# 输出：3
# 解释：让所有学生坐在可用的座位上。

# 示例 3：
# 输入：seats = [["#",".",".",".","#"],
#               [".","#",".","#","."],
#               [".",".","#",".","."],
#               [".","#",".","#","."],
#               ["#",".",".",".","#"]]
# 输出：10
# 解释：让学生坐在第 1、3 和 5 列的可用座位上。
 

# 提示：
# seats 只包含字符 '.' 和'#'
# m == seats.length
# n == seats[i].length
# 1 <= m <= 8
# 1 <= n <= 8

# Hard

from functools import cache
from typing import List
# @lc code=start
class SeatChartIt:
    def __init__(self, row: List[str]):
        self.row = row
        self.idx = 0
        self.limit = 2 ** row.count(".")
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.idx < self.limit:
            val = self.idx
            self.idx += 1
            return self.merge(val)
        else:
            raise StopIteration()
        
    def merge(self, val: int) -> int:
        mask = 0
        b = 1
        for i, s in enumerate(self.row):
            if s == ".": # 可坐人的
                if b & val:
                    mask |= (1 << i)
                b <<= 1

        return mask

class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        def legalRow(seatChart: int) -> bool:
            '''
            判断座次是否合规（不能有两人挨在一起）
            '''
            prev = 0
            for i in range(1, n):
                if (seatChart & (1 << i)) and (seatChart & (1 << (i-1))):
                    return False
            return True
        
        def compatibleWithPrevRow(seatChart: int, prevSeatChat: int) -> bool:
            for i in range(n):
                if seatChart & (1 << i):
                    if i > 0 and (prevSeatChat & (1 << (i-1))):
                        return False
                    if i < n - 1 and (prevSeatChat & (1 << (i + 1))):
                        return False

            return True
                    

        # 每排能坐的学生只依赖于前一排的座位安排
        @cache
        def dp(row: int, seatChart: int) -> int:
            '''
            第row行，座位安排如seatChart，返回前row行总共能坐的学生数——如果seatChart不合规，则返回-inf
            '''
            students = bin(seatChart).count('1')
            if row == 0:
                return students
            ma = 0
            for prevSeatChat in SeatChartIt(seats[row-1]):
                if legalRow(prevSeatChat) and compatibleWithPrevRow(seatChart, prevSeatChat):
                    ma = max(ma, dp(row - 1, prevSeatChat))
            return ma + students

        m, n = len(seats), len(seats[0])
        return dp(m, 0) 

        
# @lc code=end

if __name__ == "__main__":
    # for i in SeatChartIt([".","#","#","."]):
    #     print(bin(i))

    solution = Solution()
    print(solution.maxStudents([[".","#","#","."],[".",".",".","#"],[".",".",".","."],["#",".","#","#"]])) # 5
    # print(solution.maxStudents([["#",".","#","#",".","#"],
    #           [".","#","#","#","#","."],
    #           ["#",".","#","#",".","#"]])) # 4
    # print(solution.maxStudents([[".","#"],
    #           ["#","#"],
    #           ["#","."],
    #           ["#","#"],
    #           [".","#"]])) # 3
    # print(solution.maxStudents([["#",".",".",".","#"],
    #           [".","#",".","#","."],
    #           [".",".","#",".","."],
    #           [".","#",".","#","."],
    #           ["#",".",".",".","#"]])) # 10