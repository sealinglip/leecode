#
# @lc app=leetcode.cn id=673 lang=python3
#
# [673] 最长递增子序列的个数
#
# 给定一个未排序的整数数组，找到最长递增子序列的个数。

# 示例 1:
# 输入: [1, 3, 5, 4, 7]
# 输出: 2
# 解释: 有两个最长递增子序列，分别是[1, 3, 4, 7] 和[1, 3, 5, 7]。

# 示例 2:
# 输入: [2, 2, 2, 2, 2]
# 输出: 5
# 解释: 最长递增子序列的长度是1，并且存在5个子序列的长度为1，因此输出5。
# 注意: 给定的数组长度不超过 2000 并且结果一定是32位有符号整数。

from typing import List, Callable
# @lc code=start
from collections import defaultdict


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        # # 方法1：动态规划
        # # 记dp[i]为以nums[i]结尾的最长子序列长度
        # # cnt[i]为以nums[i]结尾的最长子序列的组合数
        # dp = [1] * N
        # cnt = [1] * N
        # for i in range(N):
        #     for j in range(i):
        #         if nums[j] < nums[i]:
        #             if dp[j] + 1 > dp[i]:
        #                 dp[i] = dp[j] + 1
        #                 cnt[i] = cnt[j]
        #             elif dp[j] + 1 == dp[i]:
        #                 cnt[i] += cnt[j]

        # maxDp = res = 0
        # for i in range(N):
        #     if dp[i] > maxDp:
        #         maxDp = dp[i]
        #         res = cnt[i]
        #     elif dp[i] == maxDp:
        #         res += cnt[i]

        # return res

        # 方法2：参考300题的解法
        # 记d[i]为长度为i的子序列其结尾元素的列表，d为二维列表
        # 记cnt[i]为d[i]中每个元素对应的以它结尾，长度为i的子序列的个数，cnt和d同构
        # 优化：将cnt[i][k]的含义改为前缀和
        d = []
        cnt = []
        for n in nums:
            i = bisect(len(d), lambda p: d[p][-1] < n)
            c = 1
            if i > 0:
                k = bisect(len(d[i - 1]), lambda p: d[i - 1][p] >= n)
                c = cnt[i - 1][-1] - cnt[i - 1][k]
            if i >= len(d):
                d.append([n])
                cnt.append([0, c])
            else:
                d[i].append(n)
                cnt[i].append(cnt[i][-1] + c)

        return cnt[-1][-1]


def bisect(n: int, f: Callable[[int], bool]) -> int:
    l, r = 0, n
    while l < r:
        m = (l + r) >> 1
        if f(m):
            l = m + 1
        else:
            r = m

    return l


    # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.findNumberOfLIS([1, 3, 5, 4, 7]))  # 2
    print(solution.findNumberOfLIS([2, 2, 2, 2, 2]))  # 5
