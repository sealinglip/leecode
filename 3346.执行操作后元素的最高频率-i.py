#
# @lc app=leetcode.cn id=3346 lang=python3
#
# [3346] 执行操作后元素的最高频率 I
#
# https://leetcode.cn/problems/maximum-frequency-of-an-element-after-performing-operations-i/description/
#
# algorithms
# Medium (25.49%)
# Likes:    9
# Dislikes: 0
# Total Accepted:    3.2K
# Total Submissions: 9.5K
# Testcase Example:  '[1,4,5]\n1\n2'
#
# 给你一个整数数组 nums 和两个整数 k 和 numOperations 。
# 你必须对 nums 执行 操作  numOperations 次。每次操作中，你可以：
# 
# 选择一个下标 i ，它在之前的操作中 没有 被选择过。
# 将 nums[i] 增加范围 [-k, k] 中的一个整数。
# 
# 在执行完所有操作以后，请你返回 nums 中出现 频率最高 元素的出现次数。
# 一个元素 x 的 频率 指的是它在数组中出现的次数。
# 
# 
# 示例 1：
# 输入：nums = [1,4,5], k = 1, numOperations = 2
# 输出：2
# 解释：
# 通过以下操作得到最高频率 2 ：
# 将 nums[1] 增加 0 ，nums 变为 [1, 4, 5] 。
# 将 nums[2] 增加 -1 ，nums 变为 [1, 4, 4] 。
# 
# 示例 2：
# 输入：nums = [5,11,20,20], k = 5, numOperations = 1
# 输出：2
# 解释：
# 通过以下操作得到最高频率 2 ：
# 将 nums[1] 增加 0 。
# 
# 
# 提示：
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^5
# 0 <= k <= 10^5
# 0 <= numOperations <= nums.length
# 
# 
#

from collections import Counter
from typing import List
# @lc code=start
class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        cnts = Counter(nums)
        keys = sorted(cnts.keys())
        ub = len(keys) - 1
        l = r = 0 # 闭区间[l, r]
        res = inRange = cnts[keys[0]]
        # 以每个元素为中心，判断
        for i, x in enumerate(keys):
            # 扩右边界
            while r < ub and keys[r+1] - x <= k:
                r += 1
                inRange += cnts[keys[r]]
            # 缩左边界
            while x - keys[l] > k:
                inRange -= cnts[keys[l]]
                l += 1
            res = max(res, cnts[x] + min(inRange-cnts[x], numOperations))
        # 以滑动窗口来判断
        r = 0
        inRange = cnts[keys[0]]
        for l, x in enumerate(keys):
            while r < ub and keys[r+1] - x <= (k << 1):
                r += 1
                inRange += cnts[keys[r]]
            res = max(res, min(inRange, numOperations))
            inRange -= cnts[x]

        return res

        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.maxFrequency([51,17,70], 10, 3)) # 2
    print(solution.maxFrequency([88,53], 27, 2)) # 2
    print(solution.maxFrequency([1,4,5], 1, 2)) # 2
    print(solution.maxFrequency([5,11,20,20], 5, 1)) # 2
