#
# @lc app=leetcode.cn id=640 lang=python3
#
# [640] 求解方程
#

# 求解一个给定的方程，将x以字符串 "x=#value" 的形式返回。该方程仅包含 '+' ， '-' 操作，变量 x 和其对应系数。
# 如果方程没有解，请返回 "No solution" 。如果方程有无限解，则返回 “Infinite solutions” 。
# 题目保证，如果方程中只有一个解，则 'x' 的值是一个整数。


# 示例 1：
# 输入: equation = "x+5-3+x=6+x-2"
# 输出: "x=2"

# 示例 2:
# 输入: equation = "x=x"
# 输出: "Infinite solutions"

# 示例 3:
# 输入: equation = "2x=x"
# 输出: "x=0"


# 提示:
# 3 <= equation.length <= 1000
# equation 只有一个 '='.
# equation 方程由整数组成，其绝对值在[0, 100] 范围内，不含前导零和变量 'x' 。

from ast import operator
from typing import Tuple
# @lc code=start


class Solution:
    def solveEquation(self, equation: str) -> str:
        def simplifyEq(eq: str) -> Tuple[int]:
            '''
            化简方程为ax + b的形式，返回(a, b)
            '''
            a = b = 0
            i, n = 0, len(eq)
            while i < n:
                sign = 1
                if eq[i] == '+':
                    i += 1
                elif eq[i] == '-':
                    sign = -1
                    i += 1

                num, valid = 0, False
                while i < n and eq[i].isdigit():
                    valid = True
                    num = num * 10 + int(eq[i])
                    i += 1

                if i < n and eq[i] == 'x':  # 变量
                    a += sign * num if valid else sign
                    i += 1
                else:  # 数值
                    b += sign * num

            return (a, b)

        parts = equation.split('=')
        a, b = simplifyEq(parts[0])
        c, d = simplifyEq(parts[1])
        if a == c:
            if b == d:
                return 'Infinite solutions'
            else:
                return 'No solution'
        else:
            return 'x=' + str((d - b) // (a - c))

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.solveEquation("x+5-3+x=6+x-2"))  # "x=2"
    print(solution.solveEquation("x=x"))  # "Infinite solutions"
    print(solution.solveEquation("2x=x"))  # "x=0"
    print(solution.solveEquation("x+5-3+x=6+2x-2"))  # "x=0"
