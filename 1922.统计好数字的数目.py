#
# @lc app=leetcode.cn id=1922 lang=python3
#
# [1922] 统计好数字的数目
#
# https://leetcode.cn/problems/count-good-numbers/description/
#
# algorithms
# Medium (38.24%)
# Likes:    39
# Dislikes: 0
# Total Accepted:    11.3K
# Total Submissions: 26.9K
# Testcase Example:  '1'
#
# 我们称一个数字字符串是 好数字 当它满足（下标从 0 开始）偶数 下标处的数字为 偶数 且 奇数 下标处的数字为 质数 （2，3，5 或 7）。
# 
# 
# 比方说，"2582" 是好数字，因为偶数下标处的数字（2 和 8）是偶数且奇数下标处的数字（5 和 2）为质数。但 "3245" 不是 好数字，因为 3
# 在偶数下标处但不是偶数。
# 
# 
# 给你一个整数 n ，请你返回长度为 n 且为好数字的数字字符串 总数 。由于答案可能会很大，请你将它对 10^9 + 7 取余后返回 。
# 
# 一个 数字字符串 是每一位都由 0 到 9 组成的字符串，且可能包含前导 0 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：n = 1
# 输出：5
# 解释：长度为 1 的好数字包括 "0"，"2"，"4"，"6"，"8" 。
# 
# 
# 示例 2：
# 
# 
# 输入：n = 4
# 输出：400
# 
# 
# 示例 3：
# 
# 
# 输入：n = 50
# 输出：564908303
# 
# 
# 
# 
# 提示：
# 1 <= n <= 10^15
# 
# 
#

# @lc code=start
class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        # 4 ^ (n >> 1) * 5 ^ (n - (n >> 1))
        # return 4 ** (n >> 1) * 5 ** (n - (n >> 1)) % MOD # 直接算会TLE
        
        # 快速幂
        def quickPow(x: int, y: int) -> int:
            res, mul = 1, x
            while y > 0:
                if y & 1:
                    res = res * mul % MOD
                mul = mul * mul % MOD
                y >>= 1
            return res
        
        return quickPow(5, (n+1) >> 1) * quickPow(4, n >> 1) % MOD
        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.countGoodNumbers(1)) # 5
    print(solution.countGoodNumbers(4)) # 400
    print(solution.countGoodNumbers(50)) # 564908303
