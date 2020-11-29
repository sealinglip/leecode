#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: # 如果s为空串
            return 0

        count, l, r, rb, longest = {s[0]: 1}, 0, 1, len(s), 1
        while r < rb:
            if s[r] not in count:
                count[s[r]] = 1
                r += 1
                length = r - l
                if length > longest:
                    longest = length
            else:
                count[s[r]] = 2
                while count[s[r]] == 2:
                    c = count[s[l]]
                    if c == 1:
                        del count[s[l]]
                    else:
                        count[s[l]] = 1
                    l += 1
                r += 1

        return longest
        
# @lc code=end

