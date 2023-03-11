#
# @lc app=leetcode.cn id=1590 lang=python3
#
# [1590] 使数组和能被 P 整除
#
# 给你一个正整数数组 nums，请你移除 最短 子数组（可以为 空），使得剩余元素的 和 能被 p 整除。 不允许 将整个数组都移除。

# 请你返回你需要移除的最短子数组的长度，如果无法满足题目要求，返回 - 1 。

# 子数组 定义为原数组中连续的一组元素。


# 示例 1：
# 输入：nums = [3, 1, 4, 2], p = 6
# 输出：1
# 解释：nums 中元素和为 10，不能被 p 整除。我们可以移除子数组[4] ，剩余元素的和为 6 。

# 示例 2：
# 输入：nums = [6, 3, 5, 2], p = 9
# 输出：2
# 解释：我们无法移除任何一个元素使得和被 9 整除，最优方案是移除子数组[5, 2] ，剩余元素为[6, 3]，和为 9 。

# 示例 3：
# 输入：nums = [1, 2, 3], p = 3
# 输出：0
# 解释：和恰好为 6 ，已经能被 3 整除了。所以我们不需要移除任何元素。

# 示例  4：
# 输入：nums = [1, 2, 3], p = 7
# 输出：- 1
# 解释：没有任何方案使得移除子数组后剩余元素的和被 7 整除。

# 示例 5：
# 输入：nums = [1000000000, 1000000000, 1000000000], p = 3
# 输出：0


# 提示：
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^9
# 1 <= p <= 10^9

# 复习

from typing import List
# @lc code=start


class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        x = sum(nums) % p  # 余数
        if x == 0:
            return 0

        y = 0
        idx = {0: -1}
        res = len(nums)
        for i, v in enumerate(nums):
            y = (y + v) % p  # 前 i+1 个元素和 除以 p 的余数
            if (r := (y - x) % p) in idx:
                # idx[r] 表示余数为 r 的 最长前缀和
                # 前i+1个元素和除以p，余数为y，前idx[r]+1个元素和除以p，余数为r
                # r = (y - x) % p => x = (y - r) % p
                # idx[r]:i 之间的元素和 除以p，余数为x
                # 去掉 idx[r]:i 之间的元素，整个数组和一定能整除p
                res = min(res, i - idx[r])
            idx[y] = i
        return res if res < len(nums) else -1

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.minSubarray([3, 1, 4, 2], 6))  # 1
    print(solution.minSubarray([6, 3, 5, 2], 9))  # 2
    print(solution.minSubarray([1, 2, 3], 3))  # 0
    print(solution.minSubarray([1, 2, 3], 7))  # -1
    print(solution.minSubarray(
        [1000000000, 1000000000, 1000000000], 3))  # 0
