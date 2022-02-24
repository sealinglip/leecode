#
# @lc app=leetcode.cn id=917 lang=python3
#
# [917] 仅仅反转字母
#
# 给你一个字符串 s ，根据下述规则反转字符串：

# 所有非英文字母保留在原有位置。
# 所有英文字母（小写或大写）位置反转。
# 返回反转后的 s 。

# 示例 1：
# 输入：s = "ab-cd"
# 输出："dc-ba"

# 示例 2：
# 输入：s = "a-bC-dEf-ghIj"
# 输出："j-Ih-gfE-dCba"

# 示例 3：
# 输入：s = "Test1ng-Leet=code-Q!"
# 输出："Qedo1ct-eeLg=ntse-T!"


# 提示
# 1 <= s.length <= 100
# s 仅由 ASCII 值在范围[33, 122] 的字符组成
# s 不含 '\"' 或 '\\'

# @lc code=start
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        N = len(s)
        chars = [c for c in s]
        l, r = 0, N - 1
        while l < r:
            # 从左向右找字母
            while l < N and not ('a' <= chars[l] <= 'z' or 'A' <= chars[l] <= 'Z'):
                l += 1
            # 从右向左找字母
            while r >= 0 and not ('a' <= chars[r] <= 'z' or 'A' <= chars[r] <= 'Z'):
                r -= 1

            if l < r:
                chars[l], chars[r] = chars[r], chars[l]
            l += 1
            r -= 1
        return "".join(chars)
# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    print(solution.reverseOnlyLetters("7_28]"))  # "7_28]"
    print(solution.reverseOnlyLetters("ab-cd"))  # "dc-ba"
    print(solution.reverseOnlyLetters("a-bC-dEf-ghIj"))  # "j-Ih-gfE-dCba"
    # "Qedo1ct-eeLg=ntse-T!"
    print(solution.reverseOnlyLetters("Test1ng-Leet=code-Q!"))
