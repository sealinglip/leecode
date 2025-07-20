#
# @lc app=leetcode.cn id=2311 lang=python3
#
# [2311] 小于等于 K 的最长二进制子序列
#
# https://leetcode.cn/problems/longest-binary-subsequence-less-than-or-equal-to-k/description/
#
# algorithms
# Medium (38.06%)
# Likes:    48
# Dislikes: 0
# Total Accepted:    11K
# Total Submissions: 26.2K
# Testcase Example:  '"1001010"\n5'
#
# 给你一个二进制字符串 s 和一个正整数 k 。
# 请你返回 s 的 最长 子序列的长度，且该子序列对应的 二进制 数字小于等于 k 。
# 
# 注意：
# 子序列可以有 前导 0 。
# 空字符串视为 0 。
# 子序列 是指从一个字符串中删除零个或者多个字符后，不改变顺序得到的剩余字符序列。
# 
# 
# 示例 1：
# 输入：s = "1001010", k = 5
# 输出：5
# 解释：s 中小于等于 5 的最长子序列是 "00010" ，对应的十进制数字是 2 。
# 注意 "00100" 和 "00101" 也是可行的最长子序列，十进制分别对应 4 和 5 。
# 最长子序列的长度为 5 ，所以返回 5 。
# 
# 示例 2：
# 输入：s = "00101001", k = 1
# 输出：6
# 解释："000001" 是 s 中小于等于 1 的最长子序列，对应的十进制数字是 1 。
# 最长子序列的长度为 6 ，所以返回 6 。
# 
# 
# 提示：
# 1 <= s.length <= 1000
# s[i] 要么是 '0' ，要么是 '1' 。
# 1 <= k <= 10^9
# 
# 复习

# @lc code=start
class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        res = v = 0
        bits = k.bit_length()
        for i, c in enumerate(s[::-1]):
            if c == '1':
                if i < bits and v + (1 << i) <= k:
                    v += 1 << i
                    res += 1
            else:
                res += 1
        return res
        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.longestSubsequence("1001010", 5)) # 5
    print(solution.longestSubsequence("00101001", 1)) # 6
