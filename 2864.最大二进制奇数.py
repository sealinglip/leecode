#
# @lc app=leetcode.cn id=2864 lang=python3
#
# [2864] 最大二进制奇数
#
# 给你一个 二进制 字符串 s ，其中至少包含一个 '1' 。

# 你必须按某种方式 重新排列 字符串中的位，使得到的二进制数字是可以由该组合生成的 最大二进制奇数 。

# 以字符串形式，表示并返回可以由给定组合生成的最大二进制奇数。

# 注意 返回的结果字符串 可以 含前导零。


# 示例 1：
# 输入：s = "010"
# 输出："001"
# 解释：因为字符串 s 中仅有一个 '1' ，其必须出现在最后一位上。所以答案是 "001" 。

# 示例 2：
# 输入：s = "0101"
# 输出："1001"
# 解释：其中一个 '1' 必须出现在最后一位上。而由剩下的数字可以生产的最大数字是 "100" 。所以答案是 "1001" 。
 

# 提示：
# 1 <= s.length <= 100
# s 仅由 '0' 和 '1' 组成
# s 中至少包含一个 '1'

# @lc code=start
from collections import Counter


class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        bitCount = Counter(s)
        return '1' * (bitCount['1'] - 1) + '0' * bitCount['0'] + '1'
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.maximumOddBinaryNumber('010')) # 001
    print(solution.maximumOddBinaryNumber('0101')) # 1001