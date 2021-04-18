#
# @lc app=leetcode.cn id=179 lang=python3
#
# [179] 最大数
#
# 给定一组非负整数 nums，重新排列每个数的顺序（每个数不可拆分）使之组成一个最大的整数。
# 注意：输出结果可能非常大，所以你需要返回一个字符串而不是整数。

# 示例 1：
# 输入：nums = [10, 2]
# 输出："210"

# 示例 2：
# 输入：nums = [3, 30, 34, 5, 9]
# 输出："9534330"

# 示例 3：
# 输入：nums = [1]
# 输出："1"

# 示例 4：
# 输入：nums = [10]
# 输出："10"

# 提示：
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 10^9

from typing import List

# @lc code=start
from functools import cmp_to_key


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if len(nums) <= 1:
            return "".join([str(num) for num in nums])
        # 先转为字符
        strs = [str(num) for num in nums]
        # 对strs排序
        strs.sort(key=cmp_to_key(lambda x, y: int(y + x) - int(x + y)))
        res = "".join(strs)
        return "0" if res[0] == '0' else res
 # @lc code=end


if __name__ == "__main__":
    solution = Solution()
    print(solution.largestNumber([10, 2]))
    print(solution.largestNumber([3, 30, 34, 5, 9]))
    print(solution.largestNumber([1]))
    print(solution.largestNumber([10]))
