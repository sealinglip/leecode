#
# @lc app=leetcode.cn id=3272 lang=python3
#
# [3272] 统计好整数的数目
#
# https://leetcode.cn/problems/find-the-count-of-good-integers/description/
#
# algorithms
# Hard (52.58%)
# Likes:    21
# Dislikes: 0
# Total Accepted:    4.9K
# Total Submissions: 6.9K
# Testcase Example:  '3\n5'
#
# 给你两个 正 整数 n 和 k 。
# 
# 如果一个整数 x 满足以下条件，那么它被称为 k 回文 整数 。
# 
# 
# x 是一个 回文整数 。
# x 能被 k 整除。
# 
# 
# 如果一个整数的数位重新排列后能得到一个 k 回文整数 ，那么我们称这个整数为 好 整数。比方说，k = 2 ，那么 2020 可以重新排列得到 2002
# ，2002 是一个 k 回文串，所以 2020 是一个好整数。而 1010 无法重新排列数位得到一个 k 回文整数。
# 
# 请你返回 n 个数位的整数中，有多少个 好 整数。
# 
# 注意 ，任何整数在重新排列数位之前或者之后 都不能 有前导 0 。比方说 1010 不能重排列得到 101 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：n = 3, k = 5
# 
# 输出：27
# 
# 解释：
# 
# 部分好整数如下：
# 
# 
# 551 ，因为它可以重排列得到 515 。
# 525 ，因为它已经是一个 k 回文整数。
# 
# 
# 
# 示例 2：
# 
# 
# 输入：n = 1, k = 4
# 
# 输出：2
# 
# 解释：
# 
# 两个好整数分别是 4 和 8 。
# 
# 
# 示例 3：
# 
# 
# 输入：n = 5, k = 6
# 
# 输出：2468
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= n <= 10
# 1 <= k <= 9
# 
# 
#

# @lc code=start
from collections import Counter
from math import factorial


class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        fac = [factorial(i) for i in range(n + 1)]
        ans = 0
        vis = set()
        base = 10 ** ((n - 1) // 2)
        for i in range(base, base * 10):  # 枚举回文数左半边
            s = str(i)
            s += s[::-1][n % 2:]
            if int(s) % k:  # 回文数不能被 k 整除
                continue

            sorted_s = ''.join(sorted(s))
            if sorted_s in vis:  # 不能重复统计
                continue
            vis.add(sorted_s)

            cnt = Counter(sorted_s)
            res = (n - cnt['0']) * fac[n - 1]
            for c in cnt.values():
                res //= fac[c]
            ans += res
        return ans
        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.countGoodIntegers(3, 5)) # 27
    print(solution.countGoodIntegers(1, 4)) # 2
    print(solution.countGoodIntegers(5, 6)) # 2468
