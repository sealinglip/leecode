#
# @lc app=leetcode.cn id=474 lang=python3
#
# [474] 一和零
#
# 给你一个二进制字符串数组 strs 和两个整数 m 和 n 。
# 请你找出并返回 strs 的最大子集的大小，该子集中 最多 有 m 个 0 和 n 个 1 。
# 如果 x 的所有元素也是 y 的元素，集合 x 是集合 y 的 子集 。

# 示例 1：
# 输入：strs = ["10", "0001", "111001", "1", "0"], m = 5, n = 3
# 输出：4
# 解释：最多有 5 个 0 和 3 个 1 的最大子集是 {"10", "0001", "1", "0"} ，因此答案是 4 。
# 其他满足题意但较小的子集包括 {"0001", "1"} 和 {"10", "1", "0"} 。{"111001"} 不满足题意，因为它含 4 个 1 ，大于 n 的值 3 。

# 示例 2：
# 输入：strs = ["10", "0", "1"], m = 1, n = 1
# 输出：2
# 解释：最大的子集是 {"0", "1"} ，所以答案是 2 。

# 提示：
# 1 <= strs.length <= 600
# 1 <= strs[i].length <= 100
# strs[i] 仅由 '0' 和 '1' 组成
# 1 <= m, n <= 100

from typing import List, Tuple
# @lc code=start
from collections import Counter


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        def countBit(s: str) -> 'Tuple':
            c = Counter(s)
            return c['0'], c['1']
        cnt = [countBit(s) for s in strs]  # 统计出每个数字的位置

        # 转化为背包问题
        # 计dp[i][j][k]为前i个数组成的0不超过j，1不超过k的最大子集大小
        # 计cnt[i]为第i个字符串中0的个数和1的个数
        # 则有 dp[i+1][j][k] = max(dp[i][j][k], dp[i][j-cnt[i][0]][k-cnt[i][1]] + 1) if j >= cnt[i][0] and k >= cnt[i][1]
        #                   = dp[i][j][k] if j < cnt[i][0] or k < cnt[i][1]
        # 由于i+1 完全依赖于i，可以将三维dp简化为二维dp
        # 最后就是要求dp[m][n]
        N = len(strs)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(N):
            zeros, ones = cnt[i]
            for j in range(m, zeros - 1, -1):
                for k in range(n, ones - 1, -1):
                    dp[j][k] = max(dp[j][k], dp[j - zeros][k - ones] + 1)

        return dp[m][n]

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.findMaxForm(["10", "0001", "111001", "1", "0"], 4, 3))
    print(solution.findMaxForm(["10", "0001", "111001", "1", "0"], 5, 3))
    print(solution.findMaxForm(["10", "0", "1"], 1, 1))
