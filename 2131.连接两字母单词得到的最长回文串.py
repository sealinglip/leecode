#
# @lc app=leetcode.cn id=2131 lang=python3
#
# [2131] 连接两字母单词得到的最长回文串
#
# https://leetcode.cn/problems/longest-palindrome-by-concatenating-two-letter-words/description/
#
# algorithms
# Medium (43.61%)
# Likes:    75
# Dislikes: 0
# Total Accepted:    19.3K
# Total Submissions: 39.1K
# Testcase Example:  '["lc","cl","gg"]'
#
# 给你一个字符串数组 words 。words 中每个元素都是一个包含 两个 小写英文字母的单词。
# 请你从 words 中选择一些元素并按 任意顺序 连接它们，并得到一个 尽可能长的回文串 。每个元素 至多 只能使用一次。
# 请你返回你能得到的最长回文串的 长度 。如果没办法得到任何一个回文串，请你返回 0 。
# 回文串 指的是从前往后和从后往前读一样的字符串。
# 
# 
# 示例 1：
# 输入：words = ["lc","cl","gg"]
# 输出：6
# 解释：一个最长的回文串为 "lc" + "gg" + "cl" = "lcggcl" ，长度为 6 。
# "clgglc" 是另一个可以得到的最长回文串。
# 
# 示例 2：
# 输入：words = ["ab","ty","yt","lc","cl","ab"]
# 输出：8
# 解释：最长回文串是 "ty" + "lc" + "cl" + "yt" = "tylcclyt" ，长度为 8 。
# "lcyttycl" 是另一个可以得到的最长回文串。
# 
# 示例 3：
# 输入：words = ["cc","ll","xx"]
# 输出：2
# 解释：最长回文串是 "cc" ，长度为 2 。
# "ll" 是另一个可以得到的最长回文串。"xx" 也是。
# 
# 
# 提示：
# 1 <= words.length <= 10^5
# words[i].length == 2
# words[i] 仅包含小写英文字母。
# 
#

from collections import Counter
from typing import List
# @lc code=start
class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        res = 0
        midAvail = True
        cnt = Counter(words)
        for k in list(cnt.keys()):
            c = cnt[k]
            if k[0] == k[1]:
                res += (c >> 1) * 4
                if (c & 1) and midAvail:
                    midAvail = False
                    res += 2
            elif k[::-1] in cnt:
                c2 = cnt[k[::-1]]
                res += min(c, c2) * 4
                cnt[k[::-1]] = 0
                cnt[k] = 0

        return res
        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.longestPalindrome(["lc","cl","gg"])) # 6
    print(solution.longestPalindrome(["ab","ty","yt","lc","cl","ab"])) # 8
    print(solution.longestPalindrome(["cc","ll","xx"])) # 2
