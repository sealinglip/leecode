#
# @lc app=leetcode.cn id=1726 lang=python3
#
# [1726] 同积元组
#
# 给你一个由 不同 正整数组成的数组 nums ，请你返回满足 a * b = c * d 的元组(a, b, c, d) 的数量。其中 a、b、c 和 d 都是 nums 中的元素，且 a != b != c != d 。


# 示例 1：
# 输入：nums = [2, 3, 4, 6]
# 输出：8
# 解释：存在 8 个满足题意的元组：
# (2, 6, 3, 4), (2, 6, 4, 3), (6, 2, 3, 4), (6, 2, 4, 3)
# (3, 4, 2, 6), (4, 3, 2, 6), (3, 4, 6, 2), (4, 3, 6, 2)

# 示例 2：
# 输入：nums = [1, 2, 4, 5, 10]
# 输出：16
# 解释：存在 16 个满足题意的元组：
# (1, 10, 2, 5), (1, 10, 5, 2), (10, 1, 2, 5), (10, 1, 5, 2)
# (2, 5, 1, 10), (2, 5, 10, 1), (5, 2, 1, 10), (5, 2, 10, 1)
# (2, 10, 4, 5), (2, 10, 5, 4), (10, 2, 4, 5), (10, 2, 4, 5)
# (4, 5, 2, 10), (4, 5, 10, 2), (5, 4, 2, 10), (5, 4, 10, 2)


# 提示：
# 1 <= nums.length <= 1000
# 1 <= nums[i] <= 10^4
# nums 中的所有元素 互不相同

from collections import defaultdict
from typing import List
# @lc code=start


class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        product = defaultdict(int)
        n = len(nums)
        res = 0
        for i in range(1, n):
            for j in range(i):
                p = nums[i] * nums[j]
                if p in product:
                    res += product[p] * 2 * 2 * 2
                product[p] += 1

        return res
# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    print(solution.tupleSameProduct([2, 3, 4, 6, 8, 12]))  # 40
    print(solution.tupleSameProduct([2, 3, 4, 6]))  # 8
    print(solution.tupleSameProduct([1, 2, 4, 5, 10]))  # 16
