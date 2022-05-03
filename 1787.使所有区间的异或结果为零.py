#
# @lc app=leetcode.cn id=1787 lang=python3
#
# [1787] 使所有区间的异或结果为零
#
# 给你一个整数数组 nums​​​ 和一个整数 k​​​​​ 。区间[left, right]（left <= right）的 异或结果 是对下标位于 left 和 right（包括 left 和 right ）之间所有元素进行 XOR 运算的结果：nums[left] XOR nums[left+1] XOR ... XOR nums[right]。
# 返回数组中 要更改的最小元素数 ，以使所有长度为 k 的区间异或结果等于零。

# 示例 1：
# 输入：nums = [1, 2, 0, 3, 0], k = 1
# 输出：3
# 解释：将数组[1, 2, 0, 3, 0] 修改为[0, 0, 0, 0, 0]

# 示例 2：
# 输入：nums = [3, 4, 5, 2, 1, 7, 3, 4, 7], k = 3
# 输出：3
# 解释：将数组[3, 4, 5, 2, 1, 7, 3, 4, 7] 修改为[3, 4, 7, 3, 4, 7, 3, 4, 7]

# 示例 3：
# 输入：nums = [1, 2, 4, 1, 2, 5, 1, 2, 6], k = 3
# 输出：3
# 解释：将数组[1, 2, 4, 1, 2, 5, 1, 2, 6] 修改为[1, 2, 3, 1, 2, 3, 1, 2, 3]

# 提示：
# 1 <= k <= nums.length <= 2000
# ​​​​​​0 <= nums[i] < 2^10
# Hard

from typing import List
# @lc code=start
from collections import Counter


class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        MAXN = 2 ** 10
        L = len(nums)

        dp = [float('inf')] * MAXN
        dp[0] = 0  # 边界条件

        for i in range(k):
            cnt = Counter([nums[j] for j in range(i, L, k)])
            size = sum(cnt.values())

            tmp = [min(dp)] * MAXN
            for mask in range(MAXN):
                for x, c in cnt.items():
                    tmp[mask] = min(tmp[mask], dp[mask ^ x] - c)

            dp = [v + size for v in tmp]

        return dp[0]


        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.minChanges([1, 2, 0, 3, 0], 1))
    print(solution.minChanges([3, 4, 5, 2, 1, 7, 3, 4, 7], 3))
    print(solution.minChanges([1, 2, 4, 1, 2, 5, 1, 2, 6], 3))
