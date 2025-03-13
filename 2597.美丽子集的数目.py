#
# @lc app=leetcode.cn id=2597 lang=python3
#
# [2597] 美丽子集的数目
#
# 给你一个由正整数组成的数组 nums 和一个 正 整数 k 。
# 如果 nums 的子集中，任意两个整数的绝对差均不等于 k ，则认为该子数组是一个 美丽 子集。
# 返回数组 nums 中 非空 且 美丽 的子集数目。
# nums 的子集定义为：可以经由 nums 删除某些元素（也可能不删除）得到的一个数组。
# 只有在删除元素时选择的索引不同的情况下，两个子集才会被视作是不同的子集。


# 示例 1：
# 输入：nums = [2,4,6], k = 2
# 输出：4
# 解释：数组 nums 中的美丽子集有：[2], [4], [6], [2, 6] 。
# 可以证明数组 [2,4,6] 中只存在 4 个美丽子集。

# 示例 2：
# 输入：nums = [1], k = 1
# 输出：1
# 解释：数组 nums 中的美丽数组有：[1] 。
# 可以证明数组 [1] 中只存在 1 个美丽子集。 
 

# 提示：
# 1 <= nums.length <= 18
# 1 <= nums[i], k <= 1000
# 复习

from collections import defaultdict
from typing import List
# @lc code=start
class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        # 按模k分组，组与组之间的数字肯定相互不影响
        groups = defaultdict(dict)
        for x in nums:
            m = x % k
            groups[m][x] = groups[m].get(x, 0) + 1 # 计数

        res = 1
        for g in groups.values():
            keys = sorted(g.keys())
            n = len(keys)
            # dp[i]表示遍历到keys[i]时，美丽子集的个数
            # dp[i][0]表示keys[i]不入选，dp[i][1]表示入选
            # 状态转移方程为：
            # dp[i][0] = dp[i-1][0] + dp[i-1][1]
            # dp[i][1] = dp[i-1][0] * (2 ^ (g[keys[i]]) - 1) if keys[i] - keys[i-1] == k
            # dp[i][1] = (dp[i-1][0] + dp[i-1][1]) * (2 ^ (g[keys[i]]) - 1) if keys[i] - keys[i-1] != k

            dp = [[0] * 2 for _ in range(n)]
            dp[0][0] = 1
            dp[0][1] = (1 << g[keys[0]]) - 1
            for i in range(1, n):
                dp[i][0] = sum(dp[i-1])
                if keys[i] - keys[i-1] == k:
                    dp[i][1] = dp[i-1][0] * ((1 << g[keys[i]]) - 1)
                else:
                    dp[i][1] = dp[i][0] * ((1 << g[keys[i]]) - 1)
        
            res *= sum(dp[-1])

        return res - 1 # 不能什么数都不选，所以-1去掉空集这种情况
        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.beautifulSubsets([2,4,6], 2)) # 4
    print(solution.beautifulSubsets([1], 1)) # 1
