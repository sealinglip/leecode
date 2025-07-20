#
# @lc app=leetcode.cn id=2163 lang=python3
#
# [2163] 删除元素后和的最小差值
#
# https://leetcode.cn/problems/minimum-difference-in-sums-after-removal-of-elements/description/
#
# algorithms
# Hard (49.71%)
# Likes:    45
# Dislikes: 0
# Total Accepted:    5.3K
# Total Submissions: 9.8K
# Testcase Example:  '[3,1,2]'
#
# 给你一个下标从 0 开始的整数数组 nums ，它包含 3 * n 个元素。
# 你可以从 nums 中删除 恰好 n 个元素，剩下的 2 * n 个元素将会被分成两个 相同大小 的部分。
# 前面 n 个元素属于第一部分，它们的和记为 sumfirst 。
# 后面 n 个元素属于第二部分，它们的和记为 sumsecond 。
# 
# 两部分和的 差值 记为 sumfirst - sumsecond 。
# 
# 比方说，sumfirst = 3 且 sumsecond = 2 ，它们的差值为 1 。
# 再比方，sumfirst = 2 且 sumsecond = 3 ，它们的差值为 -1 。
# 
# 请你返回删除 n 个元素之后，剩下两部分和的 差值的最小值 是多少。
# 
# 
# 示例 1：
# 输入：nums = [3,1,2]
# 输出：-1
# 解释：nums 有 3 个元素，所以 n = 1 。
# 所以我们需要从 nums 中删除 1 个元素，并将剩下的元素分成两部分。
# - 如果我们删除 nums[0] = 3 ，数组变为 [1,2] 。两部分和的差值为 1 - 2 = -1 。
# - 如果我们删除 nums[1] = 1 ，数组变为 [3,2] 。两部分和的差值为 3 - 2 = 1 。
# - 如果我们删除 nums[2] = 2 ，数组变为 [3,1] 。两部分和的差值为 3 - 1 = 2 。
# 两部分和的最小差值为 min(-1,1,2) = -1 。
# 
# 示例 2：
# 输入：nums = [7,9,5,8,1,3]
# 输出：1
# 解释：n = 2 。所以我们需要删除 2 个元素，并将剩下元素分为 2 部分。
# 如果我们删除元素 nums[2] = 5 和 nums[3] = 8 ，剩下元素为 [7,9,1,3] 。和的差值为 (7+9) - (1+3) = 12。
# 为了得到最小差值，我们应该删除 nums[1] = 9 和 nums[4] = 1 ，剩下的元素为 [7,5,8,3] 。和的差值为 (7+5) - (8+3) = 1 。
# 观察可知，最优答案为 1 。
# 
# 
# 提示：
# nums.length == 3 * n
# 1 <= n <= 10^5
# 1 <= nums[i] <= 10^5
# 
# 
#

from heapq import heapify, heapreplace
from typing import List
# @lc code=start
class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 3
        # 切割点的索引只能为[n, 2n+1]
        # 按切割点从左到右遍历，求出左半部分保留n个值的最小和
        hq = [-nums[i] for i in range(n)] # 小顶堆，转成负值
        heapify(hq)
        lmin = [0] * (n+1)
        lmin[0] = -sum(hq)
        for i in range(1, n+1):
            x = -nums[i + n - 1]
            if x <= hq[0]:
                lmin[i] = lmin[i-1]
            else:
                y = heapreplace(hq, x)
                lmin[i] = lmin[i-1] + y - x

        # 按切割点从右到左遍历，求出右半部分保留n个值的最大和
        hq = list(nums[n<<1:])
        heapify(hq)
        rmax = [0] * (n+1)
        rmax[n] = sum(hq)
        for i in range(n-1, -1, -1):
            x = nums[n + i]
            if x <= hq[0]:
                rmax[i] = rmax[i+1]
            else:
                y = heapreplace(hq, x)
                rmax[i] = rmax[i+1] - y + x

        return min(lmin[i] - rmax[i] for i in range(n+1))

        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.minimumDifference([3,1,2])) # -1
    print(solution.minimumDifference([7,9,5,8,1,3])) # 1
