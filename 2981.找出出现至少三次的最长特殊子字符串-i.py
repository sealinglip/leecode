#
# @lc app=leetcode.cn id=2981 lang=python3
#
# [2981] 找出出现至少三次的最长特殊子字符串 I
#
# 给你一个仅由小写英文字母组成的字符串 s 。

# 如果一个字符串仅由单一字符组成，那么它被称为 特殊 字符串。例如，字符串 "abc" 不是特殊字符串，而字符串 "ddd"、"zz" 和 "f" 是特殊字符串。

# 返回在 s 中出现 至少三次 的 最长特殊子字符串 的长度，如果不存在出现至少三次的特殊子字符串，则返回 -1 。

# 子字符串 是字符串中的一个连续 非空 字符序列。


# 示例 1：
# 输入：s = "aaaa"
# 输出：2
# 解释：出现三次的最长特殊子字符串是 "aa" ：子字符串 "aaaa"、"aaaa" 和 "aaaa"。
# 可以证明最大长度是 2 。

# 示例 2：
# 输入：s = "abcdef"
# 输出：-1
# 解释：不存在出现至少三次的特殊子字符串。因此返回 -1 。

# 示例 3：
# 输入：s = "abcaba"
# 输出：1
# 解释：出现三次的最长特殊子字符串是 "a" ：子字符串 "abcaba"、"abcaba" 和 "abcaba"。
# 可以证明最大长度是 1 。
 

# 提示：
# 3 <= s.length <= 50
# s 仅由小写英文字母组成。

# @lc code=start
class Solution:
    def maximumLength(self, s: str) -> int:
        count = [{} for _ in range(26)]
        prevChar = None
        continueCnt = 0
        for c in s:
            if c != prevChar and prevChar:
                idx = ord(prevChar) - ord('a')
                count[idx][continueCnt] = count[idx].get(continueCnt, 0) + 1
                continueCnt = 0
            continueCnt += 1
            prevChar = c
        idx = ord(prevChar) - ord('a')
        count[idx][continueCnt] = count[idx].get(continueCnt, 0) + 1

        res = -1
        for d in count:
            if d:
                maxLen = max(d.keys())
                accum = 0
                i = 0
                for l in range(maxLen, 0, -1):
                    accum += i
                    if l in d:
                        accum += d[l]
                        i += 1
                    if accum > 2:
                        res = max(res, l)
                        break

        return res
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.maximumLength("aaaa")) # 2
    print(solution.maximumLength("abcdef")) # -1
    print(solution.maximumLength("abcaba")) # 1