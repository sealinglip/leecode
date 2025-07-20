#
# @lc app=leetcode.cn id=3405 lang=python3
#
# [3405] 统计恰好有 K 个相等相邻元素的数组数目
#
# https://leetcode.cn/problems/count-the-number-of-arrays-with-k-matching-adjacent-elements/description/
#
# algorithms
# Hard (44.98%)
# Likes:    9
# Dislikes: 0
# Total Accepted:    2.9K
# Total Submissions: 5K
# Testcase Example:  '3\n2\n1'
#
# 给你三个整数 n ，m ，k 。长度为 n 的 好数组 arr 定义如下：
# 
# arr 中每个元素都在 闭 区间 [1, m] 中。
# 恰好 有 k 个下标 i （其中 1 <= i < n）满足 arr[i - 1] == arr[i] 。
# 请你返回可以构造出的 好数组 数目。
# 由于答案可能会很大，请你将它对 10^9 + 7 取余 后返回。
# 
# 
# 示例 1：
# 输入：n = 3, m = 2, k = 1
# 输出：4
# 解释：
# 总共有 4 个好数组，分别是 [1, 1, 2] ，[1, 2, 2] ，[2, 1, 1] 和 [2, 2, 1] 。
# 所以答案为 4 。
# 
# 示例 2：
# 输入：n = 4, m = 2, k = 2
# 输出：6
# 解释：
# 好数组包括 [1, 1, 1, 2] ，[1, 1, 2, 2] ，[1, 2, 2, 2] ，[2, 1, 1, 1] ，[2, 2, 1, 1] 和
# [2, 2, 2, 1] 。
# 所以答案为 6 。
# 
# 示例 3：
# 输入：n = 5, m = 2, k = 0
# 输出：2
# 解释：
# 好数组包括 [1, 2, 1, 2, 1] 和 [2, 1, 2, 1, 2] 。
# 所以答案为 2 。
# 
# 
# 提示：
# 1 <= n <= 10^5
# 1 <= m <= 10^5
# 0 <= k <= n - 1
# 
#

# @lc code=start
MOD = 10 ** 9 + 7
MX = 10 ** 5

fact = [0] * MX
inv_fact = [0] * MX

def qpow(x: int, n: int) -> int:
    res = 1
    while n:
        if n & 1:
            res = res * x % MOD
        x = x * x % MOD
        n >>= 1
    return res

def init():
    if fact[0] != 0:
        return
    fact[0] = 1
    for i in range(1, MX):
        fact[i] = fact[i-1] * i % MOD
    inv_fact[MX-1] = qpow(fact[MX-1], MOD - 2)
    for i in range(MX-1, 0, -1):
        inv_fact[i-1] = inv_fact[i] * i % MOD

def comb(n: int, m: int) -> int:
    return fact[n] * inv_fact[m] % MOD * inv_fact[n-m] % MOD

class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        init()
        return comb(n-1, k) * m % MOD * qpow(m-1, n-k-1) % MOD
        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.countGoodArrays(15901, 53255, 3236)) # 525775631
    print(solution.countGoodArrays(64795, 5400, 54877)) # 453992041
    print(solution.countGoodArrays(3, 2, 1)) # 4
    print(solution.countGoodArrays(4, 2, 2)) # 6
    print(solution.countGoodArrays(5, 2, 0)) # 2
