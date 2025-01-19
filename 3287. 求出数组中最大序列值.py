# 给你一个整数数组 nums 和一个 正 整数 k 。

# 定义长度为 2 * x 的序列 seq 的 值 为：
# (seq[0] OR seq[1] OR ... OR seq[x - 1]) XOR (seq[x] OR seq[x + 1] OR ... OR seq[2 * x - 1]).
# 请你求出 nums 中所有长度为 2 * k 的 子序列 的 最大值 。


# 示例 1：
# 输入：nums = [2,6,7], k = 1
# 输出：5
# 解释：
# 子序列 [2, 7] 的值最大，为 2 XOR 7 = 5 。

# 示例 2：
# 输入：nums = [4,2,5,6,7], k = 2
# 输出：2

# 解释：
# 子序列 [4, 5, 6, 7] 的值最大，为 (4 OR 5) XOR (6 OR 7) = 2 。

# 提示：
# 2 <= nums.length <= 400
# 1 <= nums[i] < 2^7
# 1 <= k <= nums.length / 2

# Hard

from typing import List, Set

class Solution:
    def maxValue(self, nums: List[int], k: int) -> int:
        n = len(nums)
        def findPossibleOrs(arr: List[int]) -> List[Set[int]]:
            dp = [] # dp[i]记的是arr[:i+1]的长度为k的子序列所有可能的OR值，如果凑不够kge，那就是空集
            prev = [set() for _ in range(k+1)] # prev[j]记录到之前的位置，长度为j的子序列的所有可能的OR值
            prev[0].add(0)
            for i, num in enumerate(arr):
                for j in range(min(k-1, i+1), -1, -1):
                    for x in prev[j]:
                        prev[j+1].add(x | num)
                dp.append(prev[k].copy())
            return dp

        A = findPossibleOrs(nums)
        B = findPossibleOrs(nums[::-1])

        res = 0
        for i in range(k-1, n-k):
            res = max(res, *(a ^ b for a in A[i] for b in B[n-i-2]))
        return res

if __name__ == "__main__":
    solution = Solution()
    print(solution.maxValue([2,6,7], 1)) # 5
    print(solution.maxValue([4,2,5,6,7], 2)) # 2
