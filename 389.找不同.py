#
# @lc app=leetcode.cn id=389 lang=python3
#
# [389] 找不同
#
# 给定两个字符串 s 和 t，它们只包含小写字母。
# 字符串 t 由字符串 s 随机重排，然后在随机位置添加一个字母。
# 请找出在 t 中被添加的字母。


# 示例 1：
# 输入：s = "abcd", t = "abcde"
# 输出："e"
# 解释：'e' 是那个被添加的字母。

# 示例 2：
# 输入：s = "", t = "y"
# 输出："y"

# 示例 3：
# 输入：s = "a", t = "aa"
# 输出："a"

# 示例 4：
# 输入：s = "ae", t = "aea"
# 输出："a" 

# 提示：
# 0 <= s.length <= 1000
# t.length == s.length + 1
# s 和 t 只包含小写字母

# @lc code=start
from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        c1 = Counter(s)
        c2 = Counter(t)

        for l in c2:
            if l not in c1 or c1[l] < c2[l]:
                return l

# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.findTheDifference("abcd", "abcde"))
    print(solution.findTheDifference("", "y"))
    print(solution.findTheDifference("a", "aa"))
    print(solution.findTheDifference("ae", "aea"))