#
# @lc app=leetcode.cn id=2338 lang=python3
#
# [2338] 统计理想数组的数目
#
# https://leetcode.cn/problems/count-the-number-of-ideal-arrays/description/
#
# algorithms
# Hard (31.65%)
# Likes:    63
# Dislikes: 0
# Total Accepted:    4.6K
# Total Submissions: 12.7K
# Testcase Example:  '2\n5'
#
# 给你两个整数 n 和 maxValue ，用于描述一个 理想数组 。
# 
# 对于下标从 0 开始、长度为 n 的整数数组 arr ，如果满足以下条件，则认为该数组是一个 理想数组 ：
# 
# 
# 每个 arr[i] 都是从 1 到 maxValue 范围内的一个值，其中 0 <= i < n 。
# 每个 arr[i] 都可以被 arr[i - 1] 整除，其中 0 < i < n 。
# 
# 
# 返回长度为 n 的 不同 理想数组的数目。由于答案可能很大，返回对 10^9 + 7 取余的结果。
# 
# 
# 
# 示例 1：
# 输入：n = 2, maxValue = 5
# 输出：10
# 解释：存在以下理想数组：
# - 以 1 开头的数组（5 个）：[1,1]、[1,2]、[1,3]、[1,4]、[1,5]
# - 以 2 开头的数组（2 个）：[2,2]、[2,4]
# - 以 3 开头的数组（1 个）：[3,3]
# - 以 4 开头的数组（1 个）：[4,4]
# - 以 5 开头的数组（1 个）：[5,5]
# 共计 5 + 2 + 1 + 1 + 1 = 10 个不同理想数组。
# 
# 
# 示例 2：
# 输入：n = 5, maxValue = 3
# 输出：11
# 解释：存在以下理想数组：
# - 以 1 开头的数组（9 个）：
# ⁠  - 不含其他不同值（1 个）：[1,1,1,1,1] 
# ⁠  - 含一个不同值 2（4 个）：[1,1,1,1,2], [1,1,1,2,2], [1,1,2,2,2], [1,2,2,2,2]
# ⁠  - 含一个不同值 3（4 个）：[1,1,1,1,3], [1,1,1,3,3], [1,1,3,3,3], [1,3,3,3,3]
# - 以 2 开头的数组（1 个）：[2,2,2,2,2]
# - 以 3 开头的数组（1 个）：[3,3,3,3,3]
# 共计 9 + 1 + 1 = 11 个不同理想数组。
# 
# 
# 提示：
# 2 <= n <= 10^4
# 1 <= maxValue <= 10^4
#

# @lc code=start
MOD = 1_000_000_007
MAX_N = 10_000
MAX_E = 13

# EXP[x] 为 x 分解质因数后，每个质因数的指数
EXP = [[] for _ in range(MAX_N + 1)]
for x in range(2, len(EXP)):
    t = x
    i = 2
    while i * i <= t:
        e = 0
        while t % i == 0:
            e += 1
            t //= i
        if e:
            EXP[x].append(e)
        i += 1
    if t > 1:
        EXP[x].append(1)

# 预处理组合数
C = [[0] * (MAX_E + 1) for _ in range(MAX_N + MAX_E)]
for i in range(len(C)):
    C[i][0] = 1
    for j in range(1, min(i, MAX_E) + 1):
        C[i][j] = (C[i - 1][j] + C[i - 1][j - 1]) % MOD

class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        ans = 0
        for x in range(1, maxValue + 1):
            res = 1
            for e in EXP[x]:
                res = res * C[n + e - 1][e] % MOD
            ans += res
        return ans % MOD
    
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.idealArrays(2, 5)) # 10
    print(solution.idealArrays(5, 3)) # 11
