#
# @lc app=leetcode.cn id=1437 lang=python3
#
# [1437] 是否所有 1 都至少相隔 k 个元素
#
# https://leetcode.cn/problems/check-if-all-1s-are-at-least-length-k-places-away/description/
#
# algorithms
# Easy (56.05%)
# Likes:    41
# Dislikes: 0
# Total Accepted:    24.3K
# Total Submissions: 42.4K
# Testcase Example:  '[1,0,0,0,1,0,0,1]\n2'
#
# 给你一个由若干 0 和 1 组成的数组 nums 以及整数 k。如果所有 1 都至少相隔 k 个元素，则返回 true ；否则，返回 false。
# 
# 
# 示例 1：
# 输入：nums = [1,0,0,0,1,0,0,1], k = 2
# 输出：true
# 解释：每个 1 都至少相隔 2 个元素。
# 
# 示例 2：
# 输入：nums = [1,0,0,1,0,1], k = 2
# 输出：false
# 解释：第二个 1 和第三个 1 之间只隔了 1 个元素。
# 
# 
# 提示：
# 1 <= nums.length <= 10^5
# 0 <= k <= nums.length
# nums[i] 的值为 0 或 1
# 
# 
#

from typing import List
# @lc code=start
class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        gap = k
        n = len(nums)
        for i in range(n):
            if nums[i] == 1:
                if gap < k:
                    return False
                gap = 0
            else:
                gap += 1
        
        return True
        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.kLengthApart([1,0,0,0,1,0,0,1], 2)) # True
    print(solution.kLengthApart([1,0,0,1,0,1], 2)) # False
