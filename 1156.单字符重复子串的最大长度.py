#
# @lc app=leetcode.cn id=1156 lang=python3
#
# [1156] 单字符重复子串的最大长度
#
# 如果字符串中的所有字符都相同，那么这个字符串是单字符重复的字符串。

# 给你一个字符串 text，你只能交换其中两个字符一次或者什么都不做，然后得到一些单字符重复的子串。返回其中最长的子串的长度。


# 示例 1：
# 输入：text = "ababa"
# 输出：3

# 示例 2：
# 输入：text = "aaabaaa"
# 输出：6

# 示例 3：
# 输入：text = "aaabbaaa"
# 输出：4

# 示例 4：
# 输入：text = "aaaaa"
# 输出：5

# 示例 5：
# 输入：text = "abcdef"
# 输出：1


# 提示：
# 1 <= text.length <= 20000
# text 仅由小写英文字母组成。

# 复习

# @lc code=start
from collections import Counter


class Solution:
    def maxRepOpt1(self, text: str) -> int:
        cnt = Counter(text)  # 先获得所有字符的计数
        res = 0
        n = len(text)
        # 滑动窗口
        i = 0
        while i < n:
            # 从当前字符后探相同的一段
            j = i
            while j < n and text[j] == text[i]:
                j += 1
            # 此时实际连续的区间长度为j - i
            # 跳过下一个字符看看后面一段是不是能跟前面接上
            k = j + 1
            while k < n and text[k] == text[i]:
                k += 1

            # 即使跳过一个不同字符，后面那么跟前面的接不上，只要text[i]数量够多，也能交换一个字符得到比连续区间长1的区间
            res = max(res, min(k - i, cnt[text[i]]))

            i = j

        return res
# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxRepOpt1("ababa"))  # 3
    print(solution.maxRepOpt1("aabaabaaaa"))  # 7
    print(solution.maxRepOpt1("aaabaaa"))  # 6
    print(solution.maxRepOpt1("aaabbaaa"))  # 4
    print(solution.maxRepOpt1("aaaaa"))  # 5
    print(solution.maxRepOpt1("abcdef"))  # 1
