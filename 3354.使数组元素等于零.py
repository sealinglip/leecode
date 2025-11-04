#
# @lc app=leetcode.cn id=3354 lang=python3
#
# [3354] 使数组元素等于零
#
# https://leetcode.cn/problems/make-array-elements-equal-to-zero/description/
#
# algorithms
# Easy (55.75%)
# Likes:    17
# Dislikes: 0
# Total Accepted:    6.8K
# Total Submissions: 11.5K
# Testcase Example:  '[1,0,2,0,3]'
#
# 给你一个整数数组 nums 。
# 开始时，选择一个满足 nums[curr] == 0 的起始位置 curr ，并选择一个移动 方向 ：向左或者向右。
# 此后，你需要重复下面的过程：
# 
# 
# 如果 curr 超过范围 [0, n - 1] ，过程结束。
# 如果 nums[curr] == 0 ，沿当前方向继续移动：如果向右移，则 递增 curr ；如果向左移，则 递减 curr 。
# 如果 nums[curr] > 0:
# 
# 将 nums[curr] 减 1 。
# 反转 移动方向（向左变向右，反之亦然）。
# 沿新方向移动一步。
# 
# 
# 如果在结束整个过程后，nums 中的所有元素都变为 0 ，则认为选出的初始位置和移动方向 有效 。
# 
# 返回可能的有效选择方案数目。
# 
# 
# 示例 1：
# 输入：nums = [1,0,2,0,3]
# 输出：2
# 解释：
# 可能的有效选择方案如下：
# 选择 curr = 3 并向左移动。
# [1,0,2,0,3] -> [1,0,2,0,3] -> [1,0,1,0,3] -> [1,0,1,0,3] -> [1,0,1,0,2] ->
# [1,0,1,0,2] -> [1,0,0,0,2] -> [1,0,0,0,2] -> [1,0,0,0,1] -> [1,0,0,0,1] ->
# [1,0,0,0,1] -> [1,0,0,0,1] -> [0,0,0,0,1] -> [0,0,0,0,1] -> [0,0,0,0,1] ->
# [0,0,0,0,1] -> [0,0,0,0,0].
# 
# 选择 curr = 3 并向右移动。
# [1,0,2,0,3] -> [1,0,2,0,3] -> [1,0,2,0,2] -> [1,0,2,0,2] -> [1,0,1,0,2] ->
# [1,0,1,0,2] -> [1,0,1,0,1] -> [1,0,1,0,1] -> [1,0,0,0,1] -> [1,0,0,0,1] ->
# [1,0,0,0,0] -> [1,0,0,0,0] -> [1,0,0,0,0] -> [1,0,0,0,0] ->
# [0,0,0,0,0].
# 
# 
# 示例 2：
# 输入：nums = [2,3,4,0,4,1,0]
# 输出：0
# 解释：
# 不存在有效的选择方案。
# 
# 
# 提示：
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 100
# 至少存在一个元素 i 满足 nums[i] == 0 。
# 
# 
#

from typing import List
# @lc code=start
class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        total = sum(nums)
        selections = 1 if total & 1 else 2
        half = total >> 1
        half2 = total - half
        accu = 0
        res = 0
        for x in nums:
            if x == 0 and (accu == half or accu == half2):
                res += selections
            accu += x
    
        return res
        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.countValidSelections([16,13,10,0,0,0,10,6,7,8,7])) # 3
    print(solution.countValidSelections([1,0,2,0,3])) # 2
    print(solution.countValidSelections([1,0,2,0,0,3])) # 4
    print(solution.countValidSelections([2,3,4,0,4,1,0])) # 0