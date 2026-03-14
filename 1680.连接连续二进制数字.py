#
# @lc app=leetcode.cn id=1680 lang=python3
#
# [1680] 连接连续二进制数字
#
# https://leetcode.cn/problems/concatenation-of-consecutive-binary-numbers/description/
#
# algorithms
# Medium (52.81%)
# Likes:    61
# Dislikes: 0
# Total Accepted:    12.1K
# Total Submissions: 21.6K
# Testcase Example:  '1'
#
# 给你一个整数 n ，请你将 1 到 n 的二进制表示连接起来，并返回连接结果对应的 十进制 数字对 10^9 + 7 取余的结果。
# 
# 
# 示例 1：
# 输入：n = 1
# 输出：1
# 解释：二进制的 "1" 对应着十进制的 1 。
# 
# 示例 2：
# 输入：n = 3
# 输出：27
# 解释：二进制下，1，2 和 3 分别对应 "1" ，"10" 和 "11" 。
# 将它们依次连接，我们得到 "11011" ，对应着十进制的 27 。
# 
# 示例 3：
# 输入：n = 12
# 输出：505379714
# 解释：连接结果为 "1101110010111011110001001101010111100" 。
# 对应的十进制数字为 118505380540 。
# 对 10^9 + 7 取余后，结果为 505379714 。
# 
# 
# 提示：
# 1 <= n <= 10^5
# 
# 
#

# @lc code=start
class Solution:
    def concatenatedBinary(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        res = shift = 0
        for i in range(1, n+1):
            if i & (i-1) == 0:
                shift += 1 # 位数变大
            res = ((res << shift) + i) % MOD
        return res
        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.concatenatedBinary(1)) # 1
    print(solution.concatenatedBinary(3)) # 27
    print(solution.concatenatedBinary(12)) # 505379714