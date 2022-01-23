#
# @lc app=leetcode.cn id=219 lang=python3
#
# [219] 存在重复元素 II
#
# 给你一个整数数组 nums 和一个整数 k ，判断数组中是否存在两个 不同的索引 i 和 j ，满足 nums[i] == nums[j] 且 abs(i - j) <= k 。如果存在，返回 true ；否则，返回 false 。


# 示例 1：
# 输入：nums = [1, 2, 3, 1], k = 3
# 输出：true

# 示例 2：
# 输入：nums = [1, 0, 1, 1], k = 1
# 输出：true

# 示例 3：
# 输入：nums = [1, 2, 3, 1, 2, 3], k = 2
# 输出：false


# 提示：
# 1 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
# 0 <= k <= 10^5

from typing import List
# @lc code=start
from collections import Counter


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        k += 1
        N = len(nums)
        cnt = Counter(nums[:min(k, N)])  # 先构造计数器
        if cnt.most_common(1)[0][1] > 1:
            return True

        if k < N:
            for i in range(k, N):
                cnt[nums[i - k]] -= 1
                if cnt[nums[i]] >= 1:
                    return True
                cnt[nums[i]] += 1

        return False


        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.containsNearbyDuplicate([1, 2, 3, 1], 3))  # True
    print(solution.containsNearbyDuplicate([1, 0, 1, 1], 1))  # True
    print(solution.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2))  # False
