#
# @lc app=leetcode.cn id=1262 lang=python3
#
# [1262] 可被三整除的最大和
#
# 给你一个整数数组 nums，请你找出并返回能被三整除的元素最大和。


# 示例 1：
# 输入：nums = [3, 6, 5, 1, 8]
# 输出：18
# 解释：选出数字 3, 6, 1 和 8，它们的和是 18（可被 3 整除的最大和）。

# 示例 2：
# 输入：nums = [4]
# 输出：0
# 解释：4 不能被 3 整除，所以无法选出数字，返回 0。

# 示例 3：
# 输入：nums = [1, 2, 3, 4, 4]
# 输出：12
# 解释：选出数字 1, 3, 4 以及 4，它们的和是 12（可被 3 整除的最大和）。


# 提示：
# 1 <= nums.length <= 4 * 10 ^ 4
# 1 <= nums[i] <= 10 ^ 4

from math import inf
from typing import List
# @lc code=start


class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        # 方法1：贪心
        # res = 0
        # stat = [[inf, inf]
        #         for _ in range(2)]  # 分别记录余数为1和2的数的最小和次最小
        # for num in nums:
        #     res += num
        #     r = num % 3 # 看余数分别处理
        #     if r:
        #         r -= 1
        #         if num <= stat[r][0]:
        #             stat[r][0], stat[r][1] = num, stat[r][0]
        #         elif num < stat[r][1]:
        #             stat[r][1] = num

        # r = res % 3
        # if r == 1:
        #     # 如果余数是1，要么舍弃余数为1的最小的数，或余数为2的最小的两个数
        #     res -= min(sum(stat[1]), stat[0][0])
        # elif r == 2:
        #     # 如果余数是2，要么舍弃余数为2的最小的数，或余数为1的最小的两个数
        #     res -= min(sum(stat[0]), stat[1][0])

        # return res

        # 方法2：动规
        # 记dp(i,j)为前i个数选出部分数使其和模3余数为j时能达到的最大和
        # 已知dp(0,0) = 0, dp(0,1) = dp(0,2) = -∞
        # 从当前数模3的余数来推到状态转移方案，比较简单
        # 又dp(i, *)只依赖dp(i-1, *)，状态矩阵可以压缩
        dp = [-inf] * 3
        dp[0] = 0
        for x in nums:
            r = x % 3
            tmp = dp[:]
            for i in range(3):
                tmp[(i+r) % 3] = max(tmp[(i+r) % 3], dp[i] + x)
            dp = tmp
            
        return dp[0]


        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.maxSumDivThree([3, 6, 5, 1, 8]))  # 18
    print(solution.maxSumDivThree([4]))  # 0
    print(solution.maxSumDivThree([1, 2, 3, 4, 4]))  # 12
