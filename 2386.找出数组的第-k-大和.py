#
# @lc app=leetcode.cn id=2386 lang=python3
#
# [2386] 找出数组的第 K 大和
#
# 给你一个整数数组 nums 和一个 正 整数 k 。你可以选择数组的任一 子序列 并且对其全部元素求和。
# 数组的 第 k 大和 定义为：可以获得的第 k 个 最大 子序列和（子序列和允许出现重复）
# 返回数组的 第 k 大和 。

# 子序列是一个可以由其他数组删除某些或不删除元素派生而来的数组，且派生过程不改变剩余元素的顺序。
# 注意：空子序列的和视作 0 。


# 示例 1：
# 输入：nums = [2,4,-2], k = 5
# 输出：2
# 解释：所有可能获得的子序列和列出如下，按递减顺序排列：
# - 6、4、4、2、2、0、0、-2
# 数组的第 5 大和是 2 。

# 示例 2：
# 输入：nums = [1,-2,3,4,-10,12], k = 16
# 输出：10
# 解释：数组的第 16 大和是 10 。
 

# 提示：
# n == nums.length
# 1 <= n <= 10^5
# -10^9 <= nums[i] <= 10^9
# 1 <= k <= min(2000, 2^n)

# Hard
# 复习

from collections import Counter
from heapq import heappop, heappush
from typing import List
# @lc code=start
class Solution:
    def kSum(self, nums: List[int], k: int) -> int:
        # 第k个最大子序列和等于数组总和减第k个最小子序列和
        n = len(nums)
        total = 0
        for i in range(n):
            if nums[i] >= 0:
                total += nums[i]
            else:
                nums[i] = -nums[i]
        nums.sort()

        kMin = 0
        hq = [(nums[0], 0)] # 优先队列中元素(t, i) 代表以第i个元素结尾的和为t的子序列
        for j in range(2, k + 1):
            t, i = heappop(hq)
            kMin = t
            if i == n-1:
                continue
            heappush(hq, (t + nums[i+1], i+1))
            heappush(hq, (t -nums[i] + nums[i+1], i+1))

        return total - kMin

# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.kSum([2,4,-2], 5)) # 2
    print(solution.kSum([1,-2,3,4,-10,12], 16)) # 10