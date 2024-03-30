#
# @lc app=leetcode.cn id=1793 lang=python3
#
# [1793] 好子数组的最大分数
#
# 给你一个整数数组 nums （下标从 0 开始）和一个整数 k 。

# 一个子数组 (i, j) 的 分数 定义为 min(nums[i], nums[i+1], ..., nums[j]) * (j - i + 1) 。一个 好 子数组的两个端点下标需要满足 i <= k <= j 。
# 请你返回 好 子数组的最大可能 分数 。


# 示例 1：
# 输入：nums = [1,4,3,7,4,5], k = 3
# 输出：15
# 解释：最优子数组的左右端点下标是 (1, 5) ，分数为 min(4,3,7,4,5) * (5-1+1) = 3 * 5 = 15 。

# 示例 2：
# 输入：nums = [5,5,4,5,4,1,1,1], k = 0
# 输出：20
# 解释：最优子数组的左右端点下标是 (0, 4) ，分数为 min(5,5,4,5,4) * (4-0+1) = 4 * 5 = 20 。
 

# 提示：
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 2 * 10^4
# 0 <= k < nums.length

# Hard
# 复习


from typing import List
# @lc code=start
class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        # 以k为中心，往两侧延展，双指针，记录当前范围内最小值
        res = nums[k]
        mi = nums[k]
        l = r = k
        n = len(nums) - 1
        while l > 0 or r < n:
            if l == 0 or (r < n and nums[l-1] < nums[r+1]):
                r += 1
                mi = min(mi, nums[r])
            else:
                l -= 1
                mi = min(mi, nums[l])
            res = max(res, mi * (r - l + 1))

        return res
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.maximumScore([1,4,3,7,4,5], 3)) # 15
    print(solution.maximumScore([5,5,4,5,4,1,1,1], 0)) # 20