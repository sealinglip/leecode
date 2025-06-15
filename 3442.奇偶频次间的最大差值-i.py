#
# @lc app=leetcode.cn id=3442 lang=python3
#
# [3442] 奇偶频次间的最大差值 I
#
# https://leetcode.cn/problems/maximum-difference-between-even-and-odd-frequency-i/description/
#
# algorithms
# Easy (60.73%)
# Likes:    3
# Dislikes: 0
# Total Accepted:    5.4K
# Total Submissions: 8.3K
# Testcase Example:  '"aaaaabbc"'
#
# 给你一个由小写英文字母组成的字符串 s 。
# 
# 请你找出字符串中两个字符 a1 和 a2 的出现频次之间的 最大 差值 diff = a1 - a2，这两个字符需要满足：
# 
# a1 在字符串中出现 奇数次 。
# a2 在字符串中出现 偶数次 。
# 
# 返回 最大 差值。
# 
# 
# 示例 1：
# 输入：s = "aaaaabbc"
# 输出：3
# 解释：
# 字符 'a' 出现 奇数次 ，次数为 5 ；字符 'b' 出现 偶数次 ，次数为 2 。
# 最大差值为 5 - 2 = 3 。
# 
# 示例 2：
# 输入：s = "abcabcab"
# 输出：1
# 解释：
# 字符 'a' 出现 奇数次 ，次数为 3 ；字符 'c' 出现 偶数次 ，次数为 2 。
# 最大差值为 3 - 2 = 1 。
# 
# 
# 提示：
# 3 <= s.length <= 100
# s 仅由小写英文字母组成。
# s 至少由一个出现奇数次的字符和一个出现偶数次的字符组成。
# 
#

# @lc code=start
from collections import Counter


class Solution:
    def maxDifference(self, s: str) -> int:
        cnt = Counter(s)
        odd = max(v for v in cnt.values() if v & 1 == 1)
        even = min(v for v in cnt.values() if v & 1 == 0)
        return odd - even
        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.maxDifference("aaaaabbc")) # 3
    print(solution.maxDifference("abcabcab")) # 1
