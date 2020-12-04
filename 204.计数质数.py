#
# @lc app=leetcode.cn id=204 lang=python3
#
# [204] 计数质数
#
# 统计所有小于非负整数 n 的质数的数量。

# 示例 1：
# 输入：n = 10
# 输出：4
# 解释：小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。

# 示例 2：
# 输入：n = 0
# 输出：0

# 示例 3：
# 输入：n = 1
# 输出：0
 
# 提示：
# 0 <= n <= 5 * 10^6

# @lc code=start
from math import sqrt
class Solution:
    def countPrimes(self, n: int) -> int:
        primes = []

        def _isPrime(num: int) -> bool:
            if num < 2:
                return False
            elif num < 4:
                primes.append(num)
                return True
            else:
                limit = int(sqrt(num))
                for i in primes:
                    if i > limit:
                        break
                    if num % i == 0:
                        return False
                primes.append(num)
                return True
        
        if n < 2:
            return 0

        cnt = 0
        for i in range(n):
            if _isPrime(i):
                cnt += 1
        return cnt
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.countPrimes(10))
    print(solution.countPrimes(1500000))