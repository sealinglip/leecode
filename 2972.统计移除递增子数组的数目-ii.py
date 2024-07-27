#
# @lc app=leetcode.cn id=2972 lang=python3
#
# [2972] 统计移除递增子数组的数目 II
#
# 给你一个下标从 0 开始的 正 整数数组 nums 。

# 如果 nums 的一个子数组满足：移除这个子数组后剩余元素 严格递增 ，那么我们称这个子数组为 移除递增 子数组。比方说，[5, 3, 4, 6, 7] 中的 [3, 4] 是一个移除递增子数组，因为移除该子数组后，[5, 3, 4, 6, 7] 变为 [5, 6, 7] ，是严格递增的。

# 请你返回 nums 中 移除递增 子数组的总数目。

# 注意 ，剩余元素为空的数组也视为是递增的。

# 子数组 指的是一个数组中一段连续的元素序列。


# 示例 1：
# 输入：nums = [1,2,3,4]
# 输出：10
# 解释：10 个移除递增子数组分别为：[1], [2], [3], [4], [1,2], [2,3], [3,4], [1,2,3], [2,3,4] 和 [1,2,3,4]。移除任意一个子数组后，剩余元素都是递增的。注意，空数组不是移除递增子数组。

# 示例 2：
# 输入：nums = [6,5,7,8]
# 输出：7
# 解释：7 个移除递增子数组分别为：[5], [6], [5,7], [6,5], [5,7,8], [6,5,7] 和 [6,5,7,8] 。
# nums 中只有这 7 个移除递增子数组。

# 示例 3：
# 输入：nums = [8,7,6,6]
# 输出：3
# 解释：3 个移除递增子数组分别为：[8,7,6], [7,6,6] 和 [8,7,6,6] 。注意 [8,7] 不是移除递增子数组因为移除 [8,7] 后 nums 变为 [6,6] ，它不是严格递增的。
 

# 提示：
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^9

# Hard

from typing import List
# @lc code=start
class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        n = len(nums)
        # 先从左往右找严格递增子序列的右边界
        l = 0
        while l < n-1 and nums[l] < nums[l+1]:
            l += 1
        # 如果整个数组严格递增，直接返回结果
        if l == n-1: # 每个非空子数组都是“移除递增子数组”
            return (n * (n+1)) >> 1
        
        # 再从右往左找严格递增子序列的左边界
        res = l + 2 # 如果移除子数组右边界与数组右边界重合，“移除递增子数组”为i+2（严格递增前缀数组长度为i+1，可切的空当为k+2）
        r = n-1
        while r == n-1 or nums[r] < nums[r+1]:  # nums[r:]为严格递增子序列
            # 如果切到r前
            while l >= 0 and nums[l] >= nums[r]:
                l -= 1
            # 可移除的“移除递增子数组”有nums[0:r] …… nums[l+1:r]，还是l+2个
            res += l+2
            r -= 1
        return res
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.incremovableSubarrayCount([1,2,3,4])) # 10
    print(solution.incremovableSubarrayCount([6,5,7,8])) # 7
    print(solution.incremovableSubarrayCount([8,7,6,6])) # 3