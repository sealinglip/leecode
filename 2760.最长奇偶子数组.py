#
# @lc app=leetcode.cn id=2760 lang=python3
#
# [2760] 最长奇偶子数组
#
# 给你一个下标从 0 开始的整数数组 nums 和一个整数 threshold 。

# 请你从 nums 的子数组中找出以下标 l 开头、下标 r 结尾 (0 <= l <= r < nums.length) 且满足以下条件的 最长子数组 ：

# nums[l] % 2 == 0
# 对于范围 [l, r - 1] 内的所有下标 i ，nums[i] % 2 != nums[i + 1] % 2
# 对于范围 [l, r] 内的所有下标 i ，nums[i] <= threshold
# 以整数形式返回满足题目要求的最长子数组的长度。

# 注意：子数组 是数组中的一个连续非空元素序列。

# 示例 1：
# 输入：nums = [3,2,5,4], threshold = 5
# 输出：3
# 解释：在这个示例中，我们选择从 l = 1 开始、到 r = 3 结束的子数组 => [2,5,4] ，满足上述条件。
# 因此，答案就是这个子数组的长度 3 。可以证明 3 是满足题目要求的最大长度。

# 示例 2：
# 输入：nums = [1,2], threshold = 2
# 输出：1
# 解释：
# 在这个示例中，我们选择从 l = 1 开始、到 r = 1 结束的子数组 => [2] 。
# 该子数组满足上述全部条件。可以证明 1 是满足题目要求的最大长度。

# 示例 3：
# 输入：nums = [2,3,4,5], threshold = 4
# 输出：3
# 解释：
# 在这个示例中，我们选择从 l = 0 开始、到 r = 2 结束的子数组 => [2,3,4] 。 
# 该子数组满足上述全部条件。
# 因此，答案就是这个子数组的长度 3 。可以证明 3 是满足题目要求的最大长度。
 

# 提示：
# 1 <= nums.length <= 100 
# 1 <= nums[i] <= 100 
# 1 <= threshold <= 100

from typing import List
# @lc code=start
class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        l = -1
        res = 0
        for i, num in enumerate(nums):
            if num <= threshold:
                if l == -1 and (num & 1):
                    continue
                if l == -1:
                    l = i
                    res = max(res, 1)
                    odd = False
                    continue
                elif odd ^ (num & 1):
                        odd = not odd
                        res = max(res, i + 1 - l)
                        continue
                elif not (num & 1):
                    l = i
                    odd = False
                    continue
            l = -1
        
        return res
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.longestAlternatingSubarray([4,10,3], 10)) # 2
    print(solution.longestAlternatingSubarray([1,2], 2)) # 1
    print(solution.longestAlternatingSubarray([3,2,5,4], 5)) # 3
    print(solution.longestAlternatingSubarray([2,3,4,5], 4)) # 3