# 给你一个长度为 n 的 正 整数数组 nums 。

# 如果两个 非负 整数数组 (arr1, arr2) 满足以下条件，我们称它们是 单调 数组对：

# 两个数组的长度都是 n 。
# arr1 是单调 非递减 的，换句话说 arr1[0] <= arr1[1] <= ... <= arr1[n - 1] 。
# arr2 是单调 非递增 的，换句话说 arr2[0] >= arr2[1] >= ... >= arr2[n - 1] 。
# 对于所有的 0 <= i <= n - 1 都有 arr1[i] + arr2[i] == nums[i] 。
# 请你返回所有 单调 数组对的数目。

# 由于答案可能很大，请你将它对 10^9 + 7 取余 后返回。


# 示例 1：
# 输入：nums = [2,3,2]
# 输出：4
# 解释：
# 单调数组对包括：
# ([0, 1, 1], [2, 2, 1])
# ([0, 1, 2], [2, 2, 0])
# ([0, 2, 2], [2, 1, 0])
# ([1, 2, 2], [1, 1, 0])

# 示例 2：
# 输入：nums = [5,5,5,5]
# 输出：126


# 提示：
# 1 <= n == nums.length <= 2000
# 1 <= nums[i] <= 1000

# Hard  跟3250题相比只是数组元素的值域变大了

from math import comb
from typing import List
from itertools import pairwise

class Solution:
    def countOfPairs(self, nums: List[int]) -> int:
        # MOD = 10 ** 9 + 7
        # # 动态规划
        # # 记dp(i,k)为arr1[i-1]=k的单调对数目
        # # 则dp(i,k)=sum(dp(i-1, l) for l in range(min(k+nums[i-1]-nums[i], nums[i-1])+1))
        # # 因为dp(i, *)只依赖dp(i-1, *)，所以可以状态压缩
        # dp = [0] * 1001
        # # 初始化
        # prev = nums[0]
        # for i in range(prev + 1):
        #     dp[i] = 1
        
        # for num in nums[1:]:
        #     # 先计算出arr1能有哪些值
        #     x = min(num, prev)
        #     accum = sum(dp[:x+1])
        #     for k in range(num, -1, -1):
        #         # k得从大往小算
        #         if accum > 0:
        #             tmp = dp[x]
        #             dp[k] = accum % MOD
        #             accum -= tmp
        #             x -= 1
        #         else:
        #             dp[k] = 0
        #     # 清空范围之外的
        #     for k in range(num+1, 51):
        #         dp[k] = 0
        #     prev = num

        # return sum(dp[:nums[-1]+1]) % MOD
    
        # 复习
        # 见到一个🐂B解法
        # https://leetcode.cn/problems/find-the-count-of-monotonic-pairs-ii/solutions/2876190/qian-zhui-he-you-hua-dppythonjavacgo-by-3biek/
        prex = nums[-1]
        for a, b in pairwise(nums[::-1]):
           if b < a - prex:
               return 0
           if a > b:
               prex -= a - b
        return comb(prex + len(nums), len(nums)) % (10 ** 9 + 7)
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.countOfPairs([40,40,40,40,41,42,43,44,45,45])) # 272278100
    print(solution.countOfPairs([2,3,2])) # 4
    print(solution.countOfPairs([5,5,5,5])) # 126