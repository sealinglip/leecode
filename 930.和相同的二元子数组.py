#
# @lc app=leetcode.cn id=930 lang=python3
#
# [930] 和相同的二元子数组
#
# 给你一个二元数组 nums ，和一个整数 goal ，请你统计并返回有多少个和为 goal 的 非空 子数组。
# 子数组 是数组的一段连续部分。

# 示例 1：
# 输入：nums = [1, 0, 1, 0, 1], goal = 2
# 输出：4
# 解释：
# 如下面黑体所示，有 4 个满足题目要求的子数组：
# [1, 0, 1, 0, 1]
# [1, 0, 1, 0, 1]
# [1, 0, 1, 0, 1]
# [1, 0, 1, 0, 1]

# 示例 2：
# 输入：nums = [0, 0, 0, 0, 0], goal = 0
# 输出：15

# 提示：
# 1 <= nums.length <= 3 * 10^4
# nums[i] 不是 0 就是 1
# 0 <= goal <= nums.length

from typing import List
# @lc code=start


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        # 前缀和
        accum, cnt = 0, 0
        accumCnt = {0: 1}
        for num in nums:
            accum += num
            t = accum - goal
            if t in accumCnt:
                cnt += accumCnt[t]
            accumCnt[accum] = accumCnt.get(accum, 0) + 1

        return cnt

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.numSubarraysWithSum([1, 0, 1, 0, 1], 2))
    print(solution.numSubarraysWithSum([0, 0, 0, 0, 0], 0))
