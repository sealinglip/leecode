#
# @lc app=leetcode.cn id=483 lang=python3
#
# [483] 最小好进制
#
# 对于给定的整数 n, 如果n的k（k >= 2）进制数的所有数位全为1，则称 k（k >= 2）是 n 的一个好进制。
# 以字符串的形式给出 n, 以字符串的形式返回 n 的最小好进制。

# 示例 1：
# 输入："13"
# 输出："3"
# 解释：13 的 3 进制是 111。

# 示例 2：
# 输入："4681"
# 输出："8"
# 解释：4681 的 8 进制是 11111。

# 示例 3：
# 输入："1000000000000000000"
# 输出："999999999999999999"
# 解释：1000000000000000000 的 999999999999999999 进制是 11。

# 提示：
# n的取值范围是[3, 10 ^ 18]。
# 输入总是有效且没有前导 0。

# Hard

# @lc code=start
import math


class Solution:
    def smallestGoodBase(self, n: str) -> str:
        nVal = int(n)
        mMax = int(math.floor(math.log2(nVal)))

        for i in range(mMax, 1, -1):
            k = int(math.pow(nVal, 1.0 / i))
            mul, sum = 1, 1
            for _ in range(i):
                mul *= k
                sum += mul
            if sum == nVal:
                return str(k)
        return str(nVal - 1)

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.smallestGoodBase("13"))
    print(solution.smallestGoodBase("4681"))
    print(solution.smallestGoodBase("1000000000000000000"))
