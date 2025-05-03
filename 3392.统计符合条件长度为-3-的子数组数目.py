#
# @lc app=leetcode.cn id=3392 lang=python3
#
# [3392] 统计符合条件长度为 3 的子数组数目
#
# https://leetcode.cn/problems/count-subarrays-of-length-three-with-a-condition/description/
#
# algorithms
# Easy (63.27%)
# Likes:    14
# Dislikes: 0
# Total Accepted:    6.7K
# Total Submissions: 9.8K
# Testcase Example:  '[1,2,1,4,1]'
#
# 给你一个整数数组 nums ，请你返回长度为 3 的 子数组，满足第一个数和第三个数的和恰好为第二个数的一半。
# 子数组 指的是一个数组中连续 非空 的元素序列。
# 
# 
# 示例 1：
# 输入：nums = [1,2,1,4,1]
# 输出：1
# 解释：
# 只有子数组 [1,4,1] 包含 3 个元素且第一个和第三个数字之和是中间数字的一半。number.
# 
# 
# 示例 2：
# 输入：nums = [1,1,1]
# 输出：0
# 解释：
# [1,1,1] 是唯一长度为 3 的子数组，但第一个数和第三个数的和不是第二个数的一半。
# 
# 
# 提示：
# 3 <= nums.length <= 100
# -100 <= nums[i] <= 100
#

from typing import List
# @lc code=start
class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for i in range(1, n-1):
            if ((nums[i-1] + nums[i+1]) << 1) == nums[i]:
                res += 1
        return res
        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.countSubarrays([1,2,1,4,1])) # 1
    print(solution.countSubarrays([1,1,1])) # 0
