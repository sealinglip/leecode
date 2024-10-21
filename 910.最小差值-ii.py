#
# @lc app=leetcode.cn id=910 lang=python3
#
# [910] 最小差值 II
#
# 给你一个整数数组 nums，和一个整数 k 。

# 对于每个下标 i（0 <= i < nums.length），将 nums[i] 变成 nums[i] + k 或 nums[i] - k 。

# nums 的 分数 是 nums 中最大元素和最小元素的差值。

# 在更改每个下标对应的值之后，返回 nums 的最小 分数 。


# 示例 1：
# 输入：nums = [1], k = 0
# 输出：0
# 解释：分数 = max(nums) - min(nums) = 1 - 1 = 0 。

# 示例 2：
# 输入：nums = [0,10], k = 2
# 输出：6
# 解释：将数组变为 [2, 8] 。分数 = max(nums) - min(nums) = 8 - 2 = 6 。

# 示例 3：
# 输入：nums = [1,3,6], k = 3
# 输出：3
# 解释：将数组变为 [4, 6, 3] 。分数 = max(nums) - min(nums) = 6 - 3 = 3 。
 

# 提示：
# 1 <= nums.length <= 10^4
# 0 <= nums[i] <= 10^4
# 0 <= k <= 10^4

# 复习

from typing import List
# @lc code=start
class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()
        mi, ma = nums[0], nums[-1]
        # 要定一个分界点，分界点上的元素，都减k，分界点下的元素，加k
        # 遍历可能的分界点
        res = ma - mi
        ma -= k
        mi += k
        for i in range(len(nums) - 1):
            # [:i+1] +,  [(i+1):] -
            res = min(res, max(ma, nums[i]+k) - min(mi, nums[i+1]-k))
        return res                
        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.smallestRangeII([3, 1, 10], 4)) # 2
    print(solution.smallestRangeII([7, 8, 8], 5)) # 1
    print(solution.smallestRangeII([1], 0)) # 0
    print(solution.smallestRangeII([0, 10], 2)) # 6
    print(solution.smallestRangeII([1, 3, 5], 3)) # 4
    print(solution.smallestRangeII([1, 3, 6], 3)) # 3
