#
# @lc app=leetcode.cn id=1017 lang=python3
#
# [1017] 负二进制转换
#
# 给你一个整数 n ，以二进制字符串的形式返回该整数的 负二进制（base - 2）表示。

# 注意，除非字符串就是 "0"，否则返回的字符串中不能含有前导零。


# 示例 1：
# 输入：n = 2
# 输出："110"
# 解释：(-2)^2 + (-2)^1 = 2

# 示例 2：
# 输入：n = 3
# 输出："111"
# 解释：(-2)^2 + (-2)^1 + (-2)^0 = 3

# 示例 3：
# 输入：n = 4
# 输出："100"
# 解释：(-2)^2 = 4


# 提示：
# 0 <= n <= 10^9

# 复习

# @lc code=start
class Solution:
    def baseNeg2(self, n: int) -> str:
        b = bin(n)  # 先得到原始二进制
        l = len(b)

        digits = []  # 从低到高
        cf = neg = False  # 进位标志和负标志为False（首位是2^0，不是负数）

        def handleDigit(d: int) -> None:
            nonlocal cf, neg
            # 如果当前位有值，且有进位，那么本位置0，保持进位
            # 如果当前位有值，没有进位，或者当前位无值，且有进位，那么本位置1，进位设置规则为：如果当前是负位，那么进位保留，否则进位清除
            # 如果无值无进位，本位置0，无进位
            if d and cf:
                digits.append('0')
            elif d or cf:
                digits.append('1')
                cf = neg  # 如果当前是负位，那么进位保留，否则进位清除
            else:
                digits.append('0')

        for i in range(l-1, 1, -1):
            d = int(b[i])  # 当前位数值
            handleDigit(d)
            neg = not neg

        while cf:
            handleDigit(0)
            neg = not neg

        if digits[-1] == '0' and len(digits) > 1:  # 去前导零
            digits.pop()

        digits.reverse()
        return "".join(digits)


        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.baseNeg2(0))  # "0"
    print(solution.baseNeg2(6))  # "11010"
    print(solution.baseNeg2(2))  # "110"
    print(solution.baseNeg2(3))  # "111"
    print(solution.baseNeg2(4))  # "100"
