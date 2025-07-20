#
# @lc app=leetcode.cn id=3085 lang=python3
#
# [3085] 成为 K 特殊字符串需要删除的最少字符数
#
# https://leetcode.cn/problems/minimum-deletions-to-make-string-k-special/description/
#
# algorithms
# Medium (42.34%)
# Likes:    24
# Dislikes: 0
# Total Accepted:    7.8K
# Total Submissions: 17K
# Testcase Example:  '"aabcaba"\n0'
#
# 给你一个字符串 word 和一个整数 k。
# 如果 |freq(word[i]) - freq(word[j])| <= k 对于字符串中所有下标 i 和 j  都成立，则认为 word 是 k
# 特殊字符串。
# 此处，freq(x) 表示字符 x 在 word 中的出现频率，而 |y| 表示 y 的绝对值。
# 返回使 word 成为 k 特殊字符串 需要删除的字符的最小数量。
# 
# 
# 示例 1：
# 输入：word = "aabcaba", k = 0
# 输出：3
# 解释：可以删除 2 个 "a" 和 1 个 "c" 使 word 成为 0 特殊字符串。word 变为 "baba"，此时 freq('a') ==
# freq('b') == 2。
# 
# 示例 2：
# 输入：word = "dabdcbdcdcd", k = 2
# 输出：2
# 解释：可以删除 1 个 "a" 和 1 个 "d" 使 word 成为 2 特殊字符串。word 变为 "bdcbdcdcd"，此时 freq('b')
# == 2，freq('c') == 3，freq('d') == 4。
# 
# 示例 3：
# 输入：word = "aaabaaa", k = 2
# 输出：1
# 解释：可以删除 1 个 "b" 使 word 成为 2特殊字符串。因此，word 变为 "aaaaaa"，此时每个字母的频率都是 6。
# 
# 
# 提示：
# 1 <= word.length <= 10^5
# 0 <= k <= 10^5
# word 仅由小写英文字母组成。
# 
# 
#

# @lc code=start
from collections import Counter


class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        res = n = len(word)
        cnts = sorted(Counter(word).values())
        # 滑动窗口
        c = len(cnts)
        l = r = 0
        accum = 0
        while r < c:
            while r < c and cnts[r] <= cnts[l] + k:
                accum += cnts[r]
                r += 1
            res = min(res, n - accum + (r-c) * (cnts[l]+k)) # 要删除的字符：左边界外的所有，右边界外不是所有，只有超出部分需要删除，所以如果只减accum就减少了，要需要减去右边界外可以保留的部分，这样剩余的才是需要删除的
            if r == c:
                break
            accum -= cnts[l]
            l += 1

        return res
        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.minimumDeletions("eeffmeefexefefffefemeexfeeffeefmfhxemmeeffffmfmmfffeeeffeffeffqffffefmeeeeefffmeffffffefefqfefffmfffmefeeeefexeffffffemffeffffffffemfeefeffffefjefxfffffffemfffffmfffefeemfeffffffmfffffeefefeffxfefefffeefffeqeffeefeemfefeemfffxfxeffffffeffffmfffexfffffee", 54)) # 49
    print(solution.minimumDeletions("aabcaba", 0)) # 3
    print(solution.minimumDeletions("dabdcbdcdcd", 2)) # 2
    print(solution.minimumDeletions("aaabaaa", 2)) # 1
