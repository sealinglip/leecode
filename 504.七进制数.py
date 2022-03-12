#
# @lc app=leetcode.cn id=504 lang=python3
#
# [504] 七进制数
#
# 给定一个整数 num，将其转化为 7 进制，并以字符串形式输出。

# 示例 1:
# 输入: num = 100
# 输出: "202"

# 示例 2:
# 输入: num = -7
# 输出: "-10"

# 提示：
# -10^7 <= num <= 10^7

# @lc code=start
class Solution:
    def convertToBase7(self, num: int) -> str:
        sign = "-" if num < 0 else ""
        num = abs(num)

        digit = []
        while num >= 7:
            num, d = divmod(num, 7)
            digit.append(d)
        digit.append(num)
        return sign + "".join(map(str, reversed(digit)))


        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.convertToBase7(100))  # "202"
    print(solution.convertToBase7(-7))  # "-10"
