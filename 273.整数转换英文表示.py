#
# @lc app=leetcode.cn id=273 lang=python3
#
# [273] 整数转换英文表示
#
# 将非负整数 num 转换为其对应的英文表示。

# 示例 1：
# 输入：num = 123
# 输出："One Hundred Twenty Three"

# 示例 2：
# 输入：num = 12345
# 输出："Twelve Thousand Three Hundred Forty Five"

# 示例 3：
# 输入：num = 1234567
# 输出："One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"

# 示例 4：
# 输入：num = 1234567891
# 输出："One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"

# 提示：
# 0 <= num <= 2^31 - 1

# Hard

# @lc code=start
class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        digit = ["", "One", "Two", "Three", "Four",
                 "Five", "Six", "Seven", "Eight", "Nine"]
        teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen",
                 "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tys = ["", "", "Twenty", "Thirty", "Forty",
               "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        grp = ["", "Thousand", "Million", "Billion"]

        numStr = str(num)

        def n2w(part: str) -> str:
            '''
            part长度不超过3
            '''
            L = len(part)
            w = ""
            di = 0
            if L > 2:
                if part[di] != '0':
                    w += digit[int(part[di])] + " Hundred "
                di += 1
            if L > 1:
                if part[di] == '0':
                    if part[di + 1] != '0':
                        w += digit[int(part[di + 1])] + " "
                elif part[di] == '1':
                    w += teens[int(part[di + 1])] + " "
                else:
                    w += tys[int(part[di])] + " " + \
                        (digit[int(part[di + 1])] +
                         " " if part[di + 1] != '0' else "")
            elif part[di] != '0':
                w += digit[int(part[di])] + " "
            return w

        # 每三位为一段
        grpIdx = 0
        N = len(numStr)
        res = ""
        for i in range(N, 0, -3):
            part = numStr[max(i - 3, 0):i]
            partStr = n2w(part)
            if partStr:
                res = partStr + grp[grpIdx] + " " + res
            grpIdx += 1

        return res.strip()

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    # "Fifty Thousand Eight Hundred Sixty Eight"
    # print(solution.numberToWords(50868))
    print(solution.numberToWords(1000000) + "$")  # "One Million"
    print(solution.numberToWords(0) + "$")  # "Zero"
    print(solution.numberToWords(100) + "$")  # "One Hundred"
    print(solution.numberToWords(123) + "$")  # "One Hundred Twenty Three"
    print(solution.numberToWords(1000) + "$")  # "One Thousand"
    print(solution.numberToWords(1001) + "$")  # "One Thousand One"
    # "Twelve Thousand Three Hundred Forty Five"
    print(solution.numberToWords(12345) + "$")
    # "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
    print(solution.numberToWords(1234567) + "$")
    # "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
    print(solution.numberToWords(1234567891) + "$")
