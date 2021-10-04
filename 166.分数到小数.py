#
# @lc app=leetcode.cn id=166 lang=python3
#
# [166] 分数到小数
#
# 给定两个整数，分别表示分数的分子 numerator 和分母 denominator，以 字符串形式返回小数 。
# 如果小数部分为循环小数，则将循环的部分括在括号内。
# 如果存在多个答案，只需返回 任意一个 。

# 对于所有给定的输入，保证 答案字符串的长度小于 104 。


# 示例 1：
# 输入：numerator = 1, denominator = 2
# 输出："0.5"

# 示例 2：
# 输入：numerator = 2, denominator = 1
# 输出："2"

# 示例 3：
# 输入：numerator = 2, denominator = 3
# 输出："0.(6)"

# 示例 4：
# 输入：numerator = 4, denominator = 333
# 输出："0.(012)"

# 示例 5：
# 输入：numerator = 1, denominator = 5
# 输出："0.2"


# 提示：
# -2^31 <= numerator, denominator <= 2^31 - 1
# denominator != 0


# @lc code=start
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if (numerator % denominator) == 0:
            return str(numerator // denominator)

        res = ""
        if (numerator < 0) ^ (denominator < 0):
            res += "-"

        numerator = abs(numerator)
        denominator = abs(denominator)

        # 整数部分
        intPart = numerator // denominator
        res += str(intPart) + "."

        # 小数部分
        remainder = numerator % denominator
        remainderDict = {}
        index = 0
        fractionPart = ""
        while remainder and remainder not in remainderDict:
            remainderDict[remainder] = index
            remainder *= 10
            fractionPart += str(remainder // denominator)
            remainder %= denominator
            index += 1

        if remainder:
            # 有循环节
            index = remainderDict[remainder]
            res += fractionPart[:index] + "(" + fractionPart[index:] + ")"
        else:
            res += fractionPart

        return res
# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    print(solution.fractionToDecimal(1, 2))  # 0.5
    print(solution.fractionToDecimal(2, 1))  # 2
    print(solution.fractionToDecimal(2, 3))  # 0.(6)
    print(solution.fractionToDecimal(4, 333))  # 0.(012)
    print(solution.fractionToDecimal(1, 5))  # 0.2
