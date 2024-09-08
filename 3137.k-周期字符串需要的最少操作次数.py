#
# @lc app=leetcode.cn id=3137 lang=python3
#
# [3137] K 周期字符串需要的最少操作次数
#
# 给你一个长度为 n 的字符串 word 和一个整数 k ，其中 k 是 n 的因数。
# 在一次操作中，你可以选择任意两个下标 i 和 j，其中 0 <= i, j < n ，且这两个下标都可以被 k 整除，然后用从 j 开始的长度为 k 的子串替换从 i 开始的长度为 k 的子串。也就是说，将子串 word[i..i + k - 1] 替换为子串 word[j..j + k - 1] 。
# 返回使 word 成为 K 周期字符串 所需的 最少 操作次数。
# 如果存在某个长度为 k 的字符串 s，使得 word 可以表示为任意次数连接 s ，则称字符串 word 是 K 周期字符串 。例如，如果 word == "ababab"，那么 word 就是 s = "ab" 时的 2 周期字符串 。


# 示例 1：
# 输入：word = "leetcodeleet", k = 4
# 输出：1
# 解释：可以选择 i = 4 和 j = 0 获得一个 4 周期字符串。这次操作后，word 变为 "leetleetleet" 。

# 示例 2：
# 输入：word = "leetcoleet", k = 2
# 输出：3
# 解释：可以执行以下操作获得一个 2 周期字符串。
# i	j	word
# 0	2	etetcoleet
# 4	0	etetetleet
# 6	0	etetetetet
 
# 提示：
# 1 <= n == word.length <= 10^5
# 1 <= k <= word.length
# k 能整除 word.length 。
# word 仅由小写英文字母组成。

# 复习
# @lc code=start
from collections import Counter


class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        cnt = Counter()
        for i in range(0, len(word), k):
            cnt[word[i:i+k]] += 1
        
        mostFreq = cnt.most_common(1)[0][1]
        return (len(word) // k) - mostFreq
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    print(solution.minimumOperationsToMakeKPeriodic("leetcodeleet", 4)) # 1
    print(solution.minimumOperationsToMakeKPeriodic("leetcoleet", 2)) # 3
