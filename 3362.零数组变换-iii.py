#
# @lc app=leetcode.cn id=3362 lang=python3
#
# [3362] 零数组变换 III
#
# https://leetcode.cn/problems/zero-array-transformation-iii/description/
#
# algorithms
# Medium (34.75%)
# Likes:    21
# Dislikes: 0
# Total Accepted:    2.9K
# Total Submissions: 6.2K
# Testcase Example:  '[2,0,2]\n[[0,2],[0,2],[1,1]]'
#
# 给你一个长度为 n 的整数数组 nums 和一个二维数组 queries ，其中 queries[i] = [li, ri] 。
# 每一个 queries[i] 表示对于 nums 的以下操作：
# 
# 将 nums 中下标在范围 [li, ri] 之间的每一个元素 最多 减少 1 。
# 坐标范围内每一个元素减少的值相互 独立 。
# 
# 零数组 指的是一个数组里所有元素都等于 0 。
# 
# 请你返回 最多 可以从 queries 中删除多少个元素，使得 queries 中剩下的元素仍然能将 nums 变为一个 零数组 。如果无法将 nums
# 变为一个 零数组 ，返回 -1 。
# 
# 
# 示例 1：
# 输入：nums = [2,0,2], queries = [[0,2],[0,2],[1,1]]
# 输出：1
# 解释：
# 删除 queries[2] 后，nums 仍然可以变为零数组。
# 对于 queries[0] ，将 nums[0] 和 nums[2] 减少 1 ，将 nums[1] 减少 0 。
# 对于 queries[1] ，将 nums[0] 和 nums[2] 减少 1 ，将 nums[1] 减少 0 。
# 
# 示例 2：
# 输入：nums = [1,1,1,1], queries = [[1,3],[0,2],[1,3],[1,2]]
# 输出：2
# 解释：
# 可以删除 queries[2] 和 queries[3] 。
# 
# 示例 3：
# 输入：nums = [1,2,3,4], queries = [[0,3]]
# 输出：-1
# 解释：
# nums 无法通过 queries 变成零数组。
# 
# 
# 提示：
# 1 <= nums.length <= 10^5
# 0 <= nums[i] <= 10^5
# 1 <= queries.length <= 10^5
# queries[i].length == 2
# 0 <= li <= ri < nums.length
# 
# 复习

from heapq import heappop, heappush
from typing import List
# @lc code=start
class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        n, m = len(nums), len(queries)
        queries.sort(key = lambda x : x[0])
        hq = []
        diff = [0] * (n+1)
        op = j = 0
        for i, num in enumerate(nums):
            op += diff[i]
            while j < m and queries[j][0] == i:
                heappush(hq, -queries[j][1])
                j += 1
            while op < num and hq and -hq[0] >= i:
                op += 1
                diff[-heappop(hq) + 1] -= 1
            if op < num:
                return -1
        return len(hq)

        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.maxRemoval([2,0,2], [[0,2],[0,2],[1,1]])) # 1
    print(solution.maxRemoval([1,1,1,1], [[1,3],[0,2],[1,3],[1,2]])) # 2
    print(solution.maxRemoval([1,2,3,4], [[0,3]])) # -1
