#
# @lc app=leetcode.cn id=686 lang=python3
#
# [686] 重复叠加字符串匹配
#
# 给定两个字符串 a 和 b，寻找重复叠加字符串 a 的最小次数，使得字符串 b 成为叠加后的字符串 a 的子串，如果不存在则返回 - 1。

# 注意：字符串 "abc" 重复叠加 0 次是 ""，重复叠加 1 次是 "abc"，重复叠加 2 次是 "abcabc"。


# 示例 1：
# 输入：a = "abcd", b = "cdabcdab"
# 输出：3
# 解释：a 重复叠加三遍后为 "abcdabcdabcd", 此时 b 是其子串。

# 示例 2：
# 输入：a = "a", b = "aa"
# 输出：2

# 示例 3：
# 输入：a = "a", b = "a"
# 输出：1

# 示例 4：
# 输入：a = "abc", b = "wxyz"
# 输出：- 1


# 提示：
# 1 <= a.length <= 10^4
# 1 <= b.length <= 10^4
# a 和 b 由小写英文字母组成

# @lc code=start
class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        L = len(b)
        N = len(a)

        s = b.find(a)
        if s == -1:
            if a.find(b) != -1:
                return 1
            elif (a + a).find(b) != -1:
                return 2
            else:
                return -1
        elif s >= N:
            return -1
        elif s and b[:s] != a[-s:]:
            return -1
        times = 2 if s else 1
        s += N
        while s + N <= L:
            if b[s:s + N] != a:
                return -1
            s += N
            times += 1
        if s < L:
            if b[s:] != a[:L-s]:
                return -1
            times += 1
        return times


# @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.repeatedStringMatch(
        "abcd", "bcdab"))  # 2
    print(solution.repeatedStringMatch(
        "aaaaaaaaaaaaaaaaaaaaaab", "ba"))  # 2
    print(solution.repeatedStringMatch("abcd", "cdabcdab"))  # 3
    print(solution.repeatedStringMatch("aa", "a"))  # 1
    print(solution.repeatedStringMatch("a", "aa"))  # 2
    print(solution.repeatedStringMatch("a", "a"))  # 1
    print(solution.repeatedStringMatch("abc", "wxyz"))  # -1
