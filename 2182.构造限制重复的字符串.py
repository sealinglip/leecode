#
# @lc app=leetcode.cn id=2182 lang=python3
#
# [2182] 构造限制重复的字符串
#
# 给你一个字符串 s 和一个整数 repeatLimit ，用 s 中的字符构造一个新字符串 repeatLimitedString ，使任何字母 连续 出现的次数都不超过 repeatLimit 次。你不必使用 s 中的全部字符。

# 返回 字典序最大的 repeatLimitedString 。

# 如果在字符串 a 和 b 不同的第一个位置，字符串 a 中的字母在字母表中出现时间比字符串 b 对应的字母晚，则认为字符串 a 比字符串 b 字典序更大 。如果字符串中前 min(a.length, b.length) 个字符都相同，那么较长的字符串字典序更大。

 
# 示例 1：
# 输入：s = "cczazcc", repeatLimit = 3
# 输出："zzcccac"
# 解释：使用 s 中的所有字符来构造 repeatLimitedString "zzcccac"。
# 字母 'a' 连续出现至多 1 次。
# 字母 'c' 连续出现至多 3 次。
# 字母 'z' 连续出现至多 2 次。
# 因此，没有字母连续出现超过 repeatLimit 次，字符串是一个有效的 repeatLimitedString 。
# 该字符串是字典序最大的 repeatLimitedString ，所以返回 "zzcccac" 。
# 注意，尽管 "zzcccca" 字典序更大，但字母 'c' 连续出现超过 3 次，所以它不是一个有效的 repeatLimitedString 。

# 示例 2：
# 输入：s = "aababab", repeatLimit = 2
# 输出："bbabaa"
# 解释：
# 使用 s 中的一些字符来构造 repeatLimitedString "bbabaa"。 
# 字母 'a' 连续出现至多 2 次。 
# 字母 'b' 连续出现至多 2 次。 
# 因此，没有字母连续出现超过 repeatLimit 次，字符串是一个有效的 repeatLimitedString 。 
# 该字符串是字典序最大的 repeatLimitedString ，所以返回 "bbabaa" 。 
# 注意，尽管 "bbabaaa" 字典序更大，但字母 'a' 连续出现超过 2 次，所以它不是一个有效的 repeatLimitedString 。
 

# 提示：
# 1 <= repeatLimit <= s.length <= 10^5
# s 由小写英文字母组成

# @lc code=start
from collections import Counter


class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        cnt = Counter(s)
        avail = sorted(cnt.keys(), reverse=True) # 可用字符
        n = len(avail)
        i = j = k = 0 # i 当前未用完的最大字符的索引 j 当前未使用的最大字符的索引 k 当前尾部相同字符个数
        ret = []
        while i < n and j < n:
            c = avail[i]
            d = avail[j]
            if cnt[c] == 0: # 当前字符已经用完，开始使用后面的字符，并重置k
                k, i = 0, i + 1
            elif k < repeatLimit:
                cnt[c] -= 1
                ret.append(c)
                k += 1
            elif j <= i or cnt[d] == 0: # 当前字符已经超限，找后面可用的字符
                j += 1
            else: # 当前字符已经超限，用后面可用的字符，并重置k
                cnt[d] -= 1
                ret.append(d)
                k = 0

        return ''.join(ret)

# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.repeatLimitedString("cczazcc", 3)) # "zzcccac"
    print(solution.repeatLimitedString("aababab", 2)) # "bbabaa"