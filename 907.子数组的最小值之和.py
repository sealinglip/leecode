#
# @lc app=leetcode.cn id=907 lang=python3
#
# [907] 子数组的最小值之和
#
# 给定一个整数数组 arr，找到 min(b) 的总和，其中 b 的范围为 arr 的每个（连续）子数组。

# 由于答案可能很大，因此 返回答案模 10 ^ 9 + 7 。


# 示例 1：
# 输入：arr = [3, 1, 2, 4]
# 输出：17
# 解释：
# 子数组为[3]，[1]，[2]，[4]，[3, 1]，[1, 2]，[2, 4]，[3, 1, 2]，[1, 2, 4]，[3, 1, 2, 4]。
# 最小值为 3，1，2，4，1，1，2，1，1，1，和为 17。

# 示例 2：
# 输入：arr = [11, 81, 94, 43, 3]
# 输出：444


# 提示：
# 1 <= arr.length <= 3 * 10^4
# 1 <= arr[i] <= 3 * 10^4

# 复习

from typing import List
# @lc code=start

MOD = 10 ** 9 + 7


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        monoStack = [] # 单调递增栈
        # 记dp(i)为以arr[i]为右边界（包含）的子数组最小值之和，那么有
        # dp(i) = sum(min(arr[j:i+1]) for j in range(i+1))
        # 设以arr[i]为最右且最小的最长子序列长度为k
        # if j >= i-k+1, min(arr[j:i+1]) == arr[i]
        # if j < i-k+1, min(arr[j:i+1]) == min(arr[j:i-k])
        # 则有：
        # dp(i) = sum(min(arr[j:i+1]) for j in range(i+1))
        #       = sum(min(arr[j:i-k] for j in range(i-k+1))) + k * arr[i]
        #       = dp(i-k) + k * arr[i]
        dp = [0] * n
        ans = 0
        for i, x in enumerate(arr):
            while monoStack and arr[monoStack[-1]] > x:
                monoStack.pop()
            k = i - monoStack[-1] if monoStack else i + 1
            dp[i] = k * x + (dp[i - k] if monoStack else 0)
            ans = (ans + dp[i]) % MOD
            monoStack.append(i)

        return ans

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.sumSubarrayMins([3,1,2,4])) # 17
    print(solution.sumSubarrayMins([11,81,94,43,3])) # 444