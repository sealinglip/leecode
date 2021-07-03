#
# @lc app=leetcode.cn id=168 lang=python3
#
# [168] Excel表列名称
#
# 给定一个正整数，返回它在 Excel 表中相对应的列名称。

# 例如，
# 1 -> A
# 2 -> B
# 3 -> C
# ...
# 26 -> Z
# 27 -> AA
# 28 -> AB
# ...

# 示例 1:
# 输入: 1
# 输出: "A"

# 示例 2:
# 输入: 28
# 输出: "AB"

# 示例 3:
# 输入: 701
# 输出: "ZY"

# @lc code=start
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        BASE = 26
        PREA = ord('A') - 1
        arr = []
        while columnNumber:
            remainder = columnNumber % BASE
            if remainder == 0:
                remainder = BASE
            arr.append(chr(PREA + remainder))
            columnNumber -= remainder
            columnNumber //= BASE
        return "".join(arr[::-1])

        # @lc code=end


if __name__ == "__main__":
    solution = Solution()
    print(solution.convertToTitle(26))
    print(solution.convertToTitle(52))
    print(solution.convertToTitle(1))
    print(solution.convertToTitle(28))
    print(solution.convertToTitle(701))
