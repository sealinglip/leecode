#
# @lc app=leetcode.cn id=564 lang=python3
#
# [564] 寻找最近的回文数
#
# 给定一个表示整数的字符串 n ，返回与它最近的回文整数（不包括自身）。如果不止一个，返回较小的那个。

# “最近的”定义为两个整数差的绝对值最小。


# 示例 1:
# 输入: n = "123"
# 输出: "121"

# 示例 2:
# 输入: n = "1"
# 输出: "0"
# 解释: 0 和 2是最近的回文，但我们返回最小的，也就是 0。


# 提示:
# 1 <= n.length <= 18
# n 只由数字组成
# n 不含前导 0
# n 代表在[1, 1018 - 1] 范围内的整数

# Hard

# @lc code=start
class Solution:
    def nearestPalindromic(self, n: str) -> str:
        l = len(n)
        orig = int(n)
        halfLen = (l + 1) >> 1
        num = int(n[0:halfLen])

        delta = orig << 1
        res = ""
        for i in range(-1, 2):
            p1 = str(num + i)
            shrink = len(p1) < halfLen  # 是否少了一位
            expand = len(p1) > halfLen  # 多了一位

            if shrink:
                if l & 1:
                    p1 = p1 + p1[::-1]
                else:
                    p1 = p1 + '9' + p1[::-1]
            elif expand:
                offset = (l & 1) + 1
                p1 = p1 + p1[::-1][offset:]
            else:
                offset = l & 1
                p1 = p1 + p1[::-1][offset:]
                if p1 == '00':
                    p1 = '9'
            d = abs(int(p1) - orig)
            if 0 < d < delta or (d == delta and int(p1) < int(res)):  # 不能包含自身，所以d 必须 > 0
                res = p1
                delta = d
        return res


        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.nearestPalindromic("99"))  # "101"
    print(solution.nearestPalindromic("999"))  # "1001"
    print(solution.nearestPalindromic("9999"))  # "10001"
    print(solution.nearestPalindromic("10"))  # "9"
    print(solution.nearestPalindromic("11"))  # "9"
    print(solution.nearestPalindromic("100"))  # "99"
    print(solution.nearestPalindromic("101"))  # "99"
    print(solution.nearestPalindromic("1000"))  # "999"
    print(solution.nearestPalindromic("10000"))  # "9999"

    print(solution.nearestPalindromic("123"))  # "121"
    print(solution.nearestPalindromic("1"))  # "0"
