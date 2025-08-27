#
# @lc app=leetcode.cn id=1717 lang=python3
#
# [1717] 删除子字符串的最大得分
#
# https://leetcode.cn/problems/maximum-score-from-removing-substrings/description/
#
# algorithms
# Medium (49.72%)
# Likes:    57
# Dislikes: 0
# Total Accepted:    10K
# Total Submissions: 17.3K
# Testcase Example:  '"cdbcbbaaabab"\n4\n5'
#
# 给你一个字符串 s 和两个整数 x 和 y 。你可以执行下面两种操作任意次。
# 删除子字符串 "ab" 并得到 x 分。
# 
# 比方说，从 "cabxbae" 删除 ab ，得到 "cxbae" 。
# 删除子字符串"ba" 并得到 y 分。
# 比方说，从 "cabxbae" 删除 ba ，得到 "cabxe" 。
# 
# 请返回对 s 字符串执行上面操作若干次能得到的最大得分。
# 
# 
# 示例 1：
# 输入：s = "cdbcbbaaabab", x = 4, y = 5
# 输出：19
# 解释：
# - 删除 "cdbcbbaaabab" 中加粗的 "ba" ，得到 s = "cdbcbbaaab" ，加 5 分。
# - 删除 "cdbcbbaaab" 中加粗的 "ab" ，得到 s = "cdbcbbaa" ，加 4 分。
# - 删除 "cdbcbbaa" 中加粗的 "ba" ，得到 s = "cdbcba" ，加 5 分。
# - 删除 "cdbcba" 中加粗的 "ba" ，得到 s = "cdbc" ，加 5 分。
# 总得分为 5 + 4 + 5 + 5 = 19 。
# 
# 示例 2：
# 输入：s = "aabbaaxybbaabb", x = 5, y = 4
# 输出：20
# 
# 
# 提示：
# 1 <= s.length <= 10^5
# 1 <= x, y <= 10^4
# s 只包含小写英文字母。
# 
# 复习
#

# @lc code=start
class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        a, b = 'a', 'b'
        if x < y:
            # 换位一下，以保证总是要尽可能多删ab，注意不是'ab'
            x, y = y, x
            a, b = b, a
        ab = a + b
        
        res = i = 0
        n = len(s)
        while i < n:
            cntA = cntB = 0
            while i < n and s[i] in ab:
                if s[i] == a:
                    cntA += 1
                else:
                    if cntA > 0:
                        cntA -= 1
                        res += x
                    else:
                        cntB += 1
                i += 1
            i += 1
            res += min(cntA, cntB) * y

        return res

        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.maximumGain("accccb", 4, 5)) # 0
    print(solution.maximumGain("cdbcbbaaabab", 4, 5)) # 19
    print(solution.maximumGain("aabbaaxybbaabb", 5, 4)) # 20
