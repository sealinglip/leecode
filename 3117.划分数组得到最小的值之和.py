#
# @lc app=leetcode.cn id=3117 lang=python3
#
# [3117] 划分数组得到最小的值之和
#
# 给你两个数组 nums 和 andValues，长度分别为 n 和 m。
# 数组的 值 等于该数组的 最后一个 元素。
# 你需要将 nums 划分为 m 个 不相交的连续 子数组，对于第 ith 个子数组 [li, ri]，子数组元素的按位 AND 运算结果等于 andValues[i]，
# 换句话说，对所有的 1 <= i <= m，nums[li] & nums[li + 1] & ... & nums[ri] == andValues[i] ，其中 & 表示按位 AND 运算符。
# 返回将 nums 划分为 m 个子数组所能得到的可能的 最小 子数组 值 之和。如果无法完成这样的划分，则返回 -1 。


# 示例 1：
# 输入： nums = [1,4,3,3,2], andValues = [0,3,3,2]
# 输出： 12
# 解释：
# 唯一可能的划分方法为：
# [1,4] 因为 1 & 4 == 0
# [3] 因为单元素子数组的按位 AND 结果就是该元素本身
# [3] 因为单元素子数组的按位 AND 结果就是该元素本身
# [2] 因为单元素子数组的按位 AND 结果就是该元素本身
# 这些子数组的值之和为 4 + 3 + 3 + 2 = 12

# 示例 2：
# 输入： nums = [2,3,5,7,7,7,5], andValues = [0,7,5]
# 输出： 17
# 解释：
# 划分 nums 的三种方式为：
# [[2,3,5],[7,7,7],[5]] 其中子数组的值之和为 5 + 7 + 5 = 17
# [[2,3,5,7],[7,7],[5]] 其中子数组的值之和为 7 + 7 + 5 = 19
# [[2,3,5,7,7],[7],[5]] 其中子数组的值之和为 7 + 7 + 5 = 19
# 子数组值之和的最小可能值为 17

# 示例 3：
# 输入： nums = [1,2,3,4], andValues = [2]
# 输出： -1
# 解释：
# 整个数组 nums 的按位 AND 结果为 0。由于无法将 nums 划分为单个子数组使得元素的按位 AND 结果为 2，因此返回 -1。


# 提示：
# 1 <= n == nums.length <= 10^4
# 1 <= m == andValues.length <= min(n, 10)
# 1 <= nums[i] < 10^5
# 0 <= andValues[j] < 10^5

# 复习
# Hard

from functools import cache
from math import inf
from typing import List
# @lc code=start
class Solution:
    def minimumValueSum(self, nums: List[int], andValues: List[int]) -> int:
        n, m = len(nums), len(andValues)
        # 动规
        # 记dp(i,j)为数组的前i个元素分解成j个子数组，满足andValues前j个限制条件时的最小可能值和，i >= j
        # dp(0, 0) = 0
        # 对于前i个元素分解成j个子数组来说，最后一个子数组对最小可能值和的贡献一定是nums[i-1]，且最后的子数组的AND值一定是andValues[j-1]
        # 下面的解法会TLE
        # 可以对紧邻的重复元素进行优化处理
        @cache
        def dp(i: int, j: int) -> int:
            if j == 0 or i == 0:
                return 0 if i == 0 and j == 0 else inf
            a = nums[i-1]
            pre = inf
            for k in range(i-1, max(-1, j-2), -1):
                if a == andValues[j-1]:
                    pre = min(pre, dp(k, j-1))
                elif a < andValues[j-1] or k == 0:
                    break
                a &= nums[k-1]

            return inf if pre == inf else pre + nums[i-1]
        
        res = dp(n, m)

        return -1 if res == inf else res
    
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.minimumValueSum([2] * 100, [2] * 10)) # 20
    print(solution.minimumValueSum([2] * 10000, [2] * 10)) # 20
    print(solution.minimumValueSum([507,507,507,507], [507])) # 507
    print(solution.minimumValueSum([1,4,3,3,2], [0,3,3,2])) # 12
    print(solution.minimumValueSum([2,3,5,7,7,7,5], [0,7,5])) # 17
    print(solution.minimumValueSum([1,2,3,4], [2])) # -1
