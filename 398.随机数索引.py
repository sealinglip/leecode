#
# @lc app=leetcode.cn id=398 lang=python3
#
# [398] 随机数索引
#
# 给定一个可能含有重复元素的整数数组，要求随机输出给定的数字的索引。 您可以假设给定的数字一定存在于数组中。

# 注意：
# 数组大小可能非常大。 使用太多额外空间的解决方案将不会通过测试。

# 示例:

# int[] nums = new int[] {1, 2, 3, 3, 3}
# Solution solution = new Solution(nums)

# // pick(3) 应该返回索引 2, 3 或者 4。每个索引的返回概率应该相等。
# solution.pick(3)

# // pick(1) 应该返回 0。因为只有nums[0]等于1。
# solution.pick(1)

from typing import List
# @lc code=start
from collections import defaultdict
from random import choice


class Solution:

    def __init__(self, nums: List[int]):
        self.di = defaultdict(list)
        for i, n in enumerate(nums):
            self.di[n].append(i)

    def pick(self, target: int) -> int:
        return choice(self.di[target])

        # Your Solution object will be instantiated and called as such:
        # obj = Solution(nums)
        # param_1 = obj.pick(target)
        # @lc code=end
if __name__ == "__main__":
    nums = [1, 2, 3, 3, 3]
    solution = Solution(nums)
    print(solution.pick(3))
    print(solution.pick(1))
