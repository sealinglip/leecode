#
# @lc app=leetcode.cn id=2962 lang=python3
#
# [2962] 统计最大元素出现至少 K 次的子数组
#
# https://leetcode.cn/problems/count-subarrays-where-max-element-appears-at-least-k-times/description/
#
# algorithms
# Medium (56.24%)
# Likes:    65
# Dislikes: 0
# Total Accepted:    21.1K
# Total Submissions: 36.3K
# Testcase Example:  '[1,3,2,3,3]\n2'
#
# 给你一个整数数组 nums 和一个 正整数 k 。
# 请你统计有多少满足 「 nums 中的 最大 元素」至少出现 k 次的子数组，并返回满足这一条件的子数组的数目。
# 子数组是数组中的一个连续元素序列。
# 
# 
# 示例 1：
# 输入：nums = [1,3,2,3,3], k = 2
# 输出：6
# 解释：包含元素 3 至少 2 次的子数组为：[1,3,2,3]、[1,3,2,3,3]、[3,2,3]、[3,2,3,3]、[2,3,3] 和 [3,3]。
# 
# 示例 2：
# 输入：nums = [1,4,2,1], k = 3
# 输出：0
# 解释：没有子数组包含元素 4 至少 3 次。
# 
# 提示：
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^6
# 1 <= k <= 10^5
# 
#
from typing import List

# @lc code=start
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        ma = max(nums)
        res = cnt = 0
        cntMap = {0:1}
        preSum = 0
        for num in nums:
            if num == ma:
                cnt += 1
                if cnt >= k:
                    preSum += cntMap[cnt-k]
            cntMap[cnt] = cntMap.get(cnt, 0) + 1
            res += preSum

        return res
        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.countSubarrays([1,3,2,3,3], 2)) # 6
    print(solution.countSubarrays([1,4,2,1], 3)) # 0
    