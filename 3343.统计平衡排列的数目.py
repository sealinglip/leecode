#
# @lc app=leetcode.cn id=3343 lang=python3
#
# [3343] 统计平衡排列的数目
#
# https://leetcode.cn/problems/count-number-of-balanced-permutations/description/
#
# algorithms
# Hard (30.86%)
# Likes:    20
# Dislikes: 0
# Total Accepted:    5.2K
# Total Submissions: 10.6K
# Testcase Example:  '"123"'
#
# 给你一个字符串 num 。如果一个数字字符串的奇数位下标的数字之和与偶数位下标的数字之和相等，那么我们称这个数字字符串是 平衡的 。
# 
# 请你返回 num 不同排列 中，平衡 字符串的数目。
# 
# 由于答案可能很大，请你将答案对 10^9 + 7 取余 后返回。
# 一个字符串的 排列 指的是将字符串中的字符打乱顺序后连接得到的字符串。
# 
# 
# 示例 1：
# 输入：num = "123"
# 输出：2
# 解释：
# num 的不同排列包括： "123" ，"132" ，"213" ，"231" ，"312" 和 "321" 。
# 它们之中，"132" 和 "231" 是平衡的。所以答案为 2 。
# 
# 示例 2：
# 输入：num = "112"
# 输出：1
# 解释：
# num 的不同排列包括："112" ，"121" 和 "211" 。
# 只有 "121" 是平衡的。所以答案为 1 。
# 
# 
# 示例 3：
# 输入：num = "12345"
# 输出：0
# 解释：
# num 的所有排列都是不平衡的。所以答案为 0 。
# 
# 
# 提示：
# 2 <= num.length <= 80
# num 中的字符只包含数字 '0' 到 '9' 。
# 

# 复习
# @lc code=start
from math import comb


class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        MOD = 10 ** 9 + 7
        n = len(num)
        cnt = [0] * 10
        total = 0
        for c in num:
            d = int(c)
            cnt[d] += 1
            total += d
        if total & 1: # 不是偶数没法满足要求
            return 0
        

        # 动态规划
        target = total >> 1
        maxOdd = (n + 1) >> 1
        f = [[0] * (maxOdd + 1) for _ in range(target + 1)]
        f[0][0] = 1
        preSum = totalSum = 0
        for i in range(10):
            # 前 i 个数字的数目之和
            preSum += cnt[i]
            # 前 i 个数字的元素之和
            totalSum += i * cnt[i]
            for oddCnt in range(min(preSum, maxOdd), max(0, preSum - (n - maxOdd)) - 1, -1):
                # 偶数位需要填充的位数
                evenCnt = preSum - oddCnt
                for curr in range(min(totalSum, target), max(0, totalSum - target) - 1, -1):
                    res = 0
                    for j in range(max(0, cnt[i] - evenCnt), min(cnt[i], oddCnt) + 1):
                        if i * j > curr:
                            break
                        # 当前数字在奇数位填充 j 位，偶数位填充 cnt[i] - j 位
                        ways = comb(oddCnt, j) * comb(evenCnt, cnt[i] - j) % MOD
                        res = (res + ways * f[curr - i * j][oddCnt - j] % MOD) % MOD
                    f[curr][oddCnt] = res % MOD

        return f[target][maxOdd]

        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.countBalancedPermutations("123")) # 2
    print(solution.countBalancedPermutations("112")) # 1
    print(solution.countBalancedPermutations("12345")) # 0
