#
# @lc app=leetcode.cn id=532 lang=python3
#
# [532] 数组中的 k-diff 数对
#
# 给你一个整数数组 nums 和一个整数 k，请你在数组中找出 不同的 k-diff 数对，并返回不同的 k-diff 数对 的数目。

# k-diff 数对定义为一个整数对(nums[i], nums[j]) ，并满足下述全部条件：

# 0 <= i, j < nums.length
# i != j
# nums[i] - nums[j] == k
# 注意，| val | 表示 val 的绝对值。


# 示例 1：
# 输入：nums = [3, 1, 4, 1, 5], k = 2
# 输出：2
# 解释：数组中有两个 2-diff 数对, (1, 3) 和(3, 5)。
# 尽管数组中有两个 1 ，但我们只应返回不同的数对的数量。

# 示例 2：
# 输入：nums = [1, 2, 3, 4, 5], k = 1
# 输出：4
# 解释：数组中有四个 1-diff 数对, (1, 2), (2, 3), (3, 4) 和(4, 5) 。

# 示例 3：
# 输入：nums = [1, 3, 1, 5, 4], k = 0
# 输出：1
# 解释：数组中只有一个 0-diff 数对，(1, 1) 。


# 提示：
# 1 <= nums.length <= 10^4
# -10 ^ 7 <= nums[i] <= 10 ^ 7
# 0 <= k <= 10 ^ 7


from typing import List
# @lc code=start
from collections import Counter


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        res = 0
        cnt = Counter(nums)
        for n in sorted(cnt.keys()):
            if k:
                if (n-k) in cnt:
                    res += 1
            elif cnt[n] > 1:
                res += 1
        return res


        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.findPairs([3, 1, 4, 1, 5], 2))  # 2
    print(solution.findPairs([1, 2, 3, 4, 5], 1))  # 4
    print(solution.findPairs([1, 3, 1, 5, 4], 0))  # 1
