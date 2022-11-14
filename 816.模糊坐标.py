#
# @lc app=leetcode.cn id=816 lang=python3
#
# [816] 模糊坐标
#
# 我们有一些二维坐标，如 "(1, 3)" 或 "(2, 0.5)"，然后我们移除所有逗号，小数点和空格，得到一个字符串S。返回所有可能的原始字符串到一个列表中。

# 原始的坐标表示法不会存在多余的零，所以不会出现类似于"00", "0.0", "0.00", "1.0", "001", "00.01"或一些其他更小的数来表示坐标。此外，一个小数点前至少存在一个数，所以也不会出现“.1”形式的数字。

# 最后返回的列表可以是任意顺序的。而且注意返回的两个数字中间（逗号之后）都有一个空格。


# 示例 1:
# 输入: "(123)"
# 输出: ["(1, 23)", "(12, 3)", "(1.2, 3)", "(1, 2.3)"]

# 示例 2:
# 输入: "(00011)"
# 输出:  ["(0.001, 1)", "(0, 0.011)"]
# 解释:
# 0.0, 00, 0001 或 00.01 是不被允许的。

# 示例 3:
# 输入: "(0123)"
# 输出: ["(0, 123)", "(0, 12.3)", "(0, 1.23)",
#      "(0.1, 23)", "(0.1, 2.3)", "(0.12, 3)"]
# 示例 4:
# 输入: "(100)"
# 输出: [(10, 0)]
# 解释:
# 1.0 是不被允许的。


# 提示:
# 4 <= S.length <= 12.
# S[0] = "(", S[S.length - 1] = ")", 且字符串 S 中的其他元素都是数字。


from itertools import product
from typing import List
# @lc code=start


class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        def getPossible(coord: str) -> List[str]:
            '''
            获取可能的坐标值
            '''
            ca = []
            if coord[0] != '0' or coord == '0':
                # 整体是合法坐标值
                ca.append(coord)
            for p in range(1, len(coord)):
                if p != 1 and coord[0] == '0' or coord[-1] == '0':
                    # 这种情况不能加小数点
                    continue
                ca.append(coord[:p] + '.' + coord[p:])
            return ca

        s = s[1:len(s) - 1]
        res = []
        for i in range(1, len(s)):
            # 从头到尾遍历，有点担心会TLE
            xs = getPossible(s[:i])
            if len(xs) == 0:
                continue
            ys = getPossible(s[i:])
            if len(ys) == 0:
                continue
            for x, y in product(xs, ys):
                res.append('(' + x + ', ' + y + ')')

        return res

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    # ["(1, 23)", "(12, 3)", "(1.2, 3)", "(1, 2.3)"]
    print(solution.ambiguousCoordinates("(123)"))
    # ["(0.001, 1)", "(0, 0.011)"]
    print(solution.ambiguousCoordinates("(00011)"))
    # ["(0, 123)", "(0, 12.3)", "(0, 1.23)", "(0.1, 23)", "(0.1, 2.3)", "(0.12, 3)"]
    print(solution.ambiguousCoordinates("(0123)"))
    # [(10, 0)]
    print(solution.ambiguousCoordinates("(100)"))
