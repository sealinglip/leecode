#
# @lc app=leetcode.cn id=1930 lang=python3
#
# [1930] 长度为 3 的不同回文子序列
#
# https://leetcode.cn/problems/unique-length-3-palindromic-subsequences/description/
#
# algorithms
# Medium (56.21%)
# Likes:    74
# Dislikes: 0
# Total Accepted:    17.6K
# Total Submissions: 29K
# Testcase Example:  '"aabca"'
#
# 给你一个字符串 s ，返回 s 中 长度为 3 的不同回文子序列 的个数。
# 即便存在多种方法来构建相同的子序列，但相同的子序列只计数一次。
# 回文 是正着读和反着读一样的字符串。
# 子序列 是由原字符串删除其中部分字符（也可以不删除）且不改变剩余字符之间相对顺序形成的一个新字符串。
# 
# 例如，"ace" 是 "abcde" 的一个子序列。
# 
# 
# 示例 1：
# 输入：s = "aabca"
# 输出：3
# 解释：长度为 3 的 3 个回文子序列分别是：
# - "aba" ("aabca" 的子序列)
# - "aaa" ("aabca" 的子序列)
# - "aca" ("aabca" 的子序列)
# 
# 示例 2：
# 输入：s = "adc"
# 输出：0
# 解释："adc" 不存在长度为 3 的回文子序列。
# 
# 示例 3：
# 输入：s = "bbcbaba"
# 输出：4
# 解释：长度为 3 的 4 个回文子序列分别是：
# - "bbb" ("bbcbaba" 的子序列)
# - "bcb" ("bbcbaba" 的子序列)
# - "bab" ("bbcbaba" 的子序列)
# - "aba" ("bbcbaba" 的子序列)
# 
# 
# 提示：
# 3 <= s.length <= 10^5
# s 仅由小写英文字母组成
# 
# 
#

# @lc code=start
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        base = ord('a')
        n = len(s)
        prev = [0] * n
        suffix = [0] * n
        for i in range(n):
            prev[i] = (prev[i-1] if i else 0) | (1 << (ord(s[i]) - base))
        for i in range(n-1, -1, -1):
            suffix[i] = (suffix[i+1] if i < n-1 else 0) | (1 << (ord(s[i]) - base))

        mask = [0] * 26
        for i in range(1, n-1):
            mask[ord(s[i]) - base] |= prev[i-1] & suffix[i+1]
        
        res = 0
        for m in mask:
            res += m.bit_count()
        return res 
        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.countPalindromicSubsequence("aabca")) # 3
    print(solution.countPalindromicSubsequence("adc")) # 0
    print(solution.countPalindromicSubsequence("bbcbaba")) # 4