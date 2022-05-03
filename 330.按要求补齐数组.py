#
# @lc app=leetcode.cn id=330 lang=python3
#
# [330] 按要求补齐数组
#
# 给定一个已排序的正整数数组 nums，和一个正整数 n 。从[1, n] 区间内选取任意个数字补充到 nums 中，使得[1, n] 区间内的任何数字都可以用 nums 中某几个数字的和来表示。请输出满足上述要求的最少需要补充的数字个数。

# 示例 1:
# 输入: nums = [1, 3], n = 6
# 输出: 1
# 解释:
# 根据 nums 里现有的组合[1], [3], [1, 3]，可以得出 1, 3, 4。
# 现在如果我们将 2 添加到 nums 中， 组合变为: [1], [2], [3], [1, 3], [2, 3], [1, 2, 3]。
# 其和可以表示数字 1, 2, 3, 4, 5, 6，能够覆盖[1, 6] 区间里所有的数。
# 所以我们最少需要添加一个数字。

# 示例 2:
# 输入: nums = [1, 5, 10], n = 20
# 输出: 2
# 解释: 我们需要添加[2, 4]。

# 示例 3:
# 输入: nums = [1, 2, 2], n = 5
# 输出: 0

# 提示：
# 1 <= nums.length <= 1000
# 1 <= nums[i] <= 10^4
# nums 按 升序排列
# 1 <= n <= 2^31 - 1

# Hard

from typing import List
# @lc code=start


class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        # 遍历nums
        # 记cMax为截止当前位置（含）能表达的连续区间的最大值（consecutive max）
        # 当遍历到下一位置时，cMax的变化满足如下规律：
        # cMax(i + 1) = cMax(i) + nums[i + 1]  if nums[i+1] <= cMax(i) + 1
        # 否则就要补数
        patch = 0
        cMax = 0
        for num in nums:
            if num <= cMax + 1:
                cMax += num
            else:
                # 补数
                while num > cMax + 1 and cMax < n:
                    patch += 1
                    cMax = (cMax << 1) + 1
                cMax += num
            if cMax >= n:
                break

        while n > cMax:
            patch += 1
            cMax = (cMax << 1) + 1

        return patch

        # @lc code=end


if __name__ == "__main__":
    solution = Solution()
    print(solution.minPatches([], 7))
    print(solution.minPatches([1, 3], 6))
    print(solution.minPatches([1, 5, 10], 20))
    print(solution.minPatches([1, 2, 2], 5))
