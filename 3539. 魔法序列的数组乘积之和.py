# 3539. 魔法序列的数组乘积之和

# 给你两个整数 M 和 K，和一个整数数组 nums。

# 一个整数序列 seq 如果满足以下条件，被称为 魔法 序列：
# seq 的序列长度为 M。
# 0 <= seq[i] < nums.length
# 2^seq[0] + 2^seq[1] + ... + 2^seq[M - 1] 的 二进制形式 有 K 个 置位。
# 这个序列的 数组乘积 定义为 prod(seq) = (nums[seq[0]] * nums[seq[1]] * ... * nums[seq[M - 1]])。

# 返回所有有效 魔法 序列的 数组乘积 的 总和 。
# 由于答案可能很大，返回结果对 10^9 + 7 取模。
# 置位 是指一个数字的二进制表示中值为 1 的位。


# 示例 1:
# 输入: M = 5, K = 5, nums = [1,10,100,10000,1000000]
# 输出: 991600007
# 解释:
# 所有 [0, 1, 2, 3, 4] 的排列都是魔法序列，每个序列的数组乘积是 1013。

# 示例 2:
# 输入: M = 2, K = 2, nums = [5,4,3,2,1]
# 输出: 170
# 解释:
# 魔法序列有 [0, 1]，[0, 2]，[0, 3]，[0, 4]，[1, 0]，[1, 2]，[1, 3]，[1, 4]，[2, 0]，[2, 1]，[2, 3]，[2, 4]，[3, 0]，[3, 1]，[3, 2]，[3, 4]，[4, 0]，[4, 1]，[4, 2] 和 [4, 3]。

# 示例 3:
# 输入: M = 1, K = 1, nums = [28]
# 输出: 28
# 解释:
# 唯一的魔法序列是 [0]。


# 提示:
# 1 <= K <= M <= 30
# 1 <= nums.length <= 50
# 1 <= nums[i] <= 108

# Hard

from typing import List

class Solution:
    def magicalSum(self, m: int, k: int, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7

        # 快速幂
        def quickPow(x: int, y: int) -> int:
            res, mul = 1, x % MOD
            while y > 0:
                if y & 1:
                    res = res * mul % MOD
                mul = mul * mul % MOD
                y >>= 1
            return res
        
        n = len(nums)
        fac = [1] * (m+1)
        for i in range(1, m+1):
            fac[i] = fac[i-1] * i % MOD

        ifac = [1] * (m+1)
        for i in range(2, m+1):
            ifac[i] = quickPow(i, MOD-2)
        for i in range(2, m+1):
            ifac[i] = ifac[i-1] * ifac[i] % MOD

        numsPower = [[1] * (m + 1) for _ in range(n)]
        for i in range(n):
            for j in range(1, m + 1):
                numsPower[i][j] = numsPower[i][j - 1] * nums[i] % MOD

        f = [[[[0] * (k + 1) for _ in range(m * 2 + 1)] 
              for _ in range(m + 1)] for _ in range(n)]
        
        for j in range(m + 1):
            f[0][j][j][0] = numsPower[0][j] * ifac[j] % MOD
            
        for i in range(n - 1):
            for j in range(m + 1):
                for p in range(m * 2 + 1):
                    for q in range(k + 1):
                        if f[i][j][p][q] == 0:
                            continue
                        q2 = (p % 2) + q
                        if q2 > k:
                            break
                        for r in range(m - j + 1):
                            p2 = (p // 2) + r
                            if p2 > m * 2:
                                continue
                            f[i + 1][j + r][p2][q2] = (
                                f[i + 1][j + r][p2][q2] + 
                                f[i][j][p][q] * numsPower[i + 1][r] % MOD * ifac[r] % MOD
                            ) % MOD
        
        res = 0
        for p in range(m * 2 + 1):
            for q in range(k + 1):
                if bin(p).count('1') + q == k:
                    res = (res + f[n - 1][m][p][q] * fac[m] % MOD) % MOD
                    
        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.magicalSum(5, 5, [1,10,100,10000,1000000])) # 991600007
    print(solution.magicalSum(2, 2, [5,4,3,2,1])) # 170
    print(solution.magicalSum(1, 1, [28])) # 28
