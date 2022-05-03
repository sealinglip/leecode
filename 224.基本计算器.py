#
# @lc app=leetcode.cn id=224 lang=python3
#
# [224] 基本计算器
#
# 实现一个基本的计算器来计算一个简单的字符串表达式 s 的值。

# 示例 1：
# 输入：s = "1 + 1"
# 输出：2

# 示例 2：
# 输入：s = " 2-1 + 2 "
# 输出：3

# 示例 3：
# 输入：s = "(1+(4+5+2)-3)+(6+8)"
# 输出：23

# 提示：
# 1 <= s.length <= 3 * 10^5
# s 由数字、'+'、'-'、'('、')'、和 ' ' 组成
# s 表示一个有效的表达式

# Hard

# @lc code=start


class Solution:
    def calculate(self, s: str) -> int:
        signStack = [1]
        sign = 1
        N = len(s)
        i = 0
        res = 0
        while i < N:
            c = s[i]
            if '0' <= c <= '9':
                mark = i
                while i < N and '0' <= s[i] <= '9':
                    i += 1
                num = int(s[mark:i])
                res += sign * num
            else:
                if c == '(':
                    signStack.append(sign)
                elif c == ')':
                    signStack.pop()
                elif c == '+':
                    sign = signStack[-1]
                elif c == '-':
                    sign = -signStack[-1]
                i += 1

        return res


        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.calculate("1 + 1"))
    print(solution.calculate(" 2-1 + 2 "))
    print(solution.calculate("(1+(4+5+2)-3)+(6+8)"))
    print(solution.calculate("(1+(45+5+2)-3)+(6+8)"))
