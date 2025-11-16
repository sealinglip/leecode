#
# @lc app=leetcode.cn id=1611 lang=python3
#
# [1611] 使整数变为 0 的最少操作次数
#
# https://leetcode.cn/problems/minimum-one-bit-operations-to-make-integers-zero/description/
#
# algorithms
# Hard (60.70%)
# Likes:    84
# Dislikes: 0
# Total Accepted:    7.5K
# Total Submissions: 10.9K
# Testcase Example:  '3'
#
# 给你一个整数 n，你需要重复执行多次下述操作将其转换为 0 ：
# 
# 翻转 n 的二进制表示中最右侧位（第 0 位）。
# 如果第 (i-1) 位为 1 且从第 (i-2) 位到第 0 位都为 0，则翻转 n 的二进制表示中的第 i 位。
# 
# 返回将 n 转换为 0 的最小操作次数。
# 
# 
# 示例 1：
# 输入：n = 3
# 输出：2
# 解释：3 的二进制表示为 "11"
# "11" -> "01" ，执行的是第 2 种操作，因为第 0 位为 1 。
# "01" -> "00" ，执行的是第 1 种操作。
# 
# 示例 2：
# 输入：n = 6
# 输出：4
# 解释：6 的二进制表示为 "110".
# "110" -> "010" ，执行的是第 2 种操作，因为第 1 位为 1 ，第 0 到 0 位为 0 。
# "010" -> "011" ，执行的是第 1 种操作。
# "011" -> "001" ，执行的是第 2 种操作，因为第 0 位为 1 。
# "001" -> "000" ，执行的是第 1 种操作。
# 
# 
# 提示：
# 0 <= n <= 10^9
# 
# 复习
#

# @lc code=start
class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        # 因为根据翻转规则，能动的位要么是最低的位，要么是该位的低一位是1，其他低位全是0
        # 那么考虑 2^k 找下规律
        # 2^0: "1" → "0"，1次
        # 2^1: "10" → "11" → "01" → "00"，共3次
        # 2^2: "100" → "101" → "111" → "110" → "010" → "011" → "001" → "000"，7次
        # 2^3: "1000" → "1001" → "1011" → "1010" → "1110" → "1111" → "1101" → "1100" → "0100" → "0101" → "0111" → "0110" → "0010" → "0011" → "0001" → "0000"，15次
        # 大致规律，要消掉2^k，需要翻转2^(k+1)-1次，方法是先要造出2^(k-1)，才能消掉2^k，造2^(k-1)需要2^(k-2)-1次，消2^k要1次，再消掉剩余的2^(k-1)需要2^(k-2)-1次
        # 数学归纳法易证。
        # 对于任意的一个数而言，转成二进制之后，从高位看向低位，每个置位都有自己对应的翻转次数，贡献到最终结果中是正向还是负向，这个是交替的，最高位是正，从高到低，所有的置位的贡献依次是负正负正……
        l = n.bit_length()
        res = 0
        flag = True
        for i in range(l-1, -1, -1):
            if (1 << i) & n:
                res += (1 if flag else -1) * ((1 << (i+1)) - 1)
                flag = not flag
        return res

        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.minimumOneBitOperations(3)) # 2
    print(solution.minimumOneBitOperations(6)) # 4
    print(solution.minimumOneBitOperations(15)) # 10
