#
# @lc app=leetcode.cn id=395 lang=python3
#
# [395] 至少有K个重复字符的最长子串
#
# 找到给定字符串（由小写字符组成）中的最长子串 T ， 要求 T 中的每一字符出现次数都不少于 k 。输出 T 的长度。

# 示例 1:
# 输入:
# s = "aaabb", k = 3
# 输出:
# 3

# 最长子串为 "aaa" ，其中 'a' 重复了 3 次。

# 示例 2:
# 输入:
# s = "ababbc", k = 2
# 输出:
# 5

# 最长子串为 "ababb" ，其中 'a' 重复了 2 次， 'b' 重复了 3 次。

# @lc code=start
from collections import Counter


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        N = len(s)
        uc = Counter(s)
        # 如果所有的字符计数都 >= k，则直接返回整个字符串的长度
        for c in uc:
            if uc.get(c) < k:
                # 分治
                return max(self.longestSubstring(part, k) for part in s.split(c))

        return N


        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.longestSubstring("aaabb", 3))
    print(solution.longestSubstring("ababbc", 2))
