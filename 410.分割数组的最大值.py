#
# @lc app=leetcode.cn id=410 lang=python3
#
# [410] 分割数组的最大值
#
# 给定一个非负整数数组 nums 和一个整数 k ，你需要将这个数组分成 k 个非空的连续子数组。
# 设计一个算法使得这 k 个子数组各自和的最大值最小。

# 示例 1：
# 输入：nums = [7,2,5,10,8], k = 2
# 输出：18
# 解释：
# 一共有四种方法将 nums 分割为 2 个子数组。 
# 其中最好的方式是将其分为 [7,2,5] 和 [10,8] 。
# 因为此时这两个子数组各自的和的最大值为18，在所有情况中最小。

# 示例 2：
# 输入：nums = [1,2,3,4,5], k = 2
# 输出：9

# 示例 3：
# 输入：nums = [1,4,4], k = 3
# 输出：4

# 提示：
# 1 <= nums.length <= 1000
# 0 <= nums[i] <= 10^6
# 1 <= k <= min(50, nums.length)

# Hard

from math import inf
from typing import List
# @lc code=start
from functools import cache
from itertools import accumulate

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        # 方法1：动规和记忆化
        # 记dp(i,j)为前i个数分成连续的j堆，最小的最大值
        # dp(i+1, j) = min(max(dp(k, j-1), sum(nums[k:i+1])) for k in range(j-1,i+1))
        # preSum = [0] + list(accumulate(nums))

        # @cache
        # def dp(i: int, j: int) -> int:
        #     if j == 1:
        #         return preSum[i] - preSum[0]
        #     elif i == j:
        #         return max(nums[:i])
        #     elif i < j: # 不合理
        #         return inf
        #     else:
        #         return min(max(dp(k, j-1), preSum[i] - preSum[k]) for k in range(j-1, i))
            
        # return dp(len(nums), k)
    
        # 方法2：二分查找
        def check(i: int) -> bool:
            '''
            检查能否将nums分k份，每份和不超过i
            '''
            subSum = grp = 0
            for n in nums:
                if subSum + n <= i:
                    subSum += n
                elif grp < k:
                    grp += 1
                    subSum = n
                else:
                    return False
            return grp < k


        l, r = max(nums), sum(nums) # 最小的最大值一定位于这个区间
        while l < r:
            mid = (l + r) >> 1
            if check(mid):
                r = mid
            else:
                l = mid + 1
        return l

# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.splitArray([7,2,5,10,8], 2)) # 18
    print(solution.splitArray([1,2,3,4,5], 2)) # 9
    print(solution.splitArray([1,4,4], 3)) # 4