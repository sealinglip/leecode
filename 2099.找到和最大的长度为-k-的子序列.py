#
# @lc app=leetcode.cn id=2099 lang=python3
#
# [2099] 找到和最大的长度为 K 的子序列
#
# https://leetcode.cn/problems/find-subsequence-of-length-k-with-the-largest-sum/description/
#
# algorithms
# Easy (49.85%)
# Likes:    63
# Dislikes: 0
# Total Accepted:    20.4K
# Total Submissions: 36.6K
# Testcase Example:  '[2,1,3,3]\n2'
#
# 给你一个整数数组 nums 和一个整数 k 。你需要找到 nums 中长度为 k 的 子序列 ，且这个子序列的 和最大 。
# 请你返回 任意 一个长度为 k 的整数子序列。
# 子序列 定义为从一个数组里删除一些元素后，不改变剩下元素的顺序得到的数组。
# 
# 
# 示例 1：
# 输入：nums = [2,1,3,3], k = 2
# 输出：[3,3]
# 解释：
# 子序列有最大和：3 + 3 = 6 。
# 
# 示例 2：
# 输入：nums = [-1,-2,3,4], k = 3
# 输出：[-1,3,4]
# 解释：
# 子序列有最大和：-1 + 3 + 4 = 6 。
# 
# 示例 3：
# 输入：nums = [3,4,3,3], k = 2
# 输出：[3,4]
# 解释：
# 子序列有最大和：3 + 4 = 7 。
# 另一个可行的子序列为 [4, 3] 。
# 
# 
# 提示：
# 1 <= nums.length <= 1000
# -10^5 <= nums[i] <= 10^5
# 1 <= k <= nums.length
# 
#

from heapq import heappop, heappush
from typing import List
# @lc code=start
class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        # 方法1：
        # l = 0
        # hq = [] # 小顶堆
        # for i, num in enumerate(nums):
        #     if l < k:
        #         heappush(hq, (num, i))
        #         l += 1
        #     elif num > hq[0][0]:
        #         heappop(hq)
        #         heappush(hq, (num, i))
        
        # return [nums[i] for _, i in sorted(hq, key=lambda e : e[1])]

        # 方法2：
        return [nums[i] for _, i in sorted(sorted(((num, i) for i, num in enumerate(nums)), reverse=True)[:k], key=lambda e : e[1])]
    
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.maxSubsequence([2,1,3,3], 2)) # [3,3]
    print(solution.maxSubsequence([-1,-2,3,4], 3)) # [-1,3,4]
    print(solution.maxSubsequence([3,4,3,3], 2)) # [3,4]
