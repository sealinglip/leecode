# 二进制数转字符串。给定一个介于0和1之间的实数（如0.72），类型为double，打印它的二进制表达式。如果该数字无法精确地用32位以内的二进制表示，则打印“ERROR”。

# 示例1:
#  输入：0.625
#  输出："0.101"

# 示例2:
#  输入：0.1
#  输出："ERROR"
#  提示：0.1无法被二进制准确表示


# 提示：
# 32位包括输出中的 "0." 这两位。
# 题目保证输入用例的小数位数最多只有 6 位

class Solution:
    def printBin(self, num: float) -> str:
        res = '0.'
        while len(res) <= 32 and num != 0:
            num *= 2
            d = int(num)
            res += str(d)
            num -= d

        return res if len(res) <= 32 else 'ERROR'


if __name__ == "__main__":
    solution = Solution()
    print(solution.printBin(0.625))  # "0.101"
    print(solution.printBin(0.1))  # "ERROR"
