#
# @lc app=leetcode.cn id=2009 lang=python3
#
# [2009] 使数组连续的最少操作数
#
# 给你一个整数数组 nums 。每一次操作中，你可以将 nums 中 任意 一个元素替换成 任意 整数。

# 如果 nums 满足以下条件，那么它是 连续的 ：

# nums 中所有元素都是 互不相同 的。
# nums 中 最大 元素与 最小 元素的差等于 nums.length - 1 。
# 比方说，nums = [4, 2, 5, 3] 是 连续的 ，但是 nums = [1, 2, 3, 5, 6] 不是连续的 。

# 请你返回使 nums 连续 的 最少 操作次数。
 

# 示例 1：
# 输入：nums = [4,2,5,3]
# 输出：0
# 解释：nums 已经是连续的了。

# 示例 2：
# 输入：nums = [1,2,3,5,6]
# 输出：1
# 解释：一个可能的解是将最后一个元素变为 4 。
# 结果数组为 [1,2,3,5,4] ，是连续数组。

# 示例 3：
# 输入：nums = [1,10,100,1000]
# 输出：3
# 解释：一个可能的解是：
# - 将第二个元素变为 2 。
# - 将第三个元素变为 3 。
# - 将第四个元素变为 4 。
# 结果数组为 [1,2,3,4] ，是连续数组。
 

# 提示：
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^9
# Hard

from bisect import bisect_left
from typing import List
# @lc code=start
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        nums = sorted(list(set(nums)))
        # 滑动窗口
        maxInWin = 1
        right = 0
        for i, left in enumerate(nums): # 以数组中的每个数作为区间的左边界（含）
            right = bisect_left(nums, left+n, right)
            maxInWin = max(maxInWin, right - i)
            if right >= n:
                break
        return n - maxInWin 
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.minOperations([8,5,9,9,8,4])) # 2
    print(solution.minOperations([4,2,5,3])) # 0
    print(solution.minOperations([1,2,3,5,6])) # 1
    print(solution.minOperations([1,10,100,1000])) # 3