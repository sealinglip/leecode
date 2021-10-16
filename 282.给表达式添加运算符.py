#
# @lc app=leetcode.cn id=282 lang=python3
#
# [282] 给表达式添加运算符
#
# 给定一个仅包含数字 0-9 的字符串 num 和一个目标值整数 target ，在 num 的数字之间添加 二元 运算符（不是一元）+、- 或 * ，返回所有能够得到目标值的表达式。


# 示例 1:
# 输入: num = "123", target = 6
# 输出: ["1+2+3", "1*2*3"]

# 示例 2:
# 输入: num = "232", target = 8
# 输出: ["2*3+2", "2+3*2"]

# 示例 3:
# 输入: num = "105", target = 5
# 输出: ["1*0+5", "10-5"]

# 示例 4:
# 输入: num = "00", target = 0
# 输出: ["0+0", "0-0", "0*0"]

# 示例 5:
# 输入: num = "3456237490", target = 9191
# 输出: []


# 提示：
# 1 <= num.length <= 10
# num 仅含数字
# -2^31 <= target <= 2^31 - 1

from typing import List
# @lc code=start


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        res = []
        N = len(num)

        def backtrack(exp: str, idx: int, prev: int, mul: int) -> None:
            if idx == N:
                if prev == target:
                    res.append(exp)
                return
            rb = idx + 1 if num[idx] == '0' else N  # 如果当前字符是0，那么数字只能是0，不能是多位数
            for i in range(idx, rb):
                piece = num[idx:i + 1]
                val = int(piece)
                if idx:
                    # try '+'
                    backtrack(exp + "+" + piece, i + 1, prev + val, val)
                    # try '-'
                    backtrack(exp + "-" + piece, i + 1, prev - val, -val)
                    # try '*'
                    backtrack(exp + "*" + piece, i + 1, prev -
                              mul + mul * val, val * mul)
                else:
                    backtrack(piece, i + 1, val, val)

        backtrack("", 0, 0, 0)
        return res


        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.addOperators("123", 6))  # ["1+2+3", "1*2*3"]
    print(solution.addOperators("232", 8))  # ["2*3+2", "2+3*2"]
    print(solution.addOperators("105", 5))  # ["1*0+5","10-5"]
    print(solution.addOperators("00", 0))  # ["0+0", "0-0", "0*0"]
    print(solution.addOperators("3456237490", 9191))  # []
