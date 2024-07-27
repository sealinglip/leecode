#
# @lc app=leetcode.cn id=3101 lang=python3
#
# [3101] 交替子数组计数
#
# 给你一个二进制数组 nums 。

# 如果一个子数组中 不存在 两个 相邻 元素的值 相同 的情况，我们称这样的子数组为 交替子数组 。

# 返回数组 nums 中交替子数组的数量。


# 示例 1：
# 输入： nums = [0,1,1,1]
# 输出： 5
# 解释：
# 以下子数组是交替子数组：[0] 、[1] 、[1] 、[1] 以及 [0,1] 。

# 示例 2：
# 输入： nums = [1,0,1,0]
# 输出： 10
# 解释：
# 数组的每个子数组都是交替子数组。可以统计在内的子数组共有 10 个。

# 提示：
# 1 <= nums.length <= 10^5
# nums[i] 不是 0 就是 1 。

from typing import List
# @lc code=start
class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        # 找出每一段连续的最大交替子数组
        n = len(nums)
        l = r = res = 0
        while r < n:
            if r < n - 1 and nums[r] != nums[r + 1]:
                r += 1
            else:
                span = r - l + 2
                res += (span * (span - 1)) >> 1
                r += 1
                l = r

        return res
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.countAlternatingSubarrays([0,1,1,1])) # 5
    print(solution.countAlternatingSubarrays([1,0,1,0])) # 10