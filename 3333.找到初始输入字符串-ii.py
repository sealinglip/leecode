#
# @lc app=leetcode.cn id=3333 lang=python3
#
# [3333] 找到初始输入字符串 II
#
# https://leetcode.cn/problems/find-the-original-typed-string-ii/description/
#
# algorithms
# Hard (25.35%)
# Likes:    14
# Dislikes: 0
# Total Accepted:    2.9K
# Total Submissions: 8K
# Testcase Example:  '"aabbccdd"\n7'
#
# Alice 正在她的电脑上输入一个字符串。但是她打字技术比较笨拙，她 可能 在一个按键上按太久，导致一个字符被输入 多次 。
# 给你一个字符串 word ，它表示 最终 显示在 Alice 显示屏上的结果。同时给你一个 正 整数 k ，表示一开始 Alice 输入字符串的长度 至少为 k 。
# 
# 请你返回 Alice 一开始可能想要输入字符串的总方案数。
# 由于答案可能很大，请你将它对 10^9 + 7 取余 后返回。
# 
# 
# 示例 1：
# 输入：word = "aabbccdd", k = 7
# 输出：5
# 解释：
# 可能的字符串包括："aabbccdd" ，"aabbccd" ，"aabbcdd" ，"aabccdd" 和 "abbccdd" 。
# 
# 示例 2：
# 输入：word = "aabbccdd", k = 8
# 输出：1
# 解释：
# 唯一可能的字符串是 "aabbccdd" 。
# 
# 示例 3：
# 输入：word = "aaabbb", k = 3
# 输出：8
# 
# 
# 提示：
# 1 <= word.length <= 5 * 10^5
# word 只包含小写英文字母。
# 1 <= k <= 2000
# 
# 复习

# @lc code=start
from itertools import accumulate


class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        n = len(word)
        if n < k:
            return 0 # 无法满足要求
        
        MOD = 10 ** 9 + 7
        # 如果不考虑原串长度要求k，原串总的方案数 = 每个片段重复字符数 连乘
        cnts = []
        res = 1 # 如果不考虑原串长度要求k，原串总的方案数
        cnt = 0
        for i in range(n):
            cnt += 1
            if i == n-1 or word[i] != word[i+1]:
                # 如果cnt为1，这个片段就是必选
                if cnt > 1:
                    if k > 0:
                        cnts.append(cnt - 1) # cnt-1 代表这个片段有这么多字符是可选的
                    res = res * cnt % MOD
                k -= 1
                cnt = 0

        if k <= 0:
            return res
        
        # 动规求长度比k小的原串方案数
        # 记dp[i][j]为前i个片段最多选j个字符的方案数(j <= k-1)
        # 则dp[0][*] = 1，就是方案数为1，啥也没得选
        # dp[i][j] = sum(dp[i-1][j-x] for x in range(min(cnts[i], j)+1))
        # dp = [[0] * k for _ in range(len(cnts) + 1)]
        # dp[0] = [1] * k
        # for i, c in enumerate(cnts):
        #     s = list(accumulate(dp[i], initial=0))
        #     for j in range(k):
        #         dp[i+1][j] = (s[j+1] - s[max(j-c, 0)]) % MOD
        
        # return (res - dp[-1][-1]) % MOD

        # 压缩状态栈
        dp = [1] * k
        for c in cnts:
            # 计算前缀和
            for j in range(1, k):
                dp[j] = (dp[j] + dp[j-1]) % MOD
            # 计算子数组和
            for j in range(k-1, c, -1):
                dp[j] -= dp[j-c-1]
        
        return (res - dp[-1]) % MOD

        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.possibleStringCount("aabbccdd", 7)) # 5
    print(solution.possibleStringCount("aabbccdd", 8)) # 1
    print(solution.possibleStringCount("aaabbb", 3)) # 8
