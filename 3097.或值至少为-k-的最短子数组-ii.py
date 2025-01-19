#
# @lc app=leetcode.cn id=3097 lang=python3
#
# [3097] 或值至少为 K 的最短子数组 II
#
# 给你一个 非负 整数数组 nums 和一个整数 k 。
# 如果一个数组中所有元素的按位或运算 OR 的值 至少 为 k ，那么我们称这个数组是 特别的 。
# 请你返回 nums 中 最短特别非空 子数组的长度，如果特别子数组不存在，那么返回 -1 。


# 示例 1：
# 输入：nums = [1,2,3], k = 2
# 输出：1
# 解释：
# 子数组 [3] 的按位 OR 值为 3 ，所以我们返回 1 。

# 示例 2：
# 输入：nums = [2,1,8], k = 10
# 输出：3
# 解释：
# 子数组 [2,1,8] 的按位 OR 值为 11 ，所以我们返回 3 。

# 示例 3：
# 输入：nums = [1,2], k = 0
# 输出：1
# 解释：
# 子数组 [1] 的按位 OR 值为 1 ，所以我们返回 1 。


# 提示：
# 1 <= nums.length <= 2 * 10^5
# 0 <= nums[i] <= 10^9
# 0 <= k <= 10^9

from math import inf
from typing import List
# @lc code=start
class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        if k == 0:
            return 1
        
        res = inf
        n = len(nums)

        def test(start: int, asc: bool) -> int:
            v = 0
            if asc:
                while v < k and start < n:
                    v |= nums[start]
                    start += 1
                return start-1 if v >= k else -1
            else:
                while v < k and start >= 0:
                    v |= nums[start]
                    start -= 1
                return start+1 if v >= k else -1 

        # 双指针
        l = r = 0
        while l < n:
            r = test(l, True)
            if r == -1:
                break
            l = test(r, False)
            if l == -1:
                break
            res = min(res, r-l+1)
            l += 1

        return -1 if res == inf else res
        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.minimumSubarrayLength([1,2,3], 2)) # 1
    print(solution.minimumSubarrayLength([2,1,8], 10)) # 3
    print(solution.minimumSubarrayLength([1,2], 0)) # 1
