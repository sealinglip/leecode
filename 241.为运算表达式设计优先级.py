#
# @lc app=leetcode.cn id=241 lang=python3
#
# [241] 为运算表达式设计优先级
#
# 给你一个由数字和运算符组成的字符串 expression ，按不同优先级组合数字和运算符，计算并返回所有可能组合的结果。你可以 按任意顺序 返回答案。

# 生成的测试用例满足其对应输出值符合 32 位整数范围，不同结果的数量不超过 10^4 。


# 示例 1：
# 输入：expression = "2-1-1"
# 输出：[0, 2]
# 解释：
# ((2-1)-1) = 0
# (2-(1-1)) = 2
# 示例 2：
# 输入：expression = "2*3-4*5"
# 输出：[-34, -14, -10, -10, 10]
# 解释：
# (2*(3-(4*5))) = -34
# ((2*3)-(4*5)) = -14
# ((2*(3-4))*5) = -10
# (2*((3-4)*5)) = -10
# (((2*3)-4)*5) = 10


# 提示：
# 1 <= expression.length <= 20
# expression 由数字和算符 '+'、'-' 和 '*' 组成。
# 输入表达式中的所有整数值在范围[0, 99]

# 复习

from typing import List
# @lc code=start


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        def isOp(c: str) -> bool:
            '''
            判断是否为操作符
            '''
            return c == '+' or c == '-' or c == '*'

        def calc(num1: int, op: str, num2: int) -> int:
            if op == '+':
                return num1 + num2
            if op == '-':
                return num1 - num2
            if op == '*':
                return num1 * num2

        # 解析得到操作数和操作符
        nums = []
        ops = []
        num = 0
        for c in expression:
            if isOp(c):
                nums.append(num)
                num = 0
                ops.append(c)
            else:
                num = num * 10 + int(c)
        nums.append(num)

        # dp(i, j)表示nums[i:j+1]之间所有的组合结果
        n = len(nums)
        dp = [[None] * n for i in range(n)]
        for i, num in enumerate(nums):
            dp[i][i] = [num]

        for span in range(2, n+1):
            # span 代表跨度
            for i in range(0, n-span+1):
                # i 代表起点, j代表终点
                j = i + span - 1
                res = []
                for s in range(i, j):
                    # 将表达式切分为nums[i:s+1]和nums[s+1:j+1]两部分
                    res1 = dp[i][s]
                    res2 = dp[s+1][j]
                    op = ops[s]

                    for x in res1:
                        for y in res2:
                            res.append(calc(x, op, y))

                dp[i][j] = res

        return dp[0][n-1]


        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.diffWaysToCompute("2*3-4*5"))  # [-34,-14,-10,-10,10]
    print(solution.diffWaysToCompute("2-1-1"))  # [0,2]
