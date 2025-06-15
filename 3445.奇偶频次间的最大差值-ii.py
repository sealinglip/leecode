#
# @lc app=leetcode.cn id=3445 lang=python3
#
# [3445] 奇偶频次间的最大差值 II
#
# https://leetcode.cn/problems/maximum-difference-between-even-and-odd-frequency-ii/description/
#
# algorithms
# Hard (33.96%)
# Likes:    13
# Dislikes: 0
# Total Accepted:    1.6K
# Total Submissions: 3.6K
# Testcase Example:  '"12233"\n4'
#
# 给你一个字符串 s 和一个整数 k 。请你找出 s 的子字符串 subs 中两个字符的出现频次之间的 最大 差值，freq[a] - freq[b]
# ，其中：
# 
# subs 的长度 至少 为 k 。
# 字符 a 在 subs 中出现奇数次。
# 字符 b 在 subs 中出现偶数次。
# 
# 返回 最大 差值。
# 
# 注意 ，subs 可以包含超过 2 个 互不相同 的字符。.
# 子字符串 是字符串中的一个连续字符序列。
# 
# 
# 示例 1：
# 输入：s = "12233", k = 4
# 输出：-1
# 解释：
# 对于子字符串 "12233" ，'1' 的出现次数是 1 ，'3' 的出现次数是 2 。差值是 1 - 2 = -1 。
# 
# 示例 2：
# 输入：s = "1122211", k = 3
# 输出：1
# 解释：
# 对于子字符串 "11222" ，'2' 的出现次数是 3 ，'1' 的出现次数是 2 。差值是 3 - 2 = 1 。
# 
# 示例 3：
# 输入：s = "110", k = 3
# 输出：-1
# 
# 
# 提示：
# 3 <= s.length <= 3 * 10^4
# s 仅由数字 '0' 到 '4' 组成。
# 输入保证至少存在一个子字符串是由一个出现奇数次的字符和一个出现偶数次的字符组成。
# 1 <= k <= s.length
# 
#

# @lc code=start

from math import inf


CA = "01234" # 可能的字符

class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        def getStatus(cntA: int, cntB: int) -> int:
            '''
            通过四种状态来标记字符a和字符b个数的奇偶性：
            0b00：两者都为偶
            0b01：a偶b奇
            0b10：a奇b偶
            0b11：a奇b奇
            满足条件的子字符串的状态应该为0b10
            如果记录前缀数组的状态，那么两个索引i<j，s[i:j]满足条件的必要条件是state(i) ^ 0b10 = state(j)，同理，state(i) = state(j) ^ 0b10
            '''
            return ((cntA & 1) << 1) | (cntB & 1)
        
        n = len(s)
        res = -inf
        
        
        # 枚举组合
        for a in CA:
            for b in CA:
                if a == b:
                    continue
                minDiff = [inf] * 4 # 记录遍历过程中每种状态的最小差
                cntA = cntB = prevCntA = prevCntB = 0
                l = -1
                for r in range(n):
                    if s[r] == a:
                        cntA += 1
                    elif s[r] == b:
                        cntB += 1
                    while r - l >= k and cntB - prevCntB >= 2:
                        leftStatus = getStatus(prevCntA, prevCntB)
                        minDiff[leftStatus] = min(minDiff[leftStatus], prevCntA - prevCntB)
                        l += 1
                        if s[l] == a:
                            prevCntA += 1
                        elif s[l] == b:
                            prevCntB += 1
                    
                    rightStatus = getStatus(cntA, cntB)
                    diff = cntA - cntB
                    res = max(diff - minDiff[rightStatus ^ 0b10], res)
                
        return res
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.maxDifference("12233", 4)) # -1
    print(solution.maxDifference("1122211", 3)) # 1
    print(solution.maxDifference("110", 3)) # -1
