#
# @lc app=leetcode.cn id=1106 lang=python3
#
# [1106] 解析布尔表达式
#
# 给你一个以字符串形式表述的 布尔表达式（boolean） expression，返回该式的运算结果。

# 有效的表达式需遵循以下约定：

# "t"，运算结果为 True
# "f"，运算结果为 False
# "!(expr)"，运算过程为对内部表达式 expr 进行逻辑 非的运算（NOT）
# "&(expr1,expr2,...)"，运算过程为对 2 个或以上内部表达式 expr1, expr2, ... 进行逻辑 与的运算（AND）
# "|(expr1,expr2,...)"，运算过程为对 2 个或以上内部表达式 expr1, expr2, ... 进行逻辑 或的运算（OR）


# 示例 1：
# 输入：expression = "!(f)"
# 输出：true

# 示例 2：
# 输入：expression = "|(f,t)"
# 输出：true

# 示例 3：
# 输入：expression = "&(t,f)"
# 输出：false

# 示例 4：
# 输入：expression = "|(&(t,f,t),!(t))"
# 输出：false


# 提示：
# 1 <= expression.length <= 20000
# expression[i] 由 {'(', ')', '&', '|', '!', 't', 'f', ','} 中的字符组成。
# expression 是以上述形式给出的有效表达式，表示一个布尔值。

# Hard
# 复习

# @lc code=start
class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = []
        for c in expression:
            if c == ',':
                continue
            if c != ')':
                stack.append(c)
                continue
            # 碰到')'求解当前表达式
            t = f = 0  # 记录True和False的个数
            while stack[-1] != '(':
                if stack.pop() == 't':
                    t += 1
                else:
                    f += 1
            stack.pop()  # '('出栈
            op = stack.pop()
            if op == '!':
                stack.append('t' if f > 0 else 'f')
            elif op == '|':
                stack.append('t' if t > 0 else 'f')
            elif op == '&':
                stack.append('t' if f == 0 else 'f')

        return stack[-1] == 't'

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.parseBoolExpr("!(f)"))  # True
    print(solution.parseBoolExpr("|(f,t)"))  # True
    print(solution.parseBoolExpr("&(t,f)"))  # False
    print(solution.parseBoolExpr("|(&(t,f,t),!(t))"))  # False
