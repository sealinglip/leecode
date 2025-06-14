#
# @lc app=leetcode.cn id=3355 lang=python3
#
# [3355] 零数组变换 I
#
# https://leetcode.cn/problems/zero-array-transformation-i/description/
#
# algorithms
# Medium (44.27%)
# Likes:    34
# Dislikes: 0
# Total Accepted:    9.8K
# Total Submissions: 18.8K
# Testcase Example:  '[1,0,1]\n[[0,2]]'
#
# 给定一个长度为 n 的整数数组 nums 和一个二维数组 queries，其中 queries[i] = [li, ri]。
# 
# 对于每个查询 queries[i]：
# 在 nums 的下标范围 [li, ri] 内选择一个下标 子集。
# 将选中的每个下标对应的元素值减 1。
# 
# 零数组 是指所有元素都等于 0 的数组。
# 如果在按顺序处理所有查询后，可以将 nums 转换为 零数组 ，则返回 true，否则返回 false。
# 
# 
# 示例 1：
# 输入： nums = [1,0,1], queries = [[0,2]]
# 输出： true
# 解释：
# 对于 i = 0：
# 选择下标子集 [0, 2] 并将这些下标处的值减 1。
# 数组将变为 [0, 0, 0]，这是一个零数组。
# 
# 示例 2：
# 输入： nums = [4,3,2,1], queries = [[1,3],[0,2]]
# 输出： false
# 解释：
# 对于 i = 0： 
# 选择下标子集 [1, 2, 3] 并将这些下标处的值减 1。
# 数组将变为 [4, 2, 1, 0]。
# 
# 对于 i = 1：
# 选择下标子集 [0, 1, 2] 并将这些下标处的值减 1。
# 数组将变为 [3, 1, 0, 0]，这不是一个零数组。
# 
# 
# 提示：
# 1 <= nums.length <= 10^5
# 0 <= nums[i] <= 10^5
# 1 <= queries.length <= 10^5
# queries[i].length == 2
# 0 <= li <= ri < nums.length
# 


from typing import List
# @lc code=start
class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        assist = [0] * n
        for l, r in queries:
            assist[l] += 1
            if r < n-1:
                assist[r+1] -= 1
        
        preSum = 0
        for num, a in zip(nums, assist):
            preSum += a
            if preSum < num:
                return False
        
        return True
        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.isZeroArray([1,0,1], [[0,2]])) # True
    print(solution.isZeroArray([4,3,2,1], [[1,3],[0,2]])) # False
