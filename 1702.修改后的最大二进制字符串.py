#
# @lc app=leetcode.cn id=1702 lang=python3
#
# [1702] 修改后的最大二进制字符串
#
# 给你一个二进制字符串 binary ，它仅有 0 或者 1 组成。你可以使用下面的操作任意次对它进行修改：

# 操作 1 ：如果二进制串包含子字符串 "00" ，你可以用 "10" 将其替换。
# 比方说， "00010" -> "10010"
# 操作 2 ：如果二进制串包含子字符串 "10" ，你可以用 "01" 将其替换。
# 比方说， "00010" -> "00001"
# 请你返回执行上述操作任意次以后能得到的 最大二进制字符串 。如果二进制字符串 x 对应的十进制数字大于二进制字符串 y 对应的十进制数字，那么我们称二进制字符串 x 大于二进制字符串 y 。


# 示例 1：
# 输入：binary = "000110"
# 输出："111011"
# 解释：一个可行的转换为：
# "000110" -> "000101" 
# "000101" -> "100101" 
# "100101" -> "110101" 
# "110101" -> "110011" 
# "110011" -> "111011"

# 示例 2：
# 输入：binary = "01"
# 输出："01"
# 解释："01" 没办法进行任何转换。
 

# 提示：
# 1 <= binary.length <= 10^5
# binary 仅包含 '0' 和 '1' 。

# 复习

# @lc code=start
from bisect import bisect_left


class Solution:
    def maximumBinaryString(self, binary: str) -> str:
        # '10' 能换成 '01' 说明1右边的0总能交换到1左边
        # '00' 能换成 '10' 说明最终结果不会有两个连续的0，如果有，那换成10答案更大，与之前已经是最终结果矛盾
        # 综上，最后这个二进制串中最多只有一个0，就看它能在哪
        # 一连串的0，最终都能变成只剩最后一个0
        # 所以要得到最大二进制串，就是首先前缀1全切除，
        # 剩余部分把所有0，像冒泡一样排到最左边，然后除最后一个0外，其他全改成1，再拼上前缀1
        firstZero = binary.find('0')
        if firstZero < 0:
            # 没有0直接返回
            return binary
        
        # prefix = binary[:firstZero]
        # c = sorted(binary[firstZero:])
        # # 找第一个1的位置
        # firstOne = bisect_left(c, '1')
        # if firstOne > 1:
        #     c[:firstOne-1] = ['1'] * (firstOne - 1) 

        # return prefix + ''.join(c)

        # 改进版
        zeroCount = binary.count('0')
        return '1' * (firstZero + zeroCount - 1) + '0' + '1' * (len(binary) - firstZero - zeroCount)

# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.maximumBinaryString("1111")) # "1111"
    print(solution.maximumBinaryString("1100")) # "1110"
    print(solution.maximumBinaryString("000110")) # "111011"
    print(solution.maximumBinaryString("01")) # "01"
    print(solution.maximumBinaryString("0")) # "0"