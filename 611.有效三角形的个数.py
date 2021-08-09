#
# @lc app=leetcode.cn id=611 lang=python3
#
# [611] 有效三角形的个数
#
# 给定一个包含非负整数的数组，你的任务是统计其中可以组成三角形三条边的三元组个数。

# 示例 1:
# 输入: [2,2,3,4]
# 输出: 3
# 解释:
# 有效的组合是:
# 2,3,4 (使用第一个 2)
# 2,3,4 (使用第二个 2)
# 2,2,3

# 注意:
# 数组长度不超过1000。
# 数组里整数的范围为 [0, 1000]。

from typing import List
# @lc code=start
from bisect import bisect_left


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()

        sum = 0
        N = len(nums)
        for i in range(N):
            if nums[i]:
                # 对于每个nums[i]，求j和k
                j = i + 1
                while j < N:
                    t = nums[i] + nums[j]
                    # nums[k] 必须小于t
                    k = bisect_left(nums, t, j + 1)
                    sum += k - j - 1
                    j += 1

        return sum


        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.triangleNumber([2, 2, 3, 4]))
