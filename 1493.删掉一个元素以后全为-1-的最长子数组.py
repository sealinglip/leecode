#
# @lc app=leetcode.cn id=1493 lang=python3
#
# [1493] 删掉一个元素以后全为 1 的最长子数组
#
# https://leetcode.cn/problems/longest-subarray-of-1s-after-deleting-one-element/description/
#
# algorithms
# Medium (66.81%)
# Likes:    198
# Dislikes: 0
# Total Accepted:    77.2K
# Total Submissions: 113.4K
# Testcase Example:  '[1,1,0,1]'
#
# 给你一个二进制数组 nums ，你需要从中删掉一个元素。
# 请你在删掉元素的结果数组中，返回最长的且只包含 1 的非空子数组的长度。
# 如果不存在这样的子数组，请返回 0 。
# 
# 
# 提示 1：
# 输入：nums = [1,1,0,1]
# 输出：3
# 解释：删掉位置 2 的数后，[1,1,1] 包含 3 个 1 。
# 
# 示例 2：
# 输入：nums = [0,1,1,1,0,1,1,0,1]
# 输出：5
# 解释：删掉位置 4 的数字后，[0,1,1,1,1,1,0,1] 的最长全 1 子数组为 [1,1,1,1,1] 。
# 
# 示例 3：
# 输入：nums = [1,1,1]
# 输出：2
# 解释：你必须要删除一个元素。
# 
# 
# 提示：
# 1 <= nums.length <= 10^5
# nums[i] 要么是 0 要么是 1 。
# 
# 
#

from typing import List
# @lc code=start
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        res = gap = prevOnes = ones = 0
        for x in nums:
            if x == 1:
                ones += 1
                gap = 0
            else:
                gap += 1
                if gap == 1:
                    res = max(res, prevOnes + ones)
                    prevOnes = ones
                    ones = 0
                else:
                    prevOnes = 0
        if gap == 0:
            # 以1结尾
            res = max(res, prevOnes + ones)
            if res == len(nums):
                res -= 1
        return res
        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.longestSubarray([1,1,0,1])) # 3
    print(solution.longestSubarray([0,1,1,1,0,1,1,0,1])) # 5
    print(solution.longestSubarray([1,1,1])) # 2
