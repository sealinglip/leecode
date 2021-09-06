#
# @lc app=leetcode.cn id=541 lang=python3
#
# [541] 反转字符串 II
#
# 给定一个字符串 s 和一个整数 k，从字符串开头算起，每 2k 个字符反转前 k 个字符。

# 如果剩余字符少于 k 个，则将剩余字符全部反转。
# 如果剩余字符小于 2k 但大于或等于 k 个，则反转前 k 个字符，其余字符保持原样。


# 示例 1：
# 输入：s = "abcdefg", k = 2
# 输出："bacdfeg"

# 示例 2：
# 输入：s = "abcd", k = 2
# 输出："bacd"


# 提示：

# 1 <= s.length <= 10^4
# s 仅由小写英文组成
# 1 <= k <= 10^4

# @lc code=start
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        N = len(s)
        reversed = []

        i, k2 = 0, k << 1
        while i < N:
            rest = N - i
            if rest <= k:
                reversed.append(s[i:N][::-1])
                i = N
            elif rest <= k2:
                reversed.append(s[i:i+k][::-1])
                reversed.append(s[i+k:N])
                i = N
            else:
                reversed.append(s[i:i+k][::-1])
                reversed.append(s[i+k:i+k2])
                i += k2

        return "".join(reversed)

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.reverseStr("abcdefg", 2))
    print(solution.reverseStr("abcd", 2))
