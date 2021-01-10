#
# @lc app=leetcode.cn id=220 lang=python3
#
# [220] 存在重复元素 III
#
# 在整数数组 nums 中，是否存在两个下标 i 和 j，使得 nums [i] 和 nums [j] 的差的绝对值小于等于 t ，且满足 i 和 j 的差的绝对值也小于等于 ķ 。
# 如果存在则返回 true，不存在返回 false。

# 示例 1:
# 输入: nums = [1,2,3,1], k = 3, t = 0
# 输出: true

# 示例 2:
# 输入: nums = [1,0,1,1], k = 1, t = 2
# 输出: true

# 示例 3:
# 输入: nums = [1,5,9,1,5,9], k = 2, t = 3
# 输出: false

from typing import List
# @lc code=start


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if not nums or t < 0 or k < 0:
            return False

        # 桶排序
        buckets = {}
        bucketSize = t + 1  # 桶大小
        for i, num in enumerate(nums):
            bucketNum = num // bucketSize  # 应该放入哪个桶

            if bucketNum in buckets:  # 该桶不为空，说明存在这样的两个数满足条件
                return True

            buckets[bucketNum] = num  # 入桶
            # 判断前一个桶的元素及后一个桶的元素，跟本桶元素的距离
            if ((bucketNum - 1) in buckets and abs(buckets[bucketNum - 1] - num) < bucketSize) \
                    or ((bucketNum + 1) in buckets and abs(buckets[bucketNum + 1] - num) < bucketSize):
                return True

            # 删除移出区间的元素对应的桶
            if i >= k:
                buckets.pop(nums[i - k] // bucketSize)

        return False
# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    print(solution.containsNearbyAlmostDuplicate([1, 2, 3, 1], 3, 0))
    print(solution.containsNearbyAlmostDuplicate([1, 0, 1, 1], 1, 2))
    print(solution.containsNearbyAlmostDuplicate([1, 5, 9, 1, 5, 9], 2, 3))
