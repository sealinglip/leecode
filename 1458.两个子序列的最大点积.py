#
# @lc app=leetcode.cn id=1458 lang=python3
#
# [1458] 两个子序列的最大点积
#
# https://leetcode.cn/problems/max-dot-product-of-two-subsequences/description/
#
# algorithms
# Hard (52.47%)
# Likes:    140
# Dislikes: 0
# Total Accepted:    21.3K
# Total Submissions: 36.6K
# Testcase Example:  '[2,1,-2,5]\n[3,0,-6]'
#
# 给你两个数组 nums1 和 nums2 。
# 
# 请你返回 nums1 和 nums2 中两个长度相同的 非空 子序列的最大点积。
# 
# 数组的非空子序列是通过删除原数组中某些元素（可能一个也不删除）后剩余数字组成的序列，但不能改变数字间相对顺序。比方说，[2,3,5] 是
# [1,2,3,4,5] 的一个子序列而 [1,5,3] 不是。
# 
# 
# 示例 1：
# 输入：nums1 = [2,1,-2,5], nums2 = [3,0,-6]
# 输出：18
# 解释：从 nums1 中得到子序列 [2,-2] ，从 nums2 中得到子序列 [3,-6] 。
# 它们的点积为 (2*3 + (-2)*(-6)) = 18 。
# 
# 示例 2：
# 输入：nums1 = [3,-2], nums2 = [2,-6,7]
# 输出：21
# 解释：从 nums1 中得到子序列 [3] ，从 nums2 中得到子序列 [7] 。
# 它们的点积为 (3*7) = 21 。
# 
# 示例 3：
# 输入：nums1 = [-1,-1], nums2 = [1,1]
# 输出：-1
# 解释：从 nums1 中得到子序列 [-1] ，从 nums2 中得到子序列 [1] 。
# 它们的点积为 -1 。
# 
# 
# 提示：
# 1 <= nums1.length, nums2.length <= 500
# -1000 <= nums1[i], nums2[i] <= 1000
# 
# 
# 点积：
# 定义 a = [a1, a2,…, an] 和 b = [b1, b2,…, bn] 的点积为：
# 
# 
# 这里的 Σ 指示总和符号。
# 
# 
#

from functools import cache
from typing import List
# @lc code=start
class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        # # 方法1：动规之记忆化搜索
        # m, n = len(nums1) - 1, len(nums2) - 1
        # @cache
        # def maxDotProduct(idx1: int, idx2: int) -> int:
        #     """
        #     计算nums1[idx1:]和nums2[idx2:]的子序列最大点积
            
        #     :param idx1: nums1中的起始索引
        #     :type idx1: int
        #     :param idx2: nums2中的起始索引
        #     :type idx2: int
        #     :return: 子序列最大点积
        #     :rtype: int
        #     """
        #     res = nums1[idx1] * nums2[idx2] + max(maxDotProduct(idx1 + 1, idx2 + 1) if (idx1 < m and idx2 < n) else 0, 0)
        #     if idx1 < m:
        #         res = max(res, maxDotProduct(idx1 + 1, idx2))
        #     if idx2 < n:
        #         res = max(res, maxDotProduct(idx1, idx2 + 1))
        #     return res
        
        # return maxDotProduct(0, 0)
    
        # 方法2：动规之递推
        m, n = len(nums1), len(nums2)
        dp = [0] * n
        newDp = [0] * n
        
        for i in range(m):
            for j in range(n):
                xij = nums1[i] * nums2[j]
                newDp[j] = xij
                if i > 0:
                    newDp[j] = max(newDp[j], dp[j])
                if j > 0:
                    newDp[j] = max(newDp[j], newDp[j - 1])
                if i > 0 and j > 0:
                    newDp[j] = max(newDp[j], dp[j - 1] + xij)

            dp, newDp = newDp, dp

        return dp[-1]

        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.maxDotProduct([-5,-1,-2], [3,3,5,5])) # -3
    print(solution.maxDotProduct([2,1,-2,5], [3,0,-6])) # 18
    print(solution.maxDotProduct([3,-2], [2,-6,7])) # 21
    print(solution.maxDotProduct([-1,-1], [1,1])) # -1
