#
# @lc app=leetcode.cn id=3098 lang=python3
#
# [3098] 求出所有子序列的能量和
#
# 给你一个长度为 n 的整数数组 nums 和一个 正 整数 k 。
# 一个 子序列 的 能量 定义为子序列中 任意 两个元素的差值绝对值的 最小值 。
# 请你返回 nums 中长度 等于 k 的 所有 子序列的 能量和 。
# 由于答案可能会很大，将答案对 109 + 7 取余 后返回。


# 示例 1：
# 输入：nums = [1,2,3,4], k = 3
# 输出：4
# 解释：
# nums 中总共有 4 个长度为 3 的子序列：[1,2,3] ，[1,3,4] ，[1,2,4] 和 [2,3,4] 。能量和为 |2 - 3| + |3 - 4| + |2 - 1| + |3 - 4| = 4 。

# 示例 2：
# 输入：nums = [2,2], k = 2
# 输出：0
# 解释：
# nums 中唯一一个长度为 2 的子序列是 [2,2] 。能量和为 |2 - 2| = 0 。

# 示例 3：
# 输入：nums = [4,3,-1], k = 2
# 输出：10
# 解释：
# nums 总共有 3 个长度为 2 的子序列：[4,3] ，[4,-1] 和 [3,-1] 。能量和为 |4 - 3| + |4 - (-1)| + |3 - (-1)| = 10 。

# 提示：
# 2 <= n == nums.length <= 50
# -10^8 <= nums[i] <= 10^8 
# 2 <= k <= n

# Hard

from collections import defaultdict
from math import inf
from typing import List
# @lc code=start
class Solution:
    def sumOfPowers(self, nums: List[int], k: int) -> int:
        MOD = 10 ** 9 + 7
        # 先对nums进行排序（排序不影响最终结果）
        nums.sort()
        n = len(nums)
        # 记dp[i][l][v]为以子序列以第i个元素结尾，长度为l，能量为v的子序列个数
        dp = [[defaultdict(int) for _ in range(k+1)] for _ in range(n)]

        res = 0
        for i in range(n):
            dp[i][1][inf] = 1 # 子序列只有一个元素，能量记为无穷大
            for j in range(i):
                # 枚举以i结尾的子序列，去掉尾巴之后的子子序列（设子子序列以j结尾）
                delta = abs(nums[i] - nums[j])
                for l in range(2, k+1):
                    for v, cnt in dp[j][l-1].items():
                        dp[i][l][min(delta, v)] = (dp[i][l][min(delta, v)] + cnt) % MOD

            for v, cnt in dp[i][k].items():
                res = (res + v * cnt % MOD) % MOD
        
        return res

# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.sumOfPowers([1,2,3,4], 3)) # 4
    print(solution.sumOfPowers([2,2], 2)) # 0
    print(solution.sumOfPowers([4,3,-1], 2)) # 10
