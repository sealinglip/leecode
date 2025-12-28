# 给你一个整数数组 nums 和一个整数 k。你的任务是将 nums 分割成一个或多个 非空 的连续子段，使得每个子段的 最大值 与 最小值 之间的差值 不超过 k。
# 返回在此条件下将 nums 分割的总方法数。
# 由于答案可能非常大，返回结果需要对 109 + 7 取余数。


# 示例 1：
# 输入： nums = [9,4,1,3,7], k = 4
# 输出： 6
# 解释：
# 共有 6 种有效的分割方式，使得每个子段中的最大值与最小值之差不超过 k = 4：
# [[9], [4], [1], [3], [7]]
# [[9], [4], [1], [3, 7]]
# [[9], [4], [1, 3], [7]]
# [[9], [4, 1], [3], [7]]
# [[9], [4, 1], [3, 7]]
# [[9], [4, 1, 3], [7]]

# 示例 2：
# 输入： nums = [3,3,4], k = 0
# 输出： 2
# 解释：
# 共有 2 种有效的分割方式，满足给定条件：
# [[3], [3], [4]]
# [[3, 3], [4]]
 

# 提示：
# 2 <= nums.length <= 5 * 10^4
# 1 <= nums[i] <= 10^9
# 0 <= k <= 10^9

from typing import List

from sortedcontainers import SortedList

class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        MOD = 10 ** 9 + 7
        # 动规 + 移动窗口
        n = len(nums)
        # 记dp[i]为前i个元素的分隔方式数
        dp = [0] * (n+1)
        preSum = [0] * (n+1) # 为了加速计算，对dp求前缀和
        dp[0] = preSum[0] = 1

        win = SortedList() # 移动窗口
        
        i = 0 # 移动窗口左边界
        for j in range(n):
            win.add(nums[j])
            while win[-1] - win[0] > k:
                win.remove(nums[i])
                i += 1
            
            dp[j+1] = (preSum[j] - (preSum[i-1] if i > 0 else 0)) % MOD
            preSum[j+1] = (preSum[j] + dp[j+1]) % MOD

        return dp[n]


if __name__ == "__main__":
    solution = Solution()
    print(solution.countPartitions([9,4,1,3,7], 4)) # 6
    print(solution.countPartitions([3,3,4], 0)) # 2

        