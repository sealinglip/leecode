#
# @lc app=leetcode.cn id=633 lang=python3
#
# [633] 平方数之和
#
# 给定一个非负整数 c ，你要判断是否存在两个整数 a 和 b，使得 a^2 + b^2 = c 。

# 示例 1：
# 输入：c = 5
# 输出：true
# 解释：1 * 1 + 2 * 2 = 5

# 示例 2：
# 输入：c = 3
# 输出：false

# 示例 3：
# 输入：c = 4
# 输出：true

# 示例 4：
# 输入：c = 2
# 输出：true

# 示例 5：
# 输入：c = 1
# 输出：true

# 提示：
# 0 <= c <= 2^31 - 1

# @lc code=start

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        # 定理：某个正整数是两平方数之和，当且仅当该正整数的所有 4k+3 型素因数的幂次均为偶数。
        # 任何一个正整数都可以因数分解为 c = (2 ^ r)*(p1 ^ n1)*(p2 ^ n2)*...*(pk ^ nk)，其中p1...pk为素因数，n1...nk为因数的幂次。
        # 也就是说有一个形如4k+3的素因数pi，如果ni为奇数，那它就不可能被写为两个整数的平方数之和了。

        # 去除所有的2
        if c <= 2:
            return True
        while (c & 1) == 0:
            c = c >> 1

        p = 3
        while p * p <= c:
            index = 0
            while c % p == 0:
                index += 1
                c = c // p
            if (p % 4 == 3) and (index % 2 == 1):
                return False
            p += 2
        return c % 4 == 1


        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.judgeSquareSum(5))
    print(solution.judgeSquareSum(4))
    print(solution.judgeSquareSum(3))
    print(solution.judgeSquareSum(2))
    print(solution.judgeSquareSum(1))
