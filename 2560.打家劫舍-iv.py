#
# @lc app=leetcode.cn id=2560 lang=python3
#
# [2560] 打家劫舍 IV
#
# 沿街有一排连续的房屋。每间房屋内都藏有一定的现金。现在有一位小偷计划从这些房屋中窃取现金。

# 由于相邻的房屋装有相互连通的防盗系统，所以小偷 不会窃取相邻的房屋 。

# 小偷的 窃取能力 定义为他在窃取过程中能从单间房屋中窃取的 最大金额 。

# 给你一个整数数组 nums 表示每间房屋存放的现金金额。形式上，从左起第 i 间房屋中放有 nums[i] 美元。

# 另给你一个整数 k ，表示窃贼将会窃取的 最少 房屋数。小偷总能窃取至少 k 间房屋。

# 返回小偷的 最小 窃取能力。


# 示例 1：
# 输入：nums = [2, 3, 5, 9], k = 2
# 输出：5
# 解释：
# 小偷窃取至少 2 间房屋，共有 3 种方式：
# - 窃取下标 0 和 2 处的房屋，窃取能力为 max(nums[0], nums[2]) = 5 。
# - 窃取下标 0 和 3 处的房屋，窃取能力为 max(nums[0], nums[3]) = 9 。
# - 窃取下标 1 和 3 处的房屋，窃取能力为 max(nums[1], nums[3]) = 9 。
# 因此，返回 min(5, 9, 9) = 5 。

# 示例 2：
# 输入：nums = [2, 7, 9, 3, 1], k = 2
# 输出：2
# 解释：共有 7 种窃取方式。窃取能力最小的情况所对应的方式是窃取下标 0 和 4 处的房屋。返回 max(nums[0], nums[4]) = 2 。


# 提示：
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^9
# 1 <= k <= (nums.length + 1)/2

# 复习

from bisect import bisect_left
from typing import List
# @lc code=start


class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def f(ma: int) -> int:
            """
            返回单间最大偷ma金额时，可以偷的最大房屋数目
            """
            cnt, choosen = 0, False
            for n in nums:
                if n <= ma and not choosen:
                    cnt, choosen = cnt + 1, True
                else:
                    choosen = False
            return cnt

        return bisect_left(range(min(nums), max(nums)), k, key=f) + min(nums)
# @lc code=end


if __name__ == "__name__":
    solution = Solution()
    print(solution.minCapability([2, 3, 5, 9], 2))  # 5
    print(solution.minCapability([2, 7, 9, 3, 1], k=2))  # 2
