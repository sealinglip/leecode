#
# @lc app=leetcode.cn id=387 lang=python3
#
# [387] 字符串中的第一个唯一字符
#
# 给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。

# 示例：
# s = "leetcode"
# 返回 0

# s = "loveleetcode"
# 返回 2

# 提示：你可以假定该字符串只包含小写字母。

# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:
        if not s:
            return -1

        L = len(s)
        pos = [L] * 26 # 26个字母
        for idx, c in enumerate(s):
            i = ord(c) - ord('a')
            if pos[i] == L:
                pos[i] = idx
            elif pos[i] < L:
                pos[i] = L + 1

        i = min(pos)
        return -1 if i >= L else i


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.firstUniqChar("leetcode"))
    print(solution.firstUniqChar("loveleetcode"))