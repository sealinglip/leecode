#
# @lc app=leetcode.cn id=629 lang=python3
#
# [629] K个逆序对数组
#
# 给出两个整数 n 和 k，找出所有包含从 1 到 n 的数字，且恰好拥有 k 个逆序对的不同的数组的个数。
# 逆序对的定义如下：对于数组的第i个和第 j个元素，如果满i < j且 a[i] > a[j]，则其为一个逆序对；否则不是。
# 由于答案可能很大，只需要返回 答案 mod 10^9 + 7 的值。

# 示例 1:
# 输入: n = 3, k = 0
# 输出: 1
# 解释:
# 只有数组[1, 2, 3] 包含了从1到3的整数并且正好拥有 0 个逆序对。

# 示例 2:
# 输入: n = 3, k = 1
# 输出: 2
# 解释:
# 数组[1, 3, 2] 和[2, 1, 3] 都有 1 个逆序对。

# 说明:
#  n 的范围是[1, 1000] 并且 k 的范围是[0, 1000]。

# Hard

# @lc code=start
class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        MOD = 10 ** 9 + 7
        # 动规
        # 设dp(i, j)为1到i，要组成恰好有j个逆序对，不同排列的个数
        # 则有dp(i, 0) = 1, dp(i, j) = 0 if j < 0
        # 且dp(i, j) = sum([dp(i - 1, j + k - i) for k in range(1, i + 1)]) = sum([dp(i - 1, k) for k in range(max(j - i + 1, 0), j)])
        #           = sum([dp(i - 1, k) for k in range(j)]) - (sum([dp(i - 1, k) for k in range(j - i)]) if j >= i else 0)
        # dp(i, *) 只依赖于dp(i-1, *)，可以降维
        # 有dp(i, *)实际上是dp(i-1, *)前缀和（之差），可以进一步优化计算量
        if k == 0:
            return 1
        # 为了表示dp(*, j) = 0 if j < 0
        # dp数组的长度+1，利用dp[-1]表示👆方程里的dp(*, j) if j < 0
        # 对应i为1的dp(1, j)前缀和 —— 因为实际上只有dp(1, 0) = 1，其他都为0，所以前缀和全是1
        dp = [1] * (k + 2)
        dp[-1] = 0
        for i in range(2, n):
            newDp = [0] * (k + 2)
            newDp[0] = 1
            for j in range(1, k + 1):
                newDp[j] = (newDp[j - 1] + dp[j] - dp[max(j - i, -1)]) % MOD
            dp = newDp
        return (dp[k] - dp[max(k - n, -1)]) % MOD

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.kInversePairs(4, 4))  # 5
    print(solution.kInversePairs(3, 0))  # 1
    print(solution.kInversePairs(3, 1))  # 2
