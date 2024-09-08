# 给你一个字符串 s ，你需要将它分割成一个或者更多的 平衡 子字符串。比方说，s == "ababcc" 那么 ("abab", "c", "c") ，("ab", "abc", "c") 和 ("ababcc") 都是合法分割，
# 但是 ("a", "bab", "cc") ，("aba", "bc", "c") 和 ("ab", "abcc") 不是，不平衡的子字符串用粗体表示。

# 请你返回 s 最少 能分割成多少个平衡子字符串。
# 注意：一个 平衡 字符串指的是字符串中所有字符出现的次数都相同。

# 示例 1：
# 输入：s = "fabccddg"
# 输出：3
# 解释：
# 我们可以将 s 分割成 3 个子字符串：("fab, "ccdd", "g") 或者 ("fabc", "cd", "dg") 。

# 示例 2：
# 输入：s = "abababaccddb"
# 输出：2
# 解释：
# 我们可以将 s 分割成 2 个子字符串：("abab", "abaccddb") 。

# 提示：
# 1 <= s.length <= 1000
# s 只包含小写英文字母。

from collections import defaultdict
from math import inf


class Solution:
    def minimumSubstringsInPartition(self, s: str) -> int:
        n = len(s)
        # 动规
        # 记dp(i)为s[i:]的最少分隔平衡子字符串数
        # dp(i) = min(dp(j) for j in range(i+1, n) if s[i:j] 平衡) + 1
        # dp(n) = 0
        dp = [inf] * (n + 1)
        dp[-1] = 0
        cnt = defaultdict(int)
        for i in range(n-1, -1, -1):
            cnt.clear() # 清空
            maxCnt = 0
            for j in range(i+1, n+1):
                cnt[s[j-1]] += 1
                maxCnt = max(maxCnt, cnt[s[j-1]])
                if maxCnt * len(cnt) == j - i and dp[j] != inf:
                    dp[i] = min(dp[i], dp[j] + 1)

        return dp[0]

if __name__ == "__main__":
    solution = Solution()
    print(solution.minimumSubstringsInPartition("c")) # 1
    print(solution.minimumSubstringsInPartition("fabccddg")) # 3
    print(solution.minimumSubstringsInPartition("abababaccddb")) # 2
