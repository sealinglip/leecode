#
# @lc app=leetcode.cn id=719 lang=python3
#
# [719] 找出第 k 小的距离对
#
# 给定一个整数数组，返回所有数对之间的第 k 个最小距离。一对(A, B) 的距离被定义为 A 和 B 之间的绝对差值。

# 示例 1:

# 输入：
# nums = [1, 3, 1]
# k = 1
# 输出：0
# 解释：
# 所有数对如下：
# (1, 3) -> 2
# (1, 1) -> 0
# (3, 1) -> 2
# 因此第 1 个最小距离的数对是(1, 1)，它们之间的距离为 0。
# 提示:

# 2 <= len(nums) <= 10000.
# 0 <= nums[i] < 1000000.
# 1 <= k <= len(nums) * (len(nums) - 1) / 2.

from typing import KeysView, List
# @lc code=start
from heapq import *
from collections import Counter


class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        # 下面的实现会TLE
        # nums.sort()
        # N = len(nums)

        # q = [(nums[i+1]-nums[i], i, i + 1) for i in range(N - 1)]  # 初始化
        # heapify(q)

        # cnt = 0
        # while cnt < k:
        #     cnt += 1
        #     dis, i, j = heappop(q)
        #     if cnt == k:
        #         return dis
        #     if j < N - 1:
        #         heappush(q, (nums[j + 1] - nums[i], i, j + 1))

        # # 优化 —— 这样能解决有很多重复元素的场景，但如果单纯就是k很大而且数组并不重复，时间复杂度仍然是o(N ^ 2 * log N)，会TLE
        # stat = Counter(nums)
        # keys = list(stat.keys())
        # keys.sort()
        # N = len(keys)
        # zeroPairs = sum([stat[k] * (stat[k] - 1) // 2
        #                  for k in keys if stat[k] > 1], 0)  # 距离为0的数对个数
        # if k <= zeroPairs:
        #     return 0
        # k -= zeroPairs

        # # 初始化
        # q = [(keys[i+1]-keys[i], stat[keys[i]] * stat[keys[i + 1]], i, i+1)
        #      for i in range(N-1)]
        # heapify(q)

        # while k > 0:
        #     dis, cnt, i, j = heappop(q)
        #     if k <= cnt:
        #         return dis
        #     k -= cnt
        #     if j < N - 1:
        #         heappush(q, (keys[j+1]-keys[i], stat[keys[i]]
        #                      * stat[keys[j + 1]], i, j+1))

        # 双指针
        def possible(guess):
            # Is there k or more pairs with distance <= guess?
            count = left = 0
            for right, x in enumerate(nums):
                while x - nums[left] > guess:
                    left += 1
                count += right - left
            return count >= k

        nums.sort()
        lo = 0
        hi = nums[-1] - nums[0]
        while lo < hi:
            mi = (lo + hi) >> 1
            if possible(mi):
                hi = mi
            else:
                lo = mi + 1

        return lo

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.smallestDistancePair([95, 29, 47, 58, 80, 65, 26, 7, 69, 0, 1, 53, 61, 46, 66, 30, 78, 25, 1, 62, 5, 1,
                                         78, 60, 81, 100, 52, 33, 9, 52, 7, 74, 94, 93, 47, 68, 80, 81, 50, 31, 9, 96, 8, 8, 64, 4, 40, 22, 50, 93], 1142))  # 79
    print(solution.smallestDistancePair([1, 3, 1], 1))  # 0
    print(solution.smallestDistancePair([1, 6, 1], 3))  # 5
