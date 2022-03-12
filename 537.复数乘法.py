#
# @lc app=leetcode.cn id=537 lang=python3
#
# [537] 复数乘法
#
# 复数 可以用字符串表示，遵循 "实部+虚部i" 的形式，并满足下述条件：

# 实部 是一个整数，取值范围是[-100, 100]
# 虚部 也是一个整数，取值范围是[-100, 100]
# i^2 == -1
# 给你两个字符串表示的复数 num1 和 num2 ，请你遵循复数表示形式，返回表示它们乘积的字符串。


# 示例 1：
# 输入：num1 = "1+1i", num2 = "1+1i"
# 输出："0+2i"
# 解释：(1 + i) * (1 + i) = 1 + i^2 + 2 * i = 2i ，你需要将它转换为 0+2i 的形式。

# 示例 2：
# 输入：num1 = "1+-1i", num2 = "1+-1i"
# 输出："0+-2i"
# 解释：(1 - i) * (1 - i) = 1 + i^2 - 2 * i = -2i ，你需要将它转换为 0+-2i 的形式。


# 提示：
# num1 和 num2 都是有效的复数表示。

from typing import Tuple
# @lc code=start
import re


class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        def parseComplex(num: str) -> Tuple[int]:
            m = re.match("(-?\d+)\+(-?\d+)i", num)
            if m:
                return (int(m.group(1)), int(m.group(2)))
            else:
                return None

        def formatComplex(comp: Tuple[int]) -> str:
            return str(comp[0]) + "+" + str(comp[1]) + "i"

        comp1 = parseComplex(num1)
        comp2 = parseComplex(num2)
        mul = (comp1[0] * comp2[0] - comp1[1] * comp2[1],
               comp1[1] * comp2[0] + comp1[0] * comp2[1])
        return formatComplex(mul)

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.complexNumberMultiply("1+1i", "1+1i"))  # 0+2i
    print(solution.complexNumberMultiply("1+-1i", "1+-1i"))  # 0+-2i
