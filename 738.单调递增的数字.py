#
# @lc app=leetcode.cn id=738 lang=python3
#
# [738] 单调递增的数字
#
# 给定一个非负整数 N，找出小于或等于 N 的最大的整数，同时这个整数需要满足其各个位数上的数字是单调递增。

# （当且仅当每个相邻位数上的数字 x 和 y 满足 x <= y 时，我们称这个整数是单调递增的。）

# 示例 1:
# 输入: N = 10
# 输出: 9

# 示例 2:
# 输入: N = 1234
# 输出: 1234

# 示例 3:
# 输入: N = 332
# 输出: 299
# 说明: N 是在 [0, 10^9] 范围内的一个整数。

# @lc code=start
class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        digits = [int(c) for c in str(N)] # 各数位的数
        L = len(digits)
        
        if L == 1:
            # 一位数的情况
            return N
        else:
            preDigit = digits[0]
            for i in range(1, L):
                digit = digits[i]
                if digit < preDigit:
                    while i > 1 and digits[i - 2] == digits[i - 1]:
                        i -= 1
                    digits[i - 1] -= 1
                    for j in range(i, L):
                        digits[j] = 9
                    break
                preDigit = digit
            
            if digits[0] == 0:
                del digits[0]
            return int("".join([str(d) for d in digits]))
        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.monotoneIncreasingDigits(121))
    print(solution.monotoneIncreasingDigits(10))
    print(solution.monotoneIncreasingDigits(1234))
    print(solution.monotoneIncreasingDigits(332))