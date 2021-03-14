#
# @lc app=leetcode.cn id=227 lang=python3
#
# [227] 基本计算器 II
#
# 给你一个字符串表达式 s ，请你实现一个基本计算器来计算并返回它的值。
# 整数除法仅保留整数部分。

# 示例 1：
# 输入：s = "3+2*2"
# 输出：7

# 示例 2：
# 输入：s = " 3/2 "
# 输出：1

# 示例 3：
# 输入：s = " 3+5 / 2 "
# 输出：5

# 提示：
# 1 <= s.length <= 3 * 10^5
# s 由整数和算符('+', '-', '*', '/') 组成，中间由一些空格隔开
# s 表示一个 有效表达式
# 表达式中的所有整数都是非负整数，且在范围[0, 2^31 - 1] 内
# 题目数据保证答案是一个 32-bit 整数

# @lc code=start
class Solution:
    def calculate(self, s: str) -> int:
        # 转后缀表达式（逆波兰式）
        N = len(s)
        i = 0
        sign = 1
        stack = []
        tmp = []
        op = True
        while i < N:
            c = s[i]
            if '0' <= c <= '9':
                mark = i
                while i < N and '0' <= s[i] <= '9':
                    i += 1
                num = int(s[mark:i])
                stack.append(sign * num)
                sign = 1
                op = False  # 当前不是操作符
            else:
                if c == '+' or c == '-':
                    if c == '-' and op:  # 上一个也是操作符，说明本-是负号而不是减号
                        sign = -1
                    else:
                        while tmp:
                            stack.append(tmp.pop())
                        tmp.append(c)
                        op = True
                elif c == '/' or c == '*':
                    while tmp and (tmp[-1] == '*' or tmp[-1] == '/'):
                        stack.append(tmp.pop())
                    tmp.append(c)
                    op = True
                i += 1
        while tmp:
            stack.append(tmp.pop())

        # 求解逆波兰式
        solve = []  # 求解栈
        for e in stack:
            if e == '+':
                solve.append(solve.pop() + solve.pop())
            elif e == '-':
                subtractor = solve.pop()
                solve.append(solve.pop() - subtractor)
            elif e == '*':
                solve.append(solve.pop() * solve.pop())
            elif e == '/':
                divisor = solve.pop()
                solve.append(solve.pop() // divisor)
            else:
                solve.append(e)
        return solve.pop()
# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    print(solution.calculate("3+2*2"))
    print(solution.calculate("3-2*2"))
    print(solution.calculate(" 3/2 "))
    print(solution.calculate(" 3+5 / 2 "))
    print(solution.calculate(" -3+5 / 2 "))
